# Unit tests for initial Player Strategy in Evolution
import unittest, sys, os

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
import dealer
import species
import trait
import inPlayer
import utils

class TestUtils(unittest.TestCase):
  def setUp(self):
    self.player = inPlayer.Player(1, [], 0)
    # self.strat = strategy.Strategy()

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

    self.opponent1 = inPlayer.Player(1, [], 0)
    self.opponent1.setSpeciesBoards([self.opherb, self.opfatherb])
    self.opponents = [self.opponent1]

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


  def testCompileSpecies(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(utils.compileSpecies([self.player, self.opponent1]), [[self.herbavore, self.fat_tissue], [self.opherb, self.opfatherb]])


if __name__ == '__main__':
    unittest.main()
