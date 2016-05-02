# handles JSON parsing for the game Evolution
import sys, os, json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

from trait import Trait
from species import Species
from inPlayer import Player
from dealer import Dealer
from trait_card import TraitCard
from wateringWhole import WateringHole

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../../externalPlayer'))

from sillyPlayer import SillyPlayer


##  Feeding_j = [Player, Natural+, LOP]
##  Player_j = [["id",Natural+], ["species",LOS], ["bag",Natural]]
## LOP_j = [Player, ..., Player]
## LOS_j = [Species+, ..., Species+]
## Species+_j = [["food",Nat], ["body",Nat], ["population",Nat], ["traits",LOT], ["fat-food" ,Nat]]
## Species_j = [["food",Nat], ["body",Nat], ["population",Nat], ["traits",LOT]]
## Species+ = Species_j or Species+_j
## Situation_j = [Species+, Species+, OptSpecies, OptSpecies]
## OptSpecies = Species+ or False
## Configuration = [LOP+, Natural, LOC]
## LOP+ = A LOP+ is [Player+, ..., Player+].
## A Player+ is one of a regular Player_j or Player+_j
## A Player+_j =   [["id",Natural+], ["species",LOS], ["bag",Natural], ["cards",LOC]]
## LOC = [SpeciesCard, ..., SpeciesCard]
## SpeciesCard = [FoodValue, Trait]
## Species+ with a 0-valued "fat-food" field renders as a plain Species;
## FoodValue is a JSON number interpretable as an integer between -8 and 8 (inclusive).
## Player+ with a []-valued "cards" field renders as a plain Player

##==========
# A Step4 is [Action4, ..., Action4].
# An Action4 is [Natural, [GP, ...], [GB, ...], [BT, ...], [RT, ...]].

# Interpretation Every natural number in an Action4 represent an index into a sequence of species boards or cards. The first natural number specifies the card that a player is turning into food.

# Constraints The embedded arrays (GP, GB, BT, and RT) may be empty.

# The dealer must ensure that the specified species board and card indexes are within the range appropriate for the corresponding player. If an error is discovered, the dealer may abort; the test harness outputs nothing on STDOUT.

# A GP is ["population",Natural, Natural].

# Interpretation A ["population",i,j] array requests a trade of card j for a growth of the population of species board i by one.

# A GB is ["body",Natural, Natural].

# Interpretation A ["body",i,j] array requests a trade of card j for a growth of the body of species board i by one.

# A BT is one of:
# [Natural]

# [Natural, Natural]

# [Natural, Natural, Natural]

# [Natural, Natural, Natural, Natural]

# Interpretation A BT represents a species board addition to the right of the existing
# sequence of boards for the corresponding player. Specifically, [i, j, ..., k] uses the first of the players cards (i) to
#  "pay" for the new board and uses the remaining (up to three) cards (j, ..., k) as traits.

# Constraint Once a player has added a species board, it becomes impossible to add a trait.

# An RT is [Natural, Natural, Natural].

# Interpretation An RT represents a trait replacement for a species board. Specifically, [b, i, j]
# specifies that board b's i's trait card is replaced with the j's card from the player's card sequence.

# A PlayerAction is [[GP, ...], [GB, ...], [BT, ...], [RT, ...]]

def parse_species_card(species_card_json):
	"""
	converts from a json card to a TraitCard
	:param species_card_json: SpeciesCard
	:return: TraitCard
	"""
	try:
		[food_value, t] = species_card_json
		return TraitCard(Trait(t), food_value)
	except ValueError:
		raise ValueError("invalid species_card")

def parse_loc(loc_json):
	"""
	converts from a list of SpeciesCards to a list of TraitCards
	:param loc_json: [SpeciesCard, ...]
	:return: [TraitCard, ...]
	"""
	loc = []
	for card in loc_json:
		loc.append(parse_species_card(card))
	return loc

def parse_player(player_json):
	"""
	converts the json representation of a player into a player representation
	:param player_json: Player+
	:return: Player
	"""
	try:
		if len(player_json) == 4:
			[[i, given_id], [l, los], [b, bag], [c, loc]] = player_json
			if (i == "id" and l == "species" and b == "bag" and c == "cards"):
				player = Player(given_id, parse_los(los), bag)
				if loc:
					player.setHand(parse_loc(loc))
					return player
				else:
					return player
		else:
			[[i, given_id], [l, los], [b, bag]] = player_json
			if (i == "id" and l == "species" and b == "bag"):
				return Player(given_id, parse_los(los), bag)
	except ValueError:
		raise ValueError("invalid player")

def parse_playerEx(player_json):
	"""
	converts the json representation of a player into a player representation
	:param player_json: Player+
	:return: Player
	"""
	try:
		if len(player_json) == 4:
			[[i, given_id], [l, los], [b, bag], [c, loc]] = player_json
			if (i == "id" and l == "species" and b == "bag" and c == "cards"):
				player = SillyPlayer(given_id, parse_los(los), bag)
				if loc:
					player.setHand(parse_loc(loc))
					return player
				else:
					return player
		else:
			[[i, given_id], [l, los], [b, bag]] = player_json
			if (i == "id" and l == "species" and b == "bag"):
				return SillyPlayer(given_id, parse_los(los), bag)
	except ValueError:
		raise ValueError("invalid player")


