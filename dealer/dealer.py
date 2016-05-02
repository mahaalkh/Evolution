# The Dealer object in a game of Evolution
import trait
import species
import trait_card
from utils import compileSpecies
from validate import validateDeck, validateListOfPlayers, validatePlayerSpecies
from copy import deepcopy

FOOD_PER_TURN = 1
FEED_SCAVENGING = FOOD_PER_TURN
FEED_COOPERATION = FOOD_PER_TURN
FERTILE_INCREASE = 1
LONGNECK_FOOD = 1
BEFORE = True

class Dealer:
	deck = []
	listOfPlayers = []
	isFed = []

	def __init__(self, wateringHole, listOfPlayers, deck=None):
		"""
		Initializes a Dealer with a watering hole, list of players and an optional deck
		:param wateringHole: WateringHole
		:param listOfPlayers: list of Player with a length between 3 and 8 inclusive
		:param deck: None or list of TraitCard with a length between 0 and 122 inclusive
		"""
		self.wateringHole = wateringHole
		if validateListOfPlayers(listOfPlayers):
			self.listOfPlayers = listOfPlayers
		if deck != None:
			if validateDeck(deck):
				self.deck = deck
		else:
			self.deck = []
		## isFed is a [Player,]
		self.isFed = []
		## indexPlayerToBeFed is the index of the player whose turn it is
		self.indexPlayerToBeFed = 0

	def setWateringHole(self, numFoodTokens):
		"""
		sets the wateringHole of this dealer to numFoodTokens
		:param numFoodTokens: int
		:effect: modifies the value of the watering hole for this dealer 
		"""
		self.wateringHole.setAmount(numFoodTokens)

	def getWateringHole(self):
		"""
		returns the value of the watering hole of this dealer
		:return: int
		"""
		return self.wateringHole.getAmount()

	def setListOfPlayers(self, players):
		"""
		sets the listOfPlayers field to the given list of players
		:param players: [Player, ...]
		:effect: modifies the list of player of this dealer 
		"""
		if validateListOfPlayers(players):
			self.listOfPlayers = players

	def getListOfPlayers(self):
		"""
		returns the list of players of this dealer
		:return: [Player, ...]
		"""
		return self.listOfPlayers

	def setDeck(self, deck):
		"""
		sets the deck of this dealer to deck
		:param deck: [TraitCard, ...]
		"""
		if validateDeck(deck):
			self.deck = deck

	def getDeck(self):
		"""
		returns the deck of this dealer
		:return: [TraitCard, ...]
		"""
		return self.deck

	def addToWateringHole(self, card_indexes):
		"""
		adds the cards to the watering hole
		:param card_indexes: [int, ...] where the index of the int is the index of the player
		 and the int is the index of the card in the player
		:return: [TraitCard, ...]
		:effect: sets the placed cards of the watering hole to the aquired cards 
		"""

		list_cards = self.acquireCards(card_indexes)
		self.wateringHole.setPlacedCards(list_cards)
		return list_cards

	def removeCardsFromDeck(self, loc):
		"""
		removes a the cards from this dealer's deck
		:param loc: [TraitCard, ...]
		:effect: removes cards from this dealer's deck
		"""
		for card in loc:
			self.deck.remove(card)

	def getCardsFromDeck(self, loi):
		"""
		returns the cards in this dealer's deck by index
		:param loi: [int, ...]
		:return: [TraitCard, ...]
		"""
		cards = []
		for i in loi:
			if i not in range(len(self.getDeck())):
				pass
			card = self.deck[i]
			cards.append(card)
		return cards

	def get_configuration(self):
		"""
		gets the configuration of the dealer
		:return: [[Player, ...], int, [TraitCard, ...]]
		"""
		result =  [self.getListOfPlayers(), self.getWateringHole(), self.getDeck()]
		return result

	def getLOS(self, p, before):
		"""
		gets the list of list of species of the players before or after the given player
		:param p: Player
		:param before: Boolean
		:return: [[Species, ...], ...]
		"""
		losBefore = []
		losAfter = []
		afterPlayer = False
		for pl in self.listOfPlayers:
			if p == pl:
				afterPlayer = True
			elif afterPlayer:
				losAfter.append(pl.getSpeciesBoards())
			else:
				losBefore.append(pl.getSpeciesBoards())

		if before:
			return losBefore
		else:
			return losAfter



	def resetIndexPlayerToBeFed(self): 
		"""
		keeps the index of the player to be fed to be in the range of the length of players\
		"""
		self.indexPlayerToBeFed = self.indexPlayerToBeFed % len(self.getListOfPlayers())




	def add1IPlayerToFeed(self):
		"""
		increments the index of the player currently being fed
		effect: changes the indexPlayerToBeFed
		"""
		self.indexPlayerToBeFed = (self.indexPlayerToBeFed + 1) % len(self.getListOfPlayers())

	def addPlayerToFed(self, player):
		"""
		adds given player to the isfed list
		:param player: Player
		:effect: modifies the isFed list in this dealer 
		"""
		if player not in self.isFed:
			self.isFed.append(player)

	def giveCardsToPlayer(self, player):
		"""
		gives two cards to the player from the deck
		:param player: Player
		:effect: modifies the deck of this dealer
		 (reduces the length of the deck)
		"""
		if len(self.getDeck()) >= 2:
			cards = self.getCardsFromDeck([0, 1])
			player.addToHand(cards)
			self.removeCardsFromDeck(cards)
		else:
		        return self.scores()

	def acquireCards(self, card_indexes):
		"""
		gets the cards from the player
		:param card_indexes: [int, ...] where the index of the int is the index of the player
		 and the int is the index of the card in the player
		:return: [TraitCard, ...]
		"""
		i = 0
		cards = []
		for card_index in card_indexes:
			player = self.getListOfPlayers()[i]
			card = player.giveCard(card_index)
			cards.append(card)
			i += 1
		return cards

	def askPlayerToDiscard(self, lol_cards_to_discard):
		"""
		asks the player to remove all the cards based on the given card card_indexes
		:param lol_cards_to_discard:  [[TraitCard, ...], ...]
		:effect: the players' hands is modified (cards are removed from it)
		"""
		i = 0
		for cards in lol_cards_to_discard:
			player = self.getListOfPlayers()[i]
			player.removeCardsFromHand(cards)
			i += 1

	def askPlayerToDiscardACard(self, cards_to_discard):
		"""
		asks the player to remove the card
		:param cards_to_discard:  [TraitCard, ...]
		:effect: the players' hands is modified (a card is removed from it)
		"""
		i = 0
		for card in cards_to_discard:
			player = self.getListOfPlayers()[i]
			player.removeCardsFromHand([card])
			i += 1


	def feed_a_species(self, species, amount, is_fat):
		"""
		feeds the given species the amount of tokens indicated
		:param species: Species
		:param amount: int
		:param is_fat: boolean which indicates if it is a fat food feeding
		:effect: the species fatFood is increased by amount given if is_fat otherwise, 
		the species food is increased by the amount given 
     	"""
		amount = min(amount, species.maximumFeed(is_fat))
		if is_fat:
			species.addToFatFood(amount)
		else:
			species.addToFood(amount)
		self.setWateringHole(self.getWateringHole() - amount)

	def feeding(self, player, i, amount, is_fat):
		"""
		feeds the species in the player
		:param player: Player
		:param i: int which is the index of the player to feed
		:param amount: number of food tokens to give the species from the watering hole
		:param is_fat: boolean which indicates if this is a fat_food feeding
		"""
		species = player.getSpeciesByIndex(i)
		is_hungry = species.isHungryForFat() if is_fat else species.isHungryForFood()
		if is_hungry:
		    amount = min(self.getWateringHole(), amount)
		    self.feed_a_species(species, amount, is_fat)

 	def feedingWithTraits(self, player, i, amount):
 		"""
 		feed the player's species
 		:param player: Player
 		:param i: int which is the index of the species to feed
 		:param amount: int which is the amount of tokens to feed the species
 		:effect: the amount of food of the given player's species (based on the index given)
 		         is increased by the given amount and the effects of
 		         feed_foraging and feed_coorperation take place if applicable
 		"""
 		self.feeding(player, i, amount, False)
		self.feed_foraging(player, i)
		self.feed_cooperation(player, i)

	def compileSpeciesWithTrait(self, t):
		"""
		gets all the indeces of species with the given trait
		:param t: Trait
		:return: [(Player, i), ...] where i is the index of the species in the player
		"""
		allSpecies = compileSpecies(self.getListOfPlayers())
		speciesWithTrait = []
		for i in range(len(allSpecies)):
			for j in range(len(allSpecies[i])):
				player = self.getListOfPlayers()[i]
				species = player.getSpeciesByIndex(j)
				if species.hasTrait(t):
					speciesWithTrait.append((player, j))
		return speciesWithTrait

	def applyAction(self, t, amount, funct):
		"""
		applies the function (funct) on the species with the given trait t
		:param t: Trait
		:param amount: int
		:param funct: function that takes in three parameters (Player, int, int)
		"""
		speciesWithTrait = self.compileSpeciesWithTrait(t)
		for pair in speciesWithTrait:
			player, speciesIndex = pair
			funct(player, speciesIndex, amount)

	def applyIncreasePopulation(self, t, amount):
		"""
		increases the population of the species with the given trait t by the given amount
		:param t: Trait
		:param amount: int
		:effect: increases the population of the species with the given trait 
			t by the given amount
		"""
		speciesWithTrait = self.compileSpeciesWithTrait(t)
		for pair in speciesWithTrait:
			player, speciesIndex = pair
			player.increaseSpeciesPopulation(speciesIndex, amount)

	def applyPlayerActions(self, players_actions):
		"""
		applies all the actions by the player
		:param players_actions: [PlayerAction, ...]
		:return: [[TraitCard, ...], ...]
		"""
		i = 0
		lol_cards_to_discard = []
		for players_action in players_actions:
			player = self.getListOfPlayers()[i]
			cards_to_discard = player.apply_action(players_action)
			i += 1
			lol_cards_to_discard.append(cards_to_discard)

		return lol_cards_to_discard

	def applyBT(self, player, bt):
		"""
		adds a species with population 1 to the player
		:param player: Player
		:param bt: BT
		:effect: adds a species to the player 
		"""
		spec = species.Species(0, 0, 1, [])
		cards = player.addSpecies(spec, bt)
		return cards

	def applyBTList(self, player, bt_list):
		"""
		add species to the player that requested
		a species based on the bt_list
		:param player: Player
		:param bt_list: [BT, ...]
		:return: [TraitCard, ...]
		"""
		cards_to_discard = []
		if len(bt_list) >= 1:
			cards_to_discard = self.applyBT(player, bt_list[0])
			for bt in bt_list[1:]:
				 cards = self.applyBT(player, bt)
				 cards_to_discard.extend(cards)
		return cards_to_discard

	def applyBTActions(self, bt_actions):
		"""
		adds the species as indicated by the bt_actions
		:param bt_actions: [[BT, ...], ...]
		"""
		i = 0
		lol_cards_to_discard = []
		for bt_list in bt_actions:
			player = self.getListOfPlayers()[i]
			cards = self.applyBTList(player, bt_list)
			lol_cards_to_discard.append(cards)
			i += 1
		return lol_cards_to_discard

	def getActions(self):
		"""
		gets the actions from the player and then returns the list of indexes of 
		 cards the players will use 
		:return: [[int, ...],
				  [[GP, GB , RT], ....], 
				  [BT, ...]]
		"""

		card_indexes = []
		players_actions = []
		bt_actions = []

		for p in self.getListOfPlayers():
			chosen = p.choose([self.getLOS(p, BEFORE), self.getLOS(p, not BEFORE)])
			if chosen == "delete":
				self.getListOfPlayers().remove(p)
				self.resetIndexPlayerToBeFed()
				if self.getListOfPlayers() == []:
					self.scores()
			else:
				whCard, gpList, gbList, btList, rtList = chosen
				card_indexes.append(whCard)
				players_actions.append([gpList, gbList, rtList])
				bt_actions.append(btList)

		return [card_indexes, players_actions, bt_actions]


	def step2And3(self):
		"""
		executes all the actions based on the players decisions
		:effect: asks the player to modify its hand 
		"""
		card_indexes, players_actions, bt_actions = self.getActions()

		cards1 = self.addToWateringHole(card_indexes)
		lolcards3 = self.applyBTActions(bt_actions)
		lolcards2 = self.applyPlayerActions(players_actions)
		self.askPlayerToDiscardACard(cards1)
		self.askPlayerToDiscard(lolcards2)
		self.askPlayerToDiscard(lolcards3)

	def askPlayersToMoveFat(self):
		"""
		tells the player to move the fat-store to the food for its fat_tissue species
		:effect: players's species fatFood is added to the species food
		"""
		for p in self.getListOfPlayers():
			p.moveFatToFood()


	def feed_foraging(self, player, i):
		"""
		allows the foraging species eat another time
		:param player: Player
		:param i: int which is the index of the species to be fed
		:effect: the species at index i in the player is fed if it has the trait foraging 
		"""
		if (player.getSpeciesByIndex(i).hasTrait(trait.Trait.foraging)) and (player.getSpeciesByIndex(i).isHungryForFood()):
			self.feeding(player, i, FOOD_PER_TURN, False)
			self.feed_cooperation(player, i)

	def feed_cooperation(self, player, iSpecies):
		"""
		feed the right neighbor of the cooperating species
		:param player: Player
		:param iSpecies: int which is the index of the species which is cooperating
		:effect: if the player's species at index iSpecies has coorperation, 
				then the right neighbor of that species is fed  
		"""
		species = player.getSpeciesByIndex(iSpecies)
		if species.hasTrait(trait.Trait.cooperation):
			if((len(player.getSpeciesBoards())-1) > iSpecies):
				nextSpecies = player.getSpeciesByIndex(iSpecies+1)
				if nextSpecies.isHungryForFood():
					self.feedingWithTraits(player, iSpecies+1, FEED_COOPERATION)

	def attack(self, player, speciesIndex):
		"""
		reduces the population of the species or makes it extinct
		:param player: Player
		:param speciesIndex: int which is the index of the species in the player's species
		:return: boolean which indicates if the species did not go extinct
		:effect: population of the species at the species index is reduced
				if population goes to 0 then the species is removed from the player's list of species 
				and the player is given 2 cards in return 
		"""

		if player.reduceSpeciesPopulation(speciesIndex, FOOD_PER_TURN):
				return True
		else:
				player.removeSpeciesInLOS(speciesIndex)
				self.giveCardsToPlayer(player)
				return False

	def feeding_carnivore(self, player, result):
		"""
		feeds the species in this player and reduces the population of the victim
		:param player: Player
		:param result: [nat, nat, nat] where the first is the
		 attacking species board index, the second is
		the defending player index, and the third is the defending species board index.
		"""

		rest_of_players = self.getListOfPlayers()[:self.indexPlayerToBeFed]
		rest_of_players.extend(self.getListOfPlayers()[self.indexPlayerToBeFed+1:])
		defendingPlayer = rest_of_players[result[1]]

		defendingSpeciesIndex = result[2]
		attackingSpeciesIndex = result[0]
		defendingSpecies = defendingPlayer.getSpeciesByIndex(defendingSpeciesIndex)

		attacked = self.attack(defendingPlayer, defendingSpeciesIndex)
		defended = True
		if defendingSpecies.hasTrait(trait.Trait.horns):
			defended = self.attack(player, attackingSpeciesIndex)
		if defended:
			self.feedingWithTraits(player, attackingSpeciesIndex, FOOD_PER_TURN)
		self.applyAction(trait.Trait.scavenger, FEED_SCAVENGING, self.feedingWithTraits)

	def autoFeed(self):
		"""
		automatically feeds the first player's species if possible
		:return: boolean which indicates if the player's species was automatically fed
		"""
		player = self.getListOfPlayers()[self.indexPlayerToBeFed]
		hungry_species_indexes =  player.getHungrySpeciesIndexes()
		if len(hungry_species_indexes) == 0:
			self.addPlayerToFed(player)
			return True

		if len(hungry_species_indexes) == 1:
			hungry_animal_index = hungry_species_indexes[0]
			hungry_animal = player.getSpeciesByIndex(hungry_animal_index)
			if hungry_animal.hasTrait(trait.Trait.carnivore) or hungry_animal.hasTrait(trait.Trait.fat_tissue):
				return False
			else:
				self.feedingWithTraits(player, hungry_animal_index, FOOD_PER_TURN)
				return True
		return False

	def willFeed(self):
		"""
		Checks if the first hungry species will feed and how based on the players strategy
		:return: a tuple of carnivore, fat_tissue or False, and a feeding output or False or "endGame"
		"""
		player = self.getListOfPlayers()[self.indexPlayerToBeFed]
		lolos = self.getLOS(player, BEFORE)
		lolos.extend(self.getLOS(player, not BEFORE))

		feeding = player.feedNext(self.getWateringHole(), lolos)

		if (not feeding) or (isinstance(feeding, int)):
			return (False, feeding)
		elif len(feeding) == 2:
			return (trait.Trait.fat_tissue, feeding)
		elif len(feeding) == 3:
			return (trait.Trait.carnivore, feeding)
		else:
			self.getListOfPlayers().remove(player)
			self.resetIndexPlayerToBeFed()
			if self.getListOfPlayers() == []:
				return "endGame"

	def processFeed(self, feeding_result):
		"""
		Feeds the appropriate species based on the feeding result if possible
		:param feeding_result: output of the Feed method
		:param i: the index of the player whose turn it is
		"""
		t, result = feeding_result
		player = self.getListOfPlayers()[self.indexPlayerToBeFed]

		if not t:
			self.feedingWithTraits(player, result, FOOD_PER_TURN)
		elif (t is trait.Trait.fat_tissue):
			self.feeding(player, result[0], result[1], True)
		elif (t is trait.Trait.carnivore):
			self.feeding_carnivore(player, result)
		else:
			self.getListOfPlayers().remove(player)
			self.resetIndexPlayerToBeFed()
			if self.getListOfPlayers() == []:
				return self.scores()

	def feed1(self):
		"""
		executes one step in the feeding cycle which includes:
		 - deciding whether it can transfer a food token from the watering hole to
		 the current player automatically or whether it is necessary to query the next player
		 - transfering food, by interpreting the answers from the player
		 - remove the player from sequence or rotate the sequence of players, as needed
		 :return: [[Player, ...], int, [TraitCard, ...]]
		 :effect: modifies the  isFed list in this dealer and  the indexPlayerToB 
		 """

		auto = self.autoFeed()

		if not auto:
			feeding_result = self.willFeed()
			if feeding_result == "endGame" or not feeding_result: 
				return self.scores()
			elif feeding_result[0] or (str(feeding_result[1]) != "False"):
				self.processFeed(feeding_result)
			else:
				self.addPlayerToFed(self.getListOfPlayers()[self.indexPlayerToBeFed])
		self.add1IPlayerToFeed()

	def executeFeed1AndReturn(self):
		"""
		executes feed1 and returns a result for the sake of testing
		:return: [[Player, ...], int, [TraitCard, ...]]
		"""
		self.feed1()
		result =  [self.getListOfPlayers(), self.getWateringHole(), self.getDeck()]
		return result


	def preFeed(self):
		"""
		applies the auto feeding
		:effect: species with fertile trait get their population increased by 1
				species with the longneck trait get fed a food token 
				all the species that have fattissue increment their food by the 
				amount of fatfood they have and the fatfood is decremented 
				 the amount added to the food 
		"""
		self.applyIncreasePopulation(trait.Trait.fertile, FERTILE_INCREASE)
		self.applyAction(trait.Trait.long_neck, LONGNECK_FOOD, self.feedingWithTraits)
		self.askPlayersToMoveFat()

	def feedLoop(self):
		"""
		feeds all the players' species
		"""
		self.preFeed()

		while len(self.isFed) != len(self.getListOfPlayers()) and (self.getWateringHole() != 0):
			if self.getListOfPlayers()[self.indexPlayerToBeFed] in self.isFed:
				self.add1IPlayerToFeed()
			self.feed1()

	def step4(self):
		"""
		runs the feeding loop and fills the watering hole for the fourth step of the evolution game
		:param step4_array: [[int, ...], [PlayerAction, ...], [[BT, ...], ...]]
		:effect: the value of the watering hole is incremented by the amount of
		 food points on the cards on the watering hole
		  		the list of cards placed on the watering hole is emptied
		"""
		self.wateringHole.turnOverCards()
		self.feedLoop()

	def dealer_strings(self):
		"""
		extract all the fields of this dealer as strings
		:return: [String, [String, ...], [String, ...]]
		"""
		wh = self.getWateringHole()
		lop = self.getListOfPlayers()
		loc = self.getDeck()

		wh_str = str(wh)
		lop_strings = []
		for player in lop:
			lop_strings.append(player.player_strings())
		loc_strings = []
		for card in loc:
			loc_strings.append(card.display_card())

		return [wh_str, lop_strings, loc_strings]

	def canDeal(self):
		"""
		Checks if there are enough cards in the deck to deal to the players
		:return: boolean
		"""
		amountNeeded = 0
		for p in self.getListOfPlayers():
			amountNeeded += 3
			if len(p.getSpeciesBoards()) == 0:
				amountNeeded += 1
			amountNeeded += len(p.getSpeciesBoards())

		return amountNeeded <= len(self.deck)

	def dealSpeciesBoards(self, p):
		"""
		returns a new species board if the given player has no species
		:param p: a player
		:return: Species or False
		"""
		if len(p.getSpeciesBoards()) == 0:
			return species.Species(0, 0, 1, [])
		return False

	def dealCards(self, p):
		"""
		returns a list of cards to be given to the given player
		:param p: a player or endGame
		:return: [TraitCard, ...]
		:effect: the deck in this dealer is modified 
		"""
		loc = self.deck[:4]
		self.deck = self.deck[4:]
		for each in p.getSpeciesBoards():
			try:
				loc.append(self.deck.pop())
			except IndexError:
				return "endGame"
		return loc

	def step1(self):
		"""
		Passes out the cards/species boards at the beginning of a turn
		"""
		for p in self.getListOfPlayers():
			b = self.dealSpeciesBoards(p)
			c = self.dealCards(p)
			if c == "endGame": 
				return self.scores()
			p.start(self.getWateringHole(), b, c)

	def reducePopulations(self):
		"""
		makes the populations of the species of the
		players equal to the amount of food the species has
		"""
		for p in self.getListOfPlayers():
			numDeleted = p.starveSpecies()
			for i in range(numDeleted):
				self.giveCardsToPlayer(p)

	def moveFoodToBag(self):
		"""
		moves the food from the players' species to the player's food bag
		"""
		for p in self.getListOfPlayers():
			p.moveFoodToBag()


	def endTurn(self):
		"""
		Wraps up turn for all players
		:effect: the populations of the species of the players is reduced to
		 the amount of food it has 
		 the food in the species is added to the food bag of the players 
		"""
		self.reducePopulations()
		self.moveFoodToBag()

	def turn(self):
		"""
		Runs a complete turn round
		"""
		self.step1()
		self.step2And3()
		self.step4()
		self.endTurn()

	def scores(self):
		"""
		returns the player results in a list form
		A PlayerResult is a string following the template
		 "x player id: y name: s score: z"  (Score) where x, y and z are ints and s is a string
		:return: [PlayerResult, ...]
		"""
		scores = []
		for p in self.getListOfPlayers():
			scores.append((p, p.calculateScore()))

		sorted_scores = sorted(scores, cmp = lambda x, y: cmp(x[1], y[1]), reverse = True)

		resultTemplate = "{} player id: {} name: {} score: {}"
		i = 1
		playerResult = []
		for p, score in sorted_scores:
			playerResult.append(resultTemplate.format(i, p.getPlayerId(), p.getInfo(), score))
			i += 1

		return playerResult

	def applyStep3(self, step4_array):
		"""
		FOR TESTS ONLY
		executes all the actions in the given step4_array
		:param step4_array: [[int, ...], [PlayerAction, ...], [[BT, ...], ...]]
		"""
		card_indexes, players_actions, bt_actions = step4_array

		cards1 = self.addToWateringHole(card_indexes)
		lolcards3 = self.applyBTActions(bt_actions)
		lolcards2 = self.applyPlayerActions(players_actions)
		self.askPlayerToDiscardACard(cards1)
		self.askPlayerToDiscard(lolcards2)
		self.askPlayerToDiscard(lolcards3)

	def step4Apply(self, step4_array):
		"""
		FOR TESTS ONLY
		runs the feeding loop and fills the watering hole for the fourth step of the evolution game
		NOTE: apply_step3 will later be moved to a run game method when that method is written
		:param step4_array: [[int, ...], [PlayerAction, ...], [[BT, ...], ...]]
		"""
		self.applyStep3(step4_array)
		self.wateringHole.turnOverCards()
		self.feedLoop()

	def runGame(self):
		"""
		runs the game & returns the scoreboard in list form
		:return: [PlayerResult, ...]
		"""
		while (self.canDeal() and self.getListOfPlayers()):
			self.turn()
		return self.scores()
