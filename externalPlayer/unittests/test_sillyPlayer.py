# unit tests for the Player in Evolution
import unittest, os, sys

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../../dealer'))


import dealer
import species
import trait
import trait_card

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

import sillyPlayer
import strategy

class TestSillyPlayer(unittest.TestCase):
  def setUp(self):
    self.player = sillyPlayer.SillyPlayer(1, [], 0)
    self.player1 = sillyPlayer.SillyPlayer(1, [], 0)


    self.speciesWith3Traits = species.Species(0, 0, 1, [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])

    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.Trait.carnivore])

    self.herbavore = species.Species(0, 1, 1, [])
    self.herbavore2 = species.Species(0, 1, 1, [])

    self.herbavore3 = species.Species(1, 1, 1, [])
    self.herbavore4 = species.Species(2, 1, 2, [])

    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setTraits([trait.Trait.fat_tissue])
    self.fat_tissue2 = species.Species(0, 3, 1, [])
    self.fat_tissue2.setTraits([trait.Trait.fat_tissue])

    self.opherb = species.Species(0, 1, 1, [])
    self.opfatherb = species.Species(0, 7, 1, [])

    self.opponent1 = sillyPlayer.SillyPlayer(2, [], 0)
    self.opponent1.setSpeciesBoards([self.opherb, self.opfatherb])
    self.opponents = [[self.opherb, self.opfatherb]]

    self.dealer = dealer.Dealer(4, [self.player, self.opponent1])

    self.fertileCard = trait_card.TraitCard(trait.Trait.fertile, 2)
    self.climbingCard = trait_card.TraitCard(trait.Trait.climbing, 0)
    self.cooperationCard = trait_card.TraitCard(trait.Trait.cooperation, 0)
    self.carnivoreCard = trait_card.TraitCard(trait.Trait.carnivore, 0)
    self.longNeckCard = trait_card.TraitCard(trait.Trait.long_neck, 0)
    self.ambushCard = trait_card.TraitCard(trait.Trait.ambush, 0)


  def tearDown(self):
    del self.player
    del self.carnivore
    del self.herbavore
    del self.fat_tissue
    del self.opherb
    del self.opfatherb
    del self.opponent1
    del self.opponents
    del self.dealer

  # FeedNext Tests
  def testSimpleHerbavore(self):
    self.player.setSpeciesBoards([self.herbavore, self.herbavore2])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getSpeciesBoards(), self.player.getHand()]), 0)

  def testSimpleCarnivore(self):
    self.player.setSpeciesBoards([self.carnivore])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getSpeciesBoards(), self.player.getHand()]), [0, 0, 1])

  def testSimpleFatTissue(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_tissue2])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getSpeciesBoards(), self.player.getHand()]), [1, 3])


  # Getter and Setter Tests
  def testGetSetSpeciesBoards(self):
    self.player.setSpeciesBoards(self.herbavore)
    self.assertEqual(self.player.getSpeciesBoards(), self.herbavore)

  def testGetSetAddFoodBag(self):
    self.player.setFoodBag(4)
    self.player.addToFoodBag(1)
    self.assertEqual(self.player.getFoodBag(), 5)

  def testGetSetPlayerID(self):
    self.player.setPlayerId(2)
    self.assertEqual(self.player.getPlayerId(), 2)

  \
  def testChoose1(self):
    self.player.setHand([self.fertileCard, self.climbingCard, self.cooperationCard])
    chosen =  self.player.choose([], [])
    self.assertEqual(chosen, [1, [], [], [[2, 0]], []])

  def testChoose2(self):
    self.player.setHand([self.fertileCard, self.climbingCard, self.cooperationCard, self.longNeckCard, self.carnivoreCard, self.ambushCard])
    chosen =  self.player.choose([], [])
    self.assertEqual(chosen, [5, [[0, 2]], [[0, 0]], [[4, 1]], [[0, 0, 3]]])

  def testStart(self):
    self.player.setHand([self.fertileCard, self.carnivoreCard, self.ambushCard])
    self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2])
    self.player.getHand().extend([self.climbingCard, self.cooperationCard, self.longNeckCard])
    self.player.getSpeciesBoards().append(self.herbavore2)
    self.player1.start([1, self.player.getFoodBag(), self.player.getSpeciesBoards(), self.player.getHand()])
    self.assertEqual(self.player1.getHand(), [self.fertileCard, self.carnivoreCard, self.ambushCard, self.climbingCard, self.cooperationCard, self.longNeckCard])
    self.assertEqual(self.player1.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2, self.herbavore2])



if __name__ == '__main__':
    unittest.main()
