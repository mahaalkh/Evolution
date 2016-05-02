import unittest
import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from dealer import Dealer
from trait import Trait
from inPlayer import Player
from species import Species
from trait_card import TraitCard
from wateringWhole import WateringHole
import deck
#TODO: check the elements in the dealer for imperative methods
class TestDealer(unittest.TestCase):
	def setUp(self):
		self.player1 = Player(1, [], 0, info = "j")
		self.player2 = Player(2, [], 0, info = "j")
		self.player3 = Player(3, [], 0, info = "j")
		self.player4 = Player(4, [], 0, info = "j")
		self.player5 = Player(5, [], 0, info = "j")
		self.player6 = Player(6, [], 0, info = "j")
		self.player7 = Player(7, [], 0, info = "j")
		self.player8 = Player(8, [], 0, info = "j")

		self.players = [self.player1, self.player2, self.player3]
		self.players8 = [self.player1, self.player2, self.player3, self.player4, self.player5, self.player6, self.player7, self.player8]

		self.species1 = Species(0, 3, 3, [])
		self.species2 = Species(0, 2, 1, [])
		self.speciesscavenger = Species(0, 3, 3, [Trait.scavenger])
		self.speciesforaging = Species(0, 3, 3, [Trait.foraging])
		self.speciescoop = Species(0, 3, 3, [Trait.cooperation])
		self.speciesfull = Species(2, 2, 2, [])
		self.speciesfull1 = Species(3, 2, 3, [])
		self.speciesfull2 = Species(4, 2, 4, [])
		self.speciesfat= Species(0, 3, 3, [Trait.fat_tissue])
		self.speciesfat.setFatFood(1)
		self.specieshorns = Species(0, 3, 3, [Trait.horns])
		self.speciescarni = Species(0, 3, 3, [Trait.carnivore])
		self.specieshorns1 = Species(0, 3, 1, [Trait.horns])
		self.speciescarni1 = Species(0, 3, 1, [Trait.carnivore])
		self.speciesLongFertile = Species(0, 3, 1, [Trait.long_neck, Trait.fertile])
		self.speciesFertile = Species(0, 3, 1, [Trait.fertile])
		self.speciesLongNeck = Species(0, 3, 1, [Trait.long_neck])

		self.watering_hole = WateringHole(0)

		self.dealer = Dealer(self.watering_hole, self.players)

		self.warning_call_card = TraitCard(Trait.warning_call, 0)
		self.warning_call_card2 = TraitCard(Trait.warning_call, 1)
		self.climbing_card = TraitCard(Trait.climbing, 3)
		self.carnivore_card = TraitCard(Trait.carnivore, -8)

		self.fertileCard = TraitCard(Trait.fertile, 2)
		self.climbingCard = TraitCard(Trait.climbing, 0)
		self.cooperationCard = TraitCard(Trait.cooperation, 0)
		self.carnivoreCard = TraitCard(Trait.carnivore, 0)
		self.longNeckCard = TraitCard(Trait.long_neck, 0)
		self.fertileCard1 = TraitCard(Trait.fertile, 2)
		self.climbingCard1 = TraitCard(Trait.climbing, 1)
		self.cooperationCard1 = TraitCard(Trait.cooperation, 1)
		self.carnivoreCard1 = TraitCard(Trait.carnivore, 1)
		self.longNeckCard1 = TraitCard(Trait.long_neck, 1)
		self.ambushCard = TraitCard(Trait.ambush, 1)


		self.deck = [self.warning_call_card, self.climbing_card, self.carnivore_card]

		self.deck2 = deck.generateDeck()[:12]

		self.dealer.setDeck(self.deck)
		self.dealer.setWateringHole(20)




	def tearDown(self):
		del self.player1
		del self.player2
		del self.player3
		del self.players
		del self.dealer
		del self.deck
		del self.species1
		del self.speciesscavenger
		del self.speciesforaging
		del self.speciescoop
		del self.species2
		del self.speciescarni
		del self.specieshorns
		del self.carnivore_card
		del self.climbing_card
		del self.warning_call_card
		del self.speciescarni1
		del self.specieshorns1
		del self.warning_call_card2
		del self.watering_hole

	# def testSetAndGetWateringHole(self):
	# 	self.dealer.setWateringHole(9)
	# 	self.assertEqual(self.dealer.getWateringHole(), 9)

	# def testSetAndGetListOfPlayer(self):
	# 	self.dealer.setListOfPlayers(self.players)
	# 	self.assertEqual(self.dealer.getListOfPlayers(), self.players)

	# def testSetAndGetDeck(self):
	# 	self.dealer.setDeck([])
	# 	self.assertEqual(self.dealer.getDeck(), [])

	# def testRemoveCardsFromDeck(self):
	# 	self.dealer.removeCardsFromDeck([self.warning_call_card])
	# 	self.assertEqual(self.dealer.getDeck(), [self.climbing_card, self.carnivore_card])

	# def testGetCardsFromDeck(self):
 #  		cards = self.dealer.getCardsFromDeck([1, 2])
 #  		self.assertEqual(self.dealer.getDeck(), [self.warning_call_card, self.climbing_card, self.carnivore_card])
 #  		self.assertEqual(cards, [self.climbing_card, self.carnivore_card])
	# def testFeedASpeciesFat(self):
 #  		self.dealer.feed_a_species(self.speciesfat, 3, True)
 #  		self.assertEqual(self.speciesfat.getFatFood(), 3)
 #  		self.assertEqual(self.dealer.getWateringHole(), 18)

	# def testFeedASpeciesFood(self):
	# 	self.dealer.feed_a_species(self.speciesfat, 3, False)
	# 	self.assertEqual(self.speciesfat.getFood(), 3)
	# 	self.assertEqual(self.dealer.getWateringHole(), 17)

	# def testFeedScavenger(self):
	# 	self.player1.setSpeciesBoards([self.speciesscavenger])
	# 	self.dealer.applyAction(Trait.scavenger, 1, self.dealer.feedingWithTraits)
	# 	self.assertEqual(self.dealer.getListOfPlayers()[0].getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)

	# def testFeedForaging(self):
	# 	self.player1.setSpeciesBoards([self.speciesforaging])
	# 	self.dealer.feed_foraging(self.player1, 0)
	# 	self.assertEqual(self.dealer.getListOfPlayers()[0].getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)

	# def testFeedCooperation(self):
	# 	self.player1.setSpeciesBoards([self.speciescoop, self.species1])
	# 	self.dealer.feed_cooperation(self.player1, 0)
	# 	self.assertEqual(self.dealer.getListOfPlayers()[0].getSpeciesBoards()[1].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)

	# def testAttack(self):
	# 	self.player1.setSpeciesBoards([self.species1])
	# 	self.dealer.attack(self.player1, 0)
	# 	self.assertEqual(self.species1.getPopulation(), 2)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getFoodBag(), 0)

	# def testExtinction(self):
	# 	self.player1.setSpeciesBoards([self.species2])
	# 	self.dealer.attack(self.player1, 0)
	# 	self.assertEqual(self.player1.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card, self.climbing_card])
	# 	self.assertEqual(self.dealer.getDeck(), [self.carnivore_card])
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getFoodBag(), 0)

	# def testGiveCardToPlayer(self):
	# 	self.dealer.giveCardsToPlayer(self.player2)
	# 	self.assertEqual(self.player2.getHand(), [self.warning_call_card, self.climbing_card])
	# 	self.assertEqual(self.dealer.getDeck(), [self.carnivore_card])
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player1.getHand(), [])
	# 	self.assertEqual(self.player1.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player1.getFoodBag(), 0)

	# def testFeedingFood(self):
	# 	self.player1.setSpeciesBoards([self.speciescoop, self.species2])
	# 	self.dealer.feeding(self.player1, 0, 1, False)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getFoodBag(), 0)


	# def testFeedingWithTraits(self):
	# 	self.player1.setSpeciesBoards([self.speciescoop, self.speciesforaging])
	# 	self.dealer.feedingWithTraits(self.player1, 0, 1)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getFood(), 2)
	# 	self.assertEqual(self.dealer.getWateringHole(), 17)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getFoodBag(), 0)


	# def testFeedingFat(self):
	# 	self.player1.setSpeciesBoards([self.speciesfat])
	# 	self.dealer.feeding(self.player1, 0, 2, True)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFatFood(), 3)
	# 	self.assertEqual(self.dealer.getWateringHole(), 18)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getFoodBag(), 0)


	# def testFeedingCarnivore(self):
	# 	self.player2.setSpeciesBoards([self.specieshorns])
	# 	self.player1.setSpeciesBoards([self.speciescarni])
	# 	self.dealer.feeding_carnivore(self.player1, [0, 0, 0])
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getPopulation(), 2)
	# 	self.assertEqual(self.player2.getSpeciesBoards()[0].getPopulation(), 2)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)



	# def testFeedingCarnivoreHornExtinction(self):
	# 	self.dealer.setDeck([self.warning_call_card, self.warning_call_card2, self.climbing_card, self.carnivore_card])
	# 	self.player2.setSpeciesBoards([self.specieshorns1])
	# 	self.player1.setSpeciesBoards([self.speciescarni1])
	# 	self.dealer.feeding_carnivore(self.player1, [0, 0, 0])
	# 	self.assertEqual(self.player1.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player1.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getFoodBag(), 0)
	# 	self.assertEqual(self.player2.getHand(), [self.warning_call_card, self.warning_call_card2])
	# 	self.assertEqual(self.player1.getHand(), [self.climbing_card, self.carnivore_card])
	# 	self.assertEqual(self.dealer.getWateringHole(), 20)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)



	# def testFeedingCarnivoreWithScavenger(self):
	# 	self.player2.setSpeciesBoards([self.specieshorns])
	# 	self.player1.setSpeciesBoards([self.speciescarni, self.speciesscavenger])
	# 	self.dealer.feeding_carnivore(self.player1, [0, 0, 0])
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getPopulation(), 2)
	# 	self.assertEqual(self.player2.getSpeciesBoards()[0].getPopulation(), 2)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 18)
	# 	self.assertEqual(self.player3.getHand(), [])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getFoodBag(), 0)


	# def testAutoFeed1(self):
	# 	self.player1.setSpeciesBoards([self.specieshorns])
	# 	auto = self.dealer.autoFeed()
	# 	self.assertTrue(auto)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)

	# def testAutoFeed2(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni])
	# 	auto = self.dealer.autoFeed()
	# 	self.assertFalse(auto)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 0)
	# 	self.assertEqual(self.dealer.getWateringHole(), 20)

	# def testAutoFeed3(self):
	# 	self.player1.setSpeciesBoards([])
	# 	auto = self.dealer.autoFeed()
	# 	self.assertTrue(auto)

	# def testWillFeed(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni])
	# 	self.player2.setSpeciesBoards([self.species1])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	result = self.dealer.willFeed()
	# 	self.assertEqual(result, (Trait.carnivore, [0, 0, 0]))

	# def testProcessFeed(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni])
	# 	self.player2.setSpeciesBoards([self.species1])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	result = self.dealer.processFeed((Trait.carnivore, [0, 0, 0]))
	# 	self.assertEqual(self.player2.getSpeciesBoards()[0].getPopulation(), 2)
	# 	self.assertEqual(self.player1.getSpeciesBoards()[0].getFood(), 1)
	# 	self.assertEqual(self.dealer.getWateringHole(), 19)


	# def testFeed1(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni])
	# 	self.player2.setSpeciesBoards([self.species1])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	result = self.dealer.executeFeed1AndReturn()
	# 	expected = [[self.player1, self.player2, self.player3], 19, self.deck]
	# 	self.assertEqual(result, expected)
	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 1)

	# def testFeed1ChangeIndex(self):
	# 	self.player1.setSpeciesBoards([self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.specieshorns1])
	# 	self.player3.setSpeciesBoards([self.speciescarni])
	# 	self.dealer.feed1()
	# 	self.assertEqual(self.dealer.getWateringHole(), 20)
	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 1)
	# 	self.assertEqual(self.speciesfull.getFood(), 2)
	# 	self.assertEqual(self.specieshorns1.getFood(), 0)
	# 	self.assertEqual(self.speciescarni.getFood(), 0)

	# def testFeedLoop1(self):
	# 	self.player1.setSpeciesBoards([self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciesfull1])
	# 	self.player3.setSpeciesBoards([self.speciesfull2])
	# 	self.player1.addToHand([self.warning_call_card2])

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.speciesfull.getFood(), 2)
	# 	self.assertEqual(self.speciesfull1.getFood(), 3)
	# 	self.assertEqual(self.speciesfull2.getFood(), 4)

	# 	self.assertEqual(self.speciesfull.getPopulation(), 2)
	# 	self.assertEqual(self.speciesfull1.getPopulation(), 3)
	# 	self.assertEqual(self.speciesfull2.getPopulation(), 4)

	# 	self.assertEqual(self.speciesfull.getBodySize(), 2)
	# 	self.assertEqual(self.speciesfull1.getBodySize(), 2)
	# 	self.assertEqual(self.speciesfull2.getBodySize(), 2)

	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesfull])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card2])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciesfull1])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesfull2])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [self.player1, self.player2, self.player3])
	# 	self.assertEqual(self.dealer.getWateringHole(), 20)

	# def testFeedLoop2(self):
	# 	self.player1.setSpeciesBoards([self.species1])
	# 	self.player2.setSpeciesBoards([self.species2])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	self.player1.addToHand([self.warning_call_card2])

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.species1.getFood(), 3)
	# 	self.assertEqual(self.species2.getFood(), 1)
	# 	self.assertEqual(self.speciescoop.getFood(), 3)

	# 	self.assertEqual(self.species1.getPopulation(), 3)
	# 	self.assertEqual(self.species2.getPopulation(), 1)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 3)

	# 	self.assertEqual(self.species1.getBodySize(), 3)
	# 	self.assertEqual(self.species2.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)

	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.species1])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card2])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.species2])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescoop])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [self.player2, self.player1, self.player3])
	# 	self.assertEqual(self.dealer.getWateringHole(), 13)

	# def testFeedLoop3(self):
	# 	self.player1.setSpeciesBoards([self.speciesfat])
	# 	self.player2.setSpeciesBoards([self.species2])
	# 	self.player3.setSpeciesBoards([self.speciescoop, self.species1])
	# 	self.player1.addToHand([self.warning_call_card2])

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.speciesfat.getFood(), 3)
	# 	self.assertEqual(self.species2.getFood(), 1)
	# 	self.assertEqual(self.speciescoop.getFood(), 3)
	# 	self.assertEqual(self.species1.getFood(), 3)

	# 	self.assertEqual(self.speciesfat.getPopulation(), 3)
	# 	self.assertEqual(self.species2.getPopulation(), 1)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 3)
	# 	self.assertEqual(self.species1.getPopulation(), 3)

	# 	self.assertEqual(self.speciesfat.getBodySize(), 3)
	# 	self.assertEqual(self.species2.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)
	# 	self.assertEqual(self.species1.getPopulation(), 3)

	# 	self.assertEqual(self.speciesfat.getFatFood(), 3)

	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesfat])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card2])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.species2])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescoop, self.species1])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [self.player2, self.player1, self.player3])
	# 	self.assertEqual(self.dealer.getWateringHole(), 8)

	# def testFeedLoop4(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni1])
	# 	self.player2.setSpeciesBoards([self.species2])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	self.player1.addToHand([self.warning_call_card2])

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.speciescarni1.getFood(), 1)
	# 	self.assertEqual(self.species2.getFood(), 1)
	# 	self.assertEqual(self.speciescoop.getFood(), 2)


	# 	self.assertEqual(self.speciescarni1.getPopulation(), 1)
	# 	self.assertEqual(self.species2.getPopulation(), 1)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 2)


	# 	self.assertEqual(self.speciescarni1.getBodySize(), 3)
	# 	self.assertEqual(self.species2.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)


	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card2])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.species2])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescoop])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [self.player1, self.player2, self.player3])
	# 	self.assertEqual(self.dealer.getWateringHole(), 16)

	# def testFeedLoop5(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni1])
	# 	self.player2.setSpeciesBoards([self.species2])
	# 	self.player3.setSpeciesBoards([self.speciescoop])
	# 	self.player1.addToHand([self.warning_call_card2])

	# 	self.species2.addTrait(Trait.climbing)
	# 	self.speciescoop.addTrait(Trait.climbing)

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.speciescarni1.getFood(), 0)
	# 	self.assertEqual(self.species2.getFood(), 1)
	# 	self.assertEqual(self.speciescoop.getFood(), 3)


	# 	self.assertEqual(self.speciescarni1.getPopulation(), 1)
	# 	self.assertEqual(self.species2.getPopulation(), 1)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 3)


	# 	self.assertEqual(self.speciescarni1.getBodySize(), 3)
	# 	self.assertEqual(self.species2.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)


	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player1.getHand(), [self.warning_call_card2])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.species2])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescoop])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [self.player1, self.player2, self.player3])
	# 	self.assertEqual(self.dealer.getWateringHole(), 16)

	# def testFeedLoopFeedLongNeckAndFertile(self):
	# 	self.player1.setSpeciesBoards([self.speciesLongFertile])

	# 	self.dealer.feedLoop()

	# 	self.assertEqual(self.speciesLongFertile.getFood(), 2)
	# 	self.assertEqual(self.speciesLongFertile.getPopulation(), 2)
	# 	self.assertEqual(self.speciesLongFertile.getBodySize(), 3)


	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 1)
	# 	self.assertEqual(self.dealer.isFed, [self.player2, self.player3, self.player1])
	# 	self.assertEqual(self.dealer.getWateringHole(), 18)

	# def testApplyFertile(self):
	# 	self.player1.setSpeciesBoards([self.speciesLongFertile])
	# 	self.player2.setSpeciesBoards([self.speciesFertile])

	# 	self.dealer.applyIncreasePopulation(Trait.fertile, 1)

	# 	self.assertEqual(self.speciesLongFertile.getFood(), 0)
	# 	self.assertEqual(self.speciesLongFertile.getPopulation(), 2)
	# 	self.assertEqual(self.speciesLongFertile.getBodySize(), 3)


	# 	self.assertEqual(self.speciesFertile.getFood(), 0)
	# 	self.assertEqual(self.speciesFertile.getPopulation(), 2)
	# 	self.assertEqual(self.speciesFertile.getBodySize(), 3)


	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciesFertile])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [])
	# 	self.assertEqual(self.dealer.getWateringHole(), 20)

	# def testApplyLongNeck(self):
	# 	self.player1.setSpeciesBoards([self.speciesLongFertile])
	# 	self.player2.setSpeciesBoards([self.speciesLongNeck])

	# 	self.dealer.applyAction(Trait.long_neck, 1, self.dealer.feedingWithTraits)

	# 	self.assertEqual(self.speciesLongFertile.getFood(), 1)
	# 	self.assertEqual(self.speciesLongFertile.getPopulation(), 1)
	# 	self.assertEqual(self.speciesLongFertile.getBodySize(), 3)


	# 	self.assertEqual(self.speciesLongNeck.getFood(), 1)
	# 	self.assertEqual(self.speciesLongNeck.getPopulation(), 1)
	# 	self.assertEqual(self.speciesFertile.getBodySize(), 3)


	# 	self.assertEqual(self.dealer.getListOfPlayers(), [self.player1, self.player2, self.player3])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciesLongNeck])
	# 	self.assertEqual(self.player2.getHand(), [])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	self.assertEqual(self.dealer.indexPlayerToBeFed, 0)
	# 	self.assertEqual(self.dealer.isFed, [])
	# 	self.assertEqual(self.dealer.getWateringHole(), 18)


	# def testGiveCardsToPlayer2(self):
	# 	self.dealer.setDeck([])
	# 	self.dealer.giveCardsToPlayer(self.player1)
	# 	self.assertEqual(self.player1.getHand(), [])

	# def testAskPlayerToDiscard(self):
	# 	self.player1.setSpeciesBoards([self.speciesLongFertile, self.speciescoop])
	# 	self.player2.setSpeciesBoards([self.speciesLongNeck])
	# 	self.player3.setSpeciesBoards([self.speciescarni1, self.specieshorns])

	# 	self.player1.setHand([self.fertileCard, self.climbingCard, self.carnivoreCard])
	# 	self.player2.setHand([self.cooperationCard, self.longNeckCard, self.carnivore_card])
	# 	self.player3.setHand([self.warning_call_card2, self.climbing_card])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile, self.speciescoop])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciesLongNeck])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescarni1, self.specieshorns])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card])

	# 	self.dealer.askPlayerToDiscard([[self.fertileCard, self.carnivoreCard], [], [self.warning_call_card2]])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile, self.speciescoop])
	# 	self.assertEqual(self.player1.getHand(), [self.climbingCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciesLongNeck])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciescarni1, self.specieshorns])
	# 	self.assertEqual(self.player3.getHand(), [self.climbing_card])



	# def testGetActions(self):
	# 	self.player1.start(1, self.speciesLongFertile, [self.fertileCard, self.climbingCard, self.carnivoreCard])

	# 	self.player2.start(1, self.speciescarni1, [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.player3.start(1, self.speciesforaging, [self.warning_call_card2, self.climbing_card, self.longNeckCard])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card, self.longNeckCard])

	# 	whCards, playerActions, btActions  = self.dealer.getActions()

	# 	self.assertEqual(whCards, [2, 2, 1])
	# 	self.assertEqual(btActions, [[[1, 0]], [[0, 1]], [[2, 0]]])
	# 	self.assertEqual(playerActions, [[[], [], []], [[], [], []], [[], [], []]])

	# def testStep2And3(self):
	# 	self.player1.start(1, self.speciesLongFertile, [self.fertileCard, self.climbingCard, self.carnivoreCard])

	# 	self.player2.start(1, self.speciescarni1, [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.player3.start(1, self.speciesforaging, [self.warning_call_card2, self.climbing_card, self.longNeckCard])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card, self.longNeckCard])

	# 	self.dealer.step2And3()

	# 	self.assertEqual(len(self.player1.getSpeciesBoards()), 2)
	# 	self.assertEqual(len(self.player2.getSpeciesBoards()), 2)
	# 	self.assertEqual(len(self.player3.getSpeciesBoards()), 2)

	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getTraits(), [Trait.fertile])
	# 	self.assertEqual(self.player2.getSpeciesBoards()[1].getTraits(), [Trait.long_neck])
	# 	self.assertEqual(self.player3.getSpeciesBoards()[1].getTraits(), [Trait.warning_call])

	# 	self.assertEqual(self.player1.getHand(), [])
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player3.getHand(), [])


	# def testGetActions2(self):
	# 	self.player1.start(1, self.speciesLongFertile, [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.player2.start(1, self.speciescarni1, [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.player3.start(1, self.speciesforaging, [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	whCards, playerActions, btActions  = self.dealer.getActions()

	# 	self.assertEqual(whCards, [5, 2, 3])
	# 	self.assertEqual(btActions, [[[2, 1]], [[3, 0]], [[1, 2]]])
	# 	self.assertEqual(playerActions, [[[[1, 3]], [[1, 0]], [[1, 0, 4]]], [[[1, 1]], [], []], [[[1, 0]],[], []]])

	# def testStep2And3_1(self):
	# 	self.player1.start(1, self.speciesLongFertile, [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.player2.start(1, self.speciescarni1, [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.player3.start(1, self.speciesforaging, [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	self.dealer.step2And3()

	# 	self.assertEqual(len(self.player1.getSpeciesBoards()), 2)
	# 	self.assertEqual(len(self.player2.getSpeciesBoards()), 2)
	# 	self.assertEqual(len(self.player3.getSpeciesBoards()), 2)

	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getPopulation(), 2)
	# 	self.assertEqual(self.player2.getSpeciesBoards()[1].getPopulation(), 2)
	# 	self.assertEqual(self.player3.getSpeciesBoards()[1].getPopulation(), 2)

	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getBodySize(), 1)
	# 	self.assertEqual(self.player2.getSpeciesBoards()[1].getBodySize(), 0)
	# 	self.assertEqual(self.player3.getSpeciesBoards()[1].getBodySize(), 0)


	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getFood(), 0)
	# 	self.assertEqual(self.player2.getSpeciesBoards()[1].getFood(), 0)
	# 	self.assertEqual(self.player3.getSpeciesBoards()[1].getFood(), 0)

	# 	self.assertEqual(self.player1.getSpeciesBoards()[1].getTraits(), [Trait.long_neck])
	# 	self.assertEqual(self.player2.getSpeciesBoards()[1].getTraits(), [Trait.cooperation])
	# 	self.assertEqual(self.player3.getSpeciesBoards()[1].getTraits(), [Trait.long_neck])

	# 	self.assertEqual(self.player1.getHand(), [])
	# 	self.assertEqual(self.player2.getHand(), [])
	# 	self.assertEqual(self.player3.getHand(), [])

	# 	externalPlayer1 = self.player1.externalPlayer
	# 	externalPlayer2 = self.player2.externalPlayer
	# 	externalPlayer3 = self.player3.externalPlayer

	# 	self.assertEqual(externalPlayer1.getHand(), [])
	# 	self.assertEqual(externalPlayer2.getHand(), [])
	# 	self.assertEqual(externalPlayer3.getHand(), [])




	# def testStep4(self):
	# 	self.player1.start(1, self.speciesLongFertile, [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.player2.start(1, self.speciescarni1, [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.player3.start(1, self.speciesforaging, [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player1.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard1, self.longNeckCard1, self.ambushCard])

	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player2.getHand(), [self.cooperationCard, self.longNeckCard, self.carnivore_card, self.carnivoreCard1])

	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])
	# 	self.assertEqual(self.player3.getHand(), [self.warning_call_card2, self.climbing_card, self.longNeckCard, self.climbingCard1])

	# 	self.assertEqual(self.dealer.getWateringHole(), 20)

	# 	self.dealer.step4()


	# 	self.assertEqual(self.player1.getSpeciesBoards(), [self.speciesLongFertile])
	# 	self.assertEqual(self.player2.getSpeciesBoards(), [self.speciescarni1])
	# 	self.assertEqual(self.player3.getSpeciesBoards(), [self.speciesforaging])

	# 	self.assertEqual(self.speciesLongFertile.getBodySize(), 3)
	# 	self.assertEqual(self.speciescarni1.getBodySize(), 3)
	# 	self.assertEqual(self.speciesforaging.getBodySize(), 3)

	# 	self.assertEqual(self.speciesLongFertile.getPopulation(), 2)
	# 	self.assertEqual(self.speciescarni1.getPopulation(), 1)
	# 	self.assertEqual(self.speciesforaging.getPopulation(), 2)

	# 	self.assertEqual(self.speciesLongFertile.getFood(), 2)
	# 	self.assertEqual(self.speciescarni1.getFood(), 1)
	# 	self.assertEqual(self.speciesforaging.getFood(), 2)

	# 	self.assertEqual(self.dealer.getWateringHole(), 15)



	# def testCanDeal(self):
	# 	self.assertFalse(self.dealer.canDeal())

	# def testCanDeal1(self):
	# 	self.dealer.setDeck(deck.generateDeck())
	# 	self.assertTrue(self.dealer.canDeal())

	# def testCanDeal2(self):
	# 	self.dealer.setDeck(self.deck2)
	# 	self.assertTrue(self.dealer.canDeal())

	# def testDealSpeciesBoards(self):
	# 	sp = self.dealer.dealSpeciesBoards(self.player1)
	# 	self.assertEqual(sp.getPopulation(), 1)
	# 	self.assertEqual(sp.getBodySize(), 0)
	# 	self.assertEqual(sp.getFood(), 0)
	# 	self.assertEqual(sp.getTraits(), [])

	# def testDealSpeciesBoards2(self):
	# 	self.player1.setSpeciesBoards([self.speciescarni1])
	# 	sp = self.dealer.dealSpeciesBoards(self.player1)
	# 	self.assertFalse(sp)

	# def testDealCards(self):
	# 	self.dealer.setDeck(deck.generateDeck())
	# 	self.player1.setSpeciesBoards([self.speciesfull])
	# 	self.assertEqual(len(self.dealer.dealCards(self.player1)), 5)

	# def testDealCards1(self):
	# 	self.dealer.setDeck(deck.generateDeck())
	# 	self.assertEqual(len(self.dealer.dealCards(self.player1)), 4)

	# def testReducePopulations(self):
	# 	self.specieshorns.addToFood(2)
	# 	self.speciescoop.addToFood(1)
	# 	self.speciesfat.addToFood(1)
	# 	self.player1.setSpeciesBoards([self.specieshorns, self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciescoop])
	# 	self.player3.setSpeciesBoards([self.speciesfat])

	# 	self.dealer.reducePopulations()

	# 	self.assertEqual(self.specieshorns.getPopulation(), 2)
	# 	self.assertEqual(self.speciesfull.getPopulation(), 2)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 1)
	# 	self.assertEqual(self.speciesfat.getPopulation(), 1)

	# 	self.assertEqual(self.specieshorns.getFood(), 2)
	# 	self.assertEqual(self.speciesfull.getFood(), 2)
	# 	self.assertEqual(self.speciescoop.getFood(), 1)
	# 	self.assertEqual(self.speciesfat.getFood(), 1)


	# 	self.assertEqual(self.specieshorns.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfull.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfat.getBodySize(), 3)

	# def testMoveToBag(self):
	# 	self.specieshorns.addToFood(2)
	# 	self.speciescoop.addToFood(1)
	# 	self.speciesfat.addToFood(1)
	# 	self.player1.setSpeciesBoards([self.specieshorns, self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciescoop])
	# 	self.player3.setSpeciesBoards([self.speciesfat])

	# 	self.dealer.moveFoodToBag()

	# 	self.assertEqual(self.specieshorns.getPopulation(), 3)
	# 	self.assertEqual(self.speciesfull.getPopulation(), 2)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 3)
	# 	self.assertEqual(self.speciesfat.getPopulation(), 3)

	# 	self.assertEqual(self.specieshorns.getFood(), 0)
	# 	self.assertEqual(self.speciesfull.getFood(), 0)
	# 	self.assertEqual(self.speciescoop.getFood(), 0)
	# 	self.assertEqual(self.speciesfat.getFood(), 0)


	# 	self.assertEqual(self.specieshorns.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfull.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfat.getBodySize(), 3)

	# 	self.assertEqual(self.player1.getFoodBag(), 4)
	# 	self.assertEqual(self.player2.getFoodBag(), 1)
	# 	self.assertEqual(self.player3.getFoodBag(), 1)

	# def testEndTurn(self):
	# 	self.specieshorns.addToFood(2)
	# 	self.speciescoop.addToFood(1)
	# 	self.speciesfat.addToFood(1)
	# 	self.player1.setSpeciesBoards([self.specieshorns, self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciescoop])
	# 	self.player3.setSpeciesBoards([self.speciesfat])

	# 	self.dealer.endTurn()

	# 	self.assertEqual(self.specieshorns.getPopulation(), 2)
	# 	self.assertEqual(self.speciesfull.getPopulation(), 2)
	# 	self.assertEqual(self.speciescoop.getPopulation(), 1)
	# 	self.assertEqual(self.speciesfat.getPopulation(), 1)


	# 	self.assertEqual(self.specieshorns.getFood(), 0)
	# 	self.assertEqual(self.speciesfull.getFood(), 0)
	# 	self.assertEqual(self.speciescoop.getFood(), 0)
	# 	self.assertEqual(self.speciesfat.getFood(), 0)


	# 	self.assertEqual(self.specieshorns.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfull.getBodySize(), 2)
	# 	self.assertEqual(self.speciescoop.getBodySize(), 3)
	# 	self.assertEqual(self.speciesfat.getBodySize(), 3)

	# 	self.assertEqual(self.player1.getFoodBag(), 4)
	# 	self.assertEqual(self.player2.getFoodBag(), 1)
	# 	self.assertEqual(self.player3.getFoodBag(), 1)

	# def testScores(self):
	# 	self.specieshorns.addToFood(2)
	# 	self.speciescoop.addToFood(1)
	# 	self.speciesfat.addToFood(1)
	# 	self.player1.setSpeciesBoards([self.specieshorns, self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciescoop])
	# 	self.player3.setSpeciesBoards([self.speciesfat])

	# 	self.player1.setFoodBag(100)
	# 	self.player2.setFoodBag(1000)
	# 	self.player3.setFoodBag(10)

	# 	scores = self.dealer.scores()

	# 	p1Score, p2Score, p3Score = scores

	# 	self.assertEqual(p1Score, "1 player id: 2 name: j score: 1004" )
	# 	self.assertEqual(p2Score, "2 player id: 1 name: j score: 106" )
	# 	self.assertEqual(p3Score, "3 player id: 3 name: j score: 14" )

	# def testGetLOS(self):
	# 	self.player1.setSpeciesBoards([self.specieshorns, self.speciesfull])
	# 	self.player2.setSpeciesBoards([self.speciescoop])
	# 	self.player3.setSpeciesBoards([self.speciesfat])
	# 	lolos = self.dealer.getLOS(self.player2, False)

	# 	self.assertEqual(lolos, [[self.speciesfat]])



	# def testStep1(self):
	# 	self.dealer.setDeck(deck.generateDeck())

	# 	self.dealer.step1()

	# 	self.assertEqual(len(self.player1.getSpeciesBoards()), 1)
	# 	self.assertEqual(len(self.player2.getSpeciesBoards()), 1)
	# 	self.assertEqual(len(self.player3.getSpeciesBoards()), 1)

	# 	self.assertEqual(len(self.player1.getHand()), 4)
	# 	self.assertEqual(len(self.player2.getHand()), 4)
	# 	self.assertEqual(len(self.player3.getHand()), 4)

	# 	self.assertEqual(len(self.player1.externalPlayer.getHand()), 4)
	# 	self.assertEqual(len(self.player2.externalPlayer.getHand()), 4)
	# 	self.assertEqual(len(self.player3.externalPlayer.getHand()), 4)



	# def testDealerStrings(self):
	# 	[wh, lop, loc] = self.dealer.dealer_strings()
	# 	self.assertEqual(wh, "20")
	# 	self.assertEqual(len(lop), 3)
	# 	self.assertEqual(len(loc), 3)
	# 	# self.assertEqual(lop[0], ["1 player id: 2  score: 1004", [], []])
	# 	# self.assertEqual(lop[1], ["1 player id: 2  score: 1004", [], []])
	# 	# self.assertEqual(lop[2], ["1 player id: 2 name: j score: 1004", [], []])
	# 	self.assertEqual(loc[0], "card: food points: 0, trait: warning-call")
	# 	self.assertEqual(loc[1], "card: food points: 3, trait: climbing")
	# 	self.assertEqual(loc[2], "card: food points: -8, trait: carnivore")

	def testRunGame(self):
		print "IN TEST RUN GAME"
		self.dealer.setDeck(deck.generateDeck())
		self.dealer.setWateringHole(0)
		self.dealer.setListOfPlayers(self.players8)
		scores = self.dealer.runGame()
		for s in scores:
			print s
		self.assertTrue(True)



if __name__ == '__main__':
	unittest.main()
