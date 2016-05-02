import unittest, sys, os

this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
import trait_card
import trait

class TestTraitCard(unittest.TestCase):
  def setUp(self):
    self.card = trait_card.TraitCard(trait.Trait.fat_tissue, 0)

  def tearDown(self):
    del self.card

  def testSetAndGetFoodPoints(self):
    self.card.setFoodPoints(3)
    self.assertEqual(self.card.getFoodPoints(), 3)

  def testSetAndGetTrait(self):
    self.card.setTrait(trait.Trait.herding)
    self.assertEqual(self.card.getTrait(), trait.Trait.herding)

  def testSetFoodPointsError(self):
    with self.assertRaises(Exception) as context:
      self.card.setFoodPoints(-9)
      self.assertTrue("invalid food_points" in context)

  def testSetTraitError(self):
    with self.assertRaises(Exception) as context:
      self.card.setTrait("0")
      self.assertTrue("invalid trait" in context)

if __name__ == '__main__':
  unittest.main()
