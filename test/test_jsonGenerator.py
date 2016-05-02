import unittest, os, sys

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../dealer'))

import species
import trait
import trait_card
import inPlayer

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../dealer/processing'))

import make_json

class TestJsonGenerations(unittest.TestCase):
  def setUp(self):
    self.maker = make_json.MakeJSON()
    self.species1 = species.Species(0, 1, 3, [])
    self.carni2 = species.Species(0, 2, 3, [trait.Trait.carnivore])
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

    self.fertileCard = trait_card.TraitCard(trait.Trait.fertile, 2)
    self.climbingCard = trait_card.TraitCard(trait.Trait.climbing, 0)
    self.cooperationCard = trait_card.TraitCard(trait.Trait.cooperation, 0)
    self.carnivoreCard = trait_card.TraitCard(trait.Trait.carnivore, 0)
    self.longNeckCard = trait_card.TraitCard(trait.Trait.long_neck, 0)
    self.ambushCard = trait_card.TraitCard(trait.Trait.ambush, 0)
    self.burrowingCard = trait_card.TraitCard(trait.Trait.burrowing, 0)
    self.cooperation2Card = trait_card.TraitCard(trait.Trait.cooperation, -1)

    self.player1 = inPlayer.Player(1, [], 0)
    self.player2 = inPlayer.Player(2, [], 0)
    self.player3 = inPlayer.Player(3, [], 0)

  def tearDown(self):
    del self.maker
    del self.species1
    del self.carni2
    del self.herbavore
    del self.herbavore2
    del self.herbavore3
    del self.herbavore4
    del self.fat_tissue
    del self.fat_tissue2
    del self.opherb
    del self.opfatherb
    del self.fertileCard
    del self.climbingCard
    del self.cooperationCard
    del self.carnivoreCard
    del self.longNeckCard
    del self.ambushCard
    del self.player1
    del self.player2
    del self.player3

  # def test1(self):
  #   self.player1.setHand([self.fertileCard, self.longNeckCard, self.ambushCard])
  #   self.player1.setSpeciesBoards([self.species1, self.carni2])
  #   specieslist = []
  #   afterlist = [[self.herbavore, self.herbavore2], [self.herbavore4, self.herbavore3]]
  #   print self.maker.make_choice(self.player1, specieslist, afterlist)
  #   self.assertTrue(True)

  # def test2(self):
  #   self.player2.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard])
  #   self.player2.setSpeciesBoards([self.species1, self.carni2])
  #   specieslist = [[self.herbavore, self.herbavore2]]
  #   afterlist = [[self.herbavore4, self.herbavore3]]
  #   print self.maker.make_choice(self.player2, specieslist, afterlist)
  #   self.assertTrue(True)

  # def test3(self):
  #   self.player3.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard, self.climbingCard])
  #   self.player3.setSpeciesBoards([self.species1, self.carni2])
  #   specieslist = [[self.herbavore, self.herbavore2], [self.herbavore4, self.herbavore3]]
  #   afterlist = []
  #   print self.maker.make_choice(self.player3, specieslist, afterlist)
  #   self.assertTrue(True)


  # def test4(self):
  #   self.player1.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard, self.climbingCard, self.burrowingCard])
  #   self.player1.setSpeciesBoards([self.species1, self.carni2])
  #   specieslist = []
  #   afterlist = [[self.herbavore, self.herbavore2], [self.herbavore4, self.herbavore3]]
  #   print self.maker.make_choice(self.player1, specieslist, afterlist)
  #   self.assertTrue(True)

  def test5(self):
    self.player1.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard, self.climbingCard, self.burrowingCard, self.cooperation2Card])
    self.player1.setSpeciesBoards([self.species1, self.carni2])
    specieslist = []
    afterlist = [[self.herbavore, self.herbavore2], [self.herbavore4, self.herbavore3]]
    print self.maker.make_choice(self.player1, specieslist, afterlist)
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
