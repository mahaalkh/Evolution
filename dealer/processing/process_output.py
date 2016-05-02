# handles JSON parsing for the game Evolution
import sys, os, json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from trait import Trait
from species import Species
from inPlayer import Player
from dealer import Dealer


#  Feeding_j = [Player, Natural+, LOP]
#  Player_j = [["id",Natural+], ["species",LOS], ["bag",Natural]]
# LOP_j = [Player, ..., Player]
# LOS_j = [Species+, ..., Species+]
# Species+_j = [["food",Nat], ["body",Nat], ["population",Nat], ["traits",LOT], ["fat-food" ,Nat]]
# Species_j = [["food",Nat], ["body",Nat], ["population",Nat], ["traits",LOT]]
# Species+ = Species_j or Species+_j
# Situation_j = [Species+, Species+, OptSpecies, OptSpecies]
# OptSpecies = Species+ or False
# Configuration = [LOP+, Natural, LOC]
# LOP+ = A LOP+ is [Player+, ..., Player+].
# A Player+ is one of a regular Player_j or Player+_j
# A Player+_j =   [["id",Natural+], ["species",LOS], ["bag",Natural], ["cards",LOC]]
# LOC = [SpeciesCard, ..., SpeciesCard]
# SpeciesCard = [FoodValue, Trait]
# Species+ with a 0-valued "fat-food" field renders as a plain Species;
# FoodValue is a JSON number interpretable as an integer between -8 and 8 (inclusive).
# Player+ with a []-valued "cards" field renders as a plain Player



def make_trait_card(trait_card):
	"""
	converts from a TraitCard to a json card
	:param trait_card: TraitCard
	:return: SpeciesCard
	"""
	food_point = trait_card.getFoodPoints()
	trait = trait_card.getTrait()
	trait_s = trait.value
	return [food_point, trait_s]

def make_loc_json(loc):
	"""
	converts from a list of TraitCards to a list of SpeciesCards
	:param loc: [TraitCard, ...]
	:return: [SpeciesCard, ...]
	"""
	loc_json = []
	if loc:
		for card in loc:
			loc_json.append(make_trait_card(card))
	return loc_json

def make_player_json(player):
	"""
	converts the representation of a player into a json player representation
	:param player_json: Player
	:return: Player+
	"""
	player_id = player.getPlayerId()
	player_los = player.getSpeciesBoards()
	player_bag = player.getFoodBag()
	player_cards = player.getHand()
	if player_cards:
		return [["id", player_id],
		        ["species", make_los_json(player_los)],
		        ["bag", player_bag],
		        ["cards", make_loc_json(player_cards)]]
	else:
		return [["id", player_id],
		        ["species", make_los_json(player_los)],
		        ["bag", player_bag]]

def make_lop_json(lop):
	"""
	converts from a list of players to a list of json players
	:param lop: [Player, ...]
	:return: LOP+
	"""
	lop_json = []
	for player in lop:
		lop_json.append(make_player_json(player))
	return lop_json

def make_species_json(species):
	"""
	converts from a  representation of species to a json species representation
	:param species: Species
	:return: Species+
	"""
	food = species.getFood()
	body = species.getBodySize()
	population = species.getPopulation()
	traits = species.getTraits()
	fat_food = species.getFatFood()

	if fat_food == 0:
		return [["food", food],
		        ["body", body],
		        ["population", population],
		        ["traits", make_lot_json(traits)]]
	else:
		return  [["food", food],
		         ["body", body],
		         ["population", population],
		         ["traits", make_lot_json(traits)],
		         ["fat-food", fat_food]]

def make_los_json(los):
	"""
	convert from a list of species to a list of json species
	:param los_json:  [Species, ...]
	:return: LOS_j
	"""
	los_json = []
	for species in los:
		los_json.append(make_species_json(species))
	return los_json

def make_lolos_json(lolos):
	"""
	makes an lolos json from the lolos
	:param lolos: [[Species, ...], ...]
	:return: [[LOS_j, ...], ...]
	"""
	lolos_json = []
	for los in lolos:
		lolos_json.append(make_los_json(los))
	return lolos_json

def make_lot_json(lot):
	lot_json = []
	for trait in lot:
		lot_json.append(trait.value)
	return lot_json

def make_choice(player, lolos1, lolos2):
	"""
	constucts a make_choice
	:param player: Player
	:param lolos1: [[Species, ...], ...]
	:param lolos2: [[Species, ...], ...]
	:return: [player+_json, lolos_json, lolos_json]
	"""
	choice =  [make_player_json(player), make_lolos_json(lolos1), make_lolos_json(lolos2)]
	return choice

def make_state(state):
	"""
	constructs a state json
	:param state: [int, [Species, ...], [TraitCard, ...], int, [[Species, ...], ...]]
	:return: [int, [Species_j+, ...], [SpeciesCard, ...], int, [[Species_j, ...], ...]]
	"""
	return [state[0], make_los_json(state[1]), make_loc_json(state[2]), state[3], make_lolos_json(state[4])]

def make_t_json(t):
	"""
	constructs a t json
	:param t: [int, int, [Species, ...], [TraitCard, ...]]
	:return: [int, int, [Species_j+, ...], [SpeciesCard, ...]]
	"""
	print "T is" + str(t) 
	return [t[0], t[1], make_los_json(t[2]), make_loc_json(t[3])]

def make_cd_json(c, d):
	"""
	constructs a cdj json
	:param cdj: [[[Species, ...], ...], [[Species, ...], ...]]
	:return: [[[Species_j+, ...], ...], [[Species_j+, ...], ...]]
	"""
	return [make_lolos_json(c), make_lolos_json(d)]








