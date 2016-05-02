import unittest, sys, os

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from  dealer import Dealer
from species import Species
from  trait import Trait
from trait_card import TraitCard
from inPlayer import Player
from validate import validateAction4, validateFeedingChoice

class TestUtils(unittest.TestCase):
  def setUp(self):
    self.species1 = Species(0, 1, 3, [])
    self.carni2 = Species(0, 2, 3, [Trait.carnivore])
    self.herbavore = Species(0, 1, 1, [])
    self.herbavore2 = Species(0, 1, 1, [])

    self.herbavore3 = Species(1, 1, 1, [])
    self.herbavore4 = Species(2, 1, 2, [])

    self.fat_tissue = Species(0, 1, 1, [])
    self.fat_tissue.setTraits([Trait.fat_tissue])
    self.fat_tissue2 = Species(0, 3, 1, [])
    self.fat_tissue2.setTraits([Trait.fat_tissue])

    self.opherb = Species(0, 1, 1, [])
    self.opfatherb = Species(0, 7, 1, [])

    self.fertileCard = TraitCard(Trait.fertile, 2)
    self.climbingCard = TraitCard(Trait.climbing, 0)
    self.cooperationCard = TraitCard(Trait.cooperation, 0)
    self.carnivoreCard = TraitCard(Trait.carnivore, 0)
    self.longNeckCard = TraitCard(Trait.long_neck, 0)
    self.ambushCard = TraitCard(Trait.ambush, 0)
    self.burrowingCard = TraitCard(Trait.burrowing, 0)
    self.cooperation2Card = TraitCard(Trait.cooperation, -1)

    self.player1 = Player(1, [], 0)
    self.player2 = Player(2, [], 0)
    self.player3 = Player(3, [], 0)

    self.validAction1 = [2, [[2, 6]], [[2, 3]], [[5, 4]], [[2, 0, 0]]]
    self.validAction2 = [2, [[2, 0]], [[2, 1]], [[4, 3]], []]
    self.validAction3 = [2, [[2, 1]], [], [[3, 0]], []]
    self.validAction4 = [2, [], [], [[0, 1]], []]
    self.validAction5 = [0, [], [], [], []]

    self.invalidAction1 = ["hi", 1, [], "so", False]
    self.invalidAction2 = ["hi", 1, []]
    self.invalidAction3 = [False, [["2", 6]], [[2, 3]], [[5, 4]], [[2, 0, 0]]]

    self.validFeeding1 = False
    self.validFeeding2 = 1
    self.validFeeding3 = [1, 9]
    self.validFeeding4 = [0, 0, 1]

    self.invalidFeeding1 = True
    self.invalidFeeding2 = [1, 2, 3, 3, ""]
    self.invalidFeeding3 = ["p", "i", "e"]


  def tearDown(self):
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
    del self.burrowingCard
    del self.cooperation2Card

    del self.player1
    del self.player2
    del self.player3

    del self.validAction1
    del self.validAction2
    del self.validAction3
    del self.validAction4
    del self.validAction5

  def testValidateAction1(self):
    # test 1
    self.player1.setHand([self.fertileCard, self.longNeckCard, self.ambushCard])
    self.player1.setSpeciesBoards([self.species1, self.carni2])
    self.assertTrue(validateAction4(self.validAction4, self.player1))

  def testValidateAction2(self):
    # test 2
    self.player2.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard])
    self.player2.setSpeciesBoards([self.species1, self.carni2])
    self.assertTrue(validateAction4(self.validAction3, self.player2))

  def testValidateAction3(self):
    # test 3
    self.player3.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard, self.climbingCard])
    self.player3.setSpeciesBoards([self.species1, self.carni2])
    self.assertTrue(validateAction4(self.validAction2, self.player3))

  def testValidateAction4(self):
    # from test 5
    self.player1.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard, self.climbingCard, self.burrowingCard, self.cooperation2Card])
    self.player1.setSpeciesBoards([self.species1, self.carni2])
    self.assertTrue(validateAction4(self.validAction1, self.player1))

  def testValidateAction5(self):
    self.player2.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard])
    self.assertTrue(validateAction4(self.validAction5, self.player2))

  def testValidateAction1Invalid(self):
    # test 1
    self.player1.setHand([self.longNeckCard, self.ambushCard])
    self.player1.setSpeciesBoards([self.species1, self.carni2])
    self.assertFalse(validateAction4(self.validAction4, self.player1))

  def testValidateAction2Invalid(self):
    #test 2
    self.player2.setHand([self.fertileCard, self.longNeckCard, self.ambushCard, self.cooperationCard])
    self.player2.setSpeciesBoards([self.carni2])
    self.assertFalse(validateAction4(self.validAction3, self.player2))

  def testValidateAction3Invalid(self):
    # test 3
    self.player3.setHand([self.fertileCard, self.climbingCard])
    self.player3.setSpeciesBoards([self.species1, self.carni2])
    self.assertFalse(validateAction4(self.validAction2, self.player3))

  def testValidateAction4Invalid(self):
    self.assertFalse(validateAction4(self.invalidAction1, self.player2))

  def testValidateAction5Invalid(self):
    self.assertFalse(validateAction4(self.invalidAction2, self.player2))

  def testValidateAction6Invalid(self):
    self.assertFalse(validateAction4(self.invalidAction3, self.player2))

  def testValidateFeeding1(self):
    self.assertTrue(validateFeedingChoice(self.validFeeding1, self.player1, [], 2))

  def testValidateFeeding2(self):
    self.player2.setSpeciesBoards([self.species1, self.carni2])
    self.assertTrue(validateFeedingChoice(self.validFeeding2, self.player2, [], 2))

  def testValidateFeeding3(self):
    self.player2.setSpeciesBoards([self.species1 ,self.fat_tissue2, self.carni2])
    self.assertTrue(validateFeedingChoice(self.validFeeding3, self.player2, [], 9))

  def testValidateFeeding4(self):
    self.player2.setSpeciesBoards([self.carni2, self.species1])
    self.assertFalse(validateFeedingChoice(self.validFeeding4, self.player2, [[self.species1]], 100))

  def testValidateFeeding2Invalid(self):
    self.assertFalse(validateFeedingChoice(self.validFeeding2, self.player2, [], 2))

  def testValidateFeeding3Invalid(self):
    self.player2.setSpeciesBoards([self.species1, self.carni2])
    self.assertFalse(validateFeedingChoice(self.validFeeding3, self.player2, [], 9))

  def testValidateFeeding4Invalid(self):
    self.player2.setSpeciesBoards([self.species1, self.carni2])
    self.assertFalse(validateFeedingChoice(self.validFeeding4, self.player2, [[self.species1]], 100))

  def testValidateFeeding01Invalid(self):
    self.assertFalse(validateFeedingChoice(self.invalidFeeding1, self.player2, [], 2))

  def testValidateFeeding02Invalid(self):
    self.player2.setSpeciesBoards([self.species1, self.carni2])
    self.assertFalse(validateFeedingChoice(self.invalidFeeding2, self.player2, [], 9))

  def testValidateFeeding03Invalid(self):
    self.player2.setSpeciesBoards([self.species1])
    self.assertFalse(validateFeedingChoice(self.invalidFeeding3, self.player2, [[self.species1]], 100))





if __name__ == '__main__':
  unittest.main()
