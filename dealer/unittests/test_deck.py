import unittest
import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from  deck import generateDeck, compareTraitCard
import trait
from trait_card import TraitCard

class TestDeck(unittest.TestCase):
  def setUp(self):
    self.thisDeck = generateDeck()
    self.card1 = TraitCard(trait.Trait.ambush, -2)
    self.card2 = TraitCard(trait.Trait.carnivore, -8)
    self.card3 = TraitCard(trait.Trait.ambush, 0)


  def tearDown(self):
    del self.thisDeck

  def testDeckSize(self):
    self.assertEqual(len(self.thisDeck), 122)

  def testCarnivoreCards(self):
    carniNum = 0
    otherNum = 0
    for card in self.thisDeck:
      if card.trait is trait.Trait.carnivore:
        carniNum += 1
      else:
        otherNum += 1
    self.assertEqual(carniNum, 17)
    self.assertEqual(otherNum, 105)

  def testCompareTraitCard(self):
    self.assertEqual(compareTraitCard(self.card1, self.card2), 1)
    self.assertEqual(compareTraitCard(self.card2, self.card1), -1)
    self.assertEqual(compareTraitCard(self.card1, self.card3), 1)
    self.assertEqual(compareTraitCard(self.card3, self.card1), -1)
    self.assertEqual(compareTraitCard(self.card1, self.card1), 0)














if __name__ == '__main__':
    unittest.main()