def parse_lop(lop_json):
	"""
	converts from a list of json players to a list of players
	:param lop_json: LOP_j
	:return: [Player, ...]
	"""
	lop = []
	for player_json in lop_json:
		lop.append(parse_player(player_json))
	return lop

def parse_species(species_json):
	"""
	converts from a json representation of species to a species representation
	:param species_json: Species+
	:return: Species
	"""
	try:
		if (len(species_json) == 5):
			[[f, food], [b, body], [p, population], [t, lot], [fb, fat_food]] = species_json
			if (f == "food" and b == "body" and p == "population" and t == "traits" and fb == "fat-food"):
				species = Species(food, body, population, parse_lot(lot))
				if fat_food == 0:
					return species
				species.setFatFood(fat_food)
				return species
		else:
			[[f, food], [b, body], [p, population], [t, lot]] = species_json
			if (f == "food" and b == "body" and p == "population" and t == "traits"):
				return Species(food, body, population, parse_lot(lot))
	except ValueError:
		raise ValueError("invalid species")

def parse_los(los_json):
	"""
	convert from a list of json species to a list of species
	:param los_json: LOS_j
	:return: [Species, ...]
	"""
	los = []
	for species_json in los_json:
		los.append(parse_species(species_json))
	return los

def parse_lolos(lolos_json):
	"""
	converts from a list of list of json species to a list of list of species
	:pram lolos: [LOS_j, ...]
	:return: [[Species], ...]
	"""
	lolos = []
	for los_json in lolos_json:
		lolos.append(parse_los(los_json))
	return lolos


def parse_lot(lot_json):
	lot = []
	for t in lot_json:
		lot.append(Trait(t))
	return lot

def parse_feeding(feeding):
	"""
	convert a feeding to an input feeding
	:param feeding: Feeding_j
	:return: [Player, int, [Player, ...]]
	"""
	try:
		[player_json, watering_hole, lop_json] = feeding
		return [parse_player(player_json), watering_hole, parse_lop(lop_json)]
	except ValueError:
		raise ValueError("invalid feeding")

def parse_situation(situation):
	"""
	convert a situation to an input situation
	:param situation: Situation_j
	:return: [Species, Species, (False or Species), (False or Species)]
	"""
	try:
		[defender, attacker, left, right] = situation
		defender_s = parse_species(defender)
		attacker_s = parse_species(attacker)
		left_s = parse_species(left) if left else False
		right_s = parse_species(right) if right else False
		return [defender_s, attacker_s, left_s, right_s]
	except:
		raise ValueError("invalid situation")

def parse_configuration(configuration):
	"""
	converts a configuration to an input configuration
	:param configuration: Configuration
	:return: [[Player, ...], int, [TraitCard, ...]]
	"""
	try:
		[lop, wh, loc] = configuration
		watering_hole = WateringHole(wh)
		return [parse_lop(lop), watering_hole, parse_loc(loc)]
	except ValueError:
		raise ValueError("invalid configuration")

def parse_step4(step4):
	"""
	converts step4 to an input step4
	:param step4: Step4
	:return: [[int, ...], [PlayerAction], [[BT, ...], ...]]
	"""
	card_indexes = []
	player_actions = []
	bt_actions = []
	for action in step4:
		[card_index, list_gp, list_gb, list_bt, list_rt] = action
		card_indexes.append(card_index)
		player_actions.append([list_gp, list_gb, list_rt])
		bt_actions.append(list_bt)


	return [card_indexes, player_actions, bt_actions]

def parse_configuration_with_xstep4(xstepconf):
	"""
	converts the given configuration and xstep4 into the respective configuration
	:param xstepconf: [Configuration, Step4]
	:return: [[[Player, ...], int, [TraitCard, ...]], [[int, ...], [PlayerAction]]]
	"""
	config = parse_configuration(xstepconf[0])
	s4 = parse_step4(xstepconf[1])
	return [config, s4]

def parse_choice(choi):
	"""
	converts the given choice into a configuration
	:param choi: [Player+, LOS, LOS]
	:return: [Player, LOLOS, LOLOS]
	"""
	play, los1, los2 = choi
	parsed_play = parse_playerEx(play)
	parsed_lolos1 = parse_lolos(los1)
	parsed_lolos2 = parse_lolos(los2)

	return [parsed_play, parsed_lolos1, parsed_lolos2]

def parse_s(t):
	"""
	converts the given t into a python list
	:param t: [int, [Species_j+, ...], [SpeciesCard, ...]]
	:return: [int, [Species, ...], [TraitCard, ...]]
	"""
	return [t[0], t[1], parse_los(t[2]), parse_loc(t[3])]

def parse_cdj(cdj):
	"""
	converts the given cdj into a python list
	:param cdj: [[[Species_j+, ...], ...], [[Species_j+, ...], ...]]
	:return: [[[Species, ...], ...], [[Species, ...], ...]]
	"""
	return [parse_lolos(cdj[0]), parse_lolos(cdj[1])]


def parse_state(state):
	"""
	converts the given t into a python list
	:param state: [int, [Species_j+, ...], [SpeciesCard, ...], int, [[Species_j, ...], ...]]
	:return: [int, [Species, ...], [TraitCard, ...], int, [[Species, ...], ...]]
	"""
	return [state[3], parse_lolos(state[4]), [state[0], parse_los(state[1]), parse_loc(state[2])]]













