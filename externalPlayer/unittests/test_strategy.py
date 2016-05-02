# Unit tests for initial Player Strategy in Evolution
import unittest, sys, os

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../../dealer'))
import dealer
import species
import trait

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))

from sillyPlayer import SillyPlayer

import strategy


class TestStrategy(unittest.TestCase):
  def setUp(self):
    self.player = SillyPlayer(1, [], 0)
    self.strat = strategy.Strategy()

    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore = species.Species(0, 1, 1, [])
    self.fat_carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore.setBodySize(5)

    self.herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore.setBodySize(4)

    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setBodySize(3)
    self.fat_tissue.setTraits([trait.Trait.fat_tissue])
    self.fat_fat_tissue = species.Species(0, 1, 1, [])
    self.fat_fat_tissue.setBodySize(6)
    self.fat_fat_tissue.setTraits([trait.Trait.fat_tissue])

    self.opherb = species.Species(0, 1, 1, [])
    self.opfatherb = species.Species(0, 1, 1, [])
    self.opfatherb.setBodySize(4)

    self.opponent1 = SillyPlayer(1, [], 0)
    self.opponent1.setSpeciesBoards([self.opherb, self.opfatherb])
    self.opponents = [[self.opherb, self.opfatherb]]

    self.dealer = dealer.Dealer(4, [self.player, self.opponent1])

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

  def testFatTissueFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), [1, 3])

  def testBiggestFatTissueFirst(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_fat_tissue])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), [1, 4])

  def testHerbBeforeCarni(self):
    self.player.setSpeciesBoards([self.herbavore, self.carnivore])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), 0)

  def testLargestHerbFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_herbavore])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), 1)

  def testLargestCarnivoreFirstIfAllHerbFed(self):
    self.herbavore.setFood(1)
    self.player.setSpeciesBoards([self.herbavore, self.carnivore, self.fat_carnivore])
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), [2, 0, 1])

  def testWontAttackSelf(self):
    self.player.setSpeciesBoards([self.fat_carnivore])
    self.opponents = []
    self.assertEqual(self.player.feedNext(4, self.opponents, [self.player.getFoodBag(), self.player.getHand(), self.player.getSpeciesBoards()]), False)

  # #Unit Test Helper Methods
  def testSortByLexPop(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(3)
    loa = [self.herbavore, self.carnivore]
    self.assertEqual(self.strat.sortByLex(loa, False), [self.carnivore, self.herbavore])

  def testSortByLexFood(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(1)
    self.herbavore.setFood(1)
    self.carnivore.setFood(3)
    loa = [self.carnivore, self.herbavore]
    self.assertEqual(self.strat.sortByLex(loa, False), [self.carnivore, self.herbavore])

  def testSortByLexBodySize(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(1)
    self.herbavore.setFood(1)
    self.carnivore.setFood(1)
    self.herbavore.setBodySize(1)
    self.carnivore.setBodySize(3)
    loa = [self.carnivore, self.herbavore]
    self.assertEqual(self.strat.sortByLex(loa, False), [self.carnivore, self.herbavore])

  def testSortByLex(self):
    self.herbavore.setPopulation(1)
    self.herbavore.setFood(1)
    self.herbavore.setBodySize(3)

    self.carnivore.setPopulation(2)
    self.carnivore.setFood(1)
    self.carnivore.setBodySize(2)

    self.fat_tissue.setPopulation(1)
    self.fat_tissue.setFood(2)
    self.fat_tissue.setBodySize(3)

    loa = [self.herbavore, self.carnivore, self.fat_tissue]
    loas = self.strat.sortByLex(loa, False)
    self.assertEqual(loas, [self.carnivore, self.fat_tissue, self.herbavore])

  def testStereotypeAnimals(self):
    loa = [self.fat_herbavore, self.herbavore, self.fat_carnivore, self.fat_tissue]
    expectedOutput = ([self.fat_tissue], [self.fat_carnivore], [self.fat_herbavore, self.herbavore])
    self.assertEqual(self.strat.stereotypeAnimals(loa), expectedOutput)

  def testFindFattestIfFatTissue(self):
    fat = [self.fat_tissue]
    carni = [self.fat_carnivore]
    herb = [self.fat_herbavore, self.herbavore]
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_tissue, trait.Trait.fat_tissue))

  def testFindFattestIfHerbi(self):
    fat = []
    carni = [self.fat_carnivore]
    herb = [self.fat_herbavore, self.herbavore]
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_herbavore, False))

  def testFindFattestIfCarni(self):
    fat = []
    carni = [self.fat_carnivore]
    herb = []
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_carnivore, trait.Trait.carnivore))

  def testFeedNext(self):
    loa = [self.fat_herbavore, self.herbavore, self.fat_carnivore, self.fat_tissue]
    self.assertEqual(self.strat.feedNext(loa), (self.fat_tissue, trait.Trait.fat_tissue))


  def testSortOpponentsSpecies(self):
    inpt = [[self.herbavore, self.fat_tissue], [self.opherb, self.opfatherb]]
    output = [[self.fat_tissue, self.herbavore] , [self.opfatherb, self.opherb]]
    self.assertEqual(self.strat.sortOpponentsSpecies(inpt), output)

  def testGetNeighborsNoLeft(self):
    self.assertEqual(self.strat.getNeighbors([self.herbavore, self.fat_tissue], self.fat_tissue), (self.herbavore, False))

  def testGetNeighborsNoRight(self):
    self.assertEqual(self.strat.getNeighbors([self.herbavore, self.fat_tissue], self.herbavore), (False, self.fat_tissue))

  def testPickVictim(self):
    self.assertEqual(self.strat.pickVictim([self.carnivore], [[self.herbavore, self.fat_tissue], [self.opherb, self.opfatherb]]), [1, 1 , self.carnivore])

if __name__ == '__main__':
    unittest.main()
