# unit tests for a Species in the game Evolution
import unittest, os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
import species
import trait

class TestSpecies(unittest.TestCase):

  def setUp(self):
    self.spec = species.Species(0, 7, 6, [])

  def tearDown(self):
    del self.spec

  def testSetAndGetFood(self):
    self.spec.setFood(3)
    self.spec.addToFood(1)
    self.assertEqual(self.spec.getFood(), 4)

  def testSetAndGetPopulation(self):
    self.spec.setPopulation(4)
    self.spec.addToPopulation(1)
    self.assertEqual(self.spec.getPopulation(), 5)

  def testSetAndGetBodySize(self):
    self.spec.setBodySize(2)
    self.assertEqual(self.spec.getBodySize(), 2)

  def testSetAndGetTraitsAndDiscardTrait(self):
    self.spec.setTraits([trait.Trait.carnivore])
    self.assertEqual(self.spec.getTraits(), [trait.Trait.carnivore])
    self.spec.discardTrait(0)
    self.assertEqual(self.spec.getTraits(), [])

  def testAddToFood(self): 
    self.spec.addToFood(6)
    self.assertEqual(self.spec.getFood(), 6)

  def testSetAndGetFatFood(self): 
    self.spec.setFatFood(1)
    self.assertEqual(self.spec.getFatFood(), 1)

  def testAddToFatFood(self): 
    self.spec.addToFatFood(1)
    self.assertEqual(self.spec.getFatFood(), 1)

  def testHasTrait(self): 
    self.spec.setTraits([trait.Trait.symbiosis])
    self.assertTrue(self.spec.hasTrait(trait.Trait.symbiosis))

  def testMoveFatFood(self): 
    self.spec.setTraits([trait.Trait.fat_tissue])
    self.spec.addToFood(6)
    self.spec.addToFatFood(7)
    self.spec.moveFatFood()
    self.assertEqual(self.spec.getFatFood(), 7)
    self.assertEqual(self.spec.getFood(), 6)
  
  def testMoveFatFood2(self): 
    self.spec.setTraits([trait.Trait.fat_tissue])
    self.spec.addToFood(2)
    self.spec.addToFatFood(7)
    self.spec.moveFatFood()
    self.assertEqual(self.spec.getFatFood(), 3)
    self.assertEqual(self.spec.getFood(), 6)

  def testMoveFatFood3(self): 
    self.spec.setTraits([trait.Trait.fat_tissue])
    self.spec.addToFatFood(6)
    self.spec.moveFatFood()
    self.assertEqual(self.spec.getFatFood(), 0)
    self.assertEqual(self.spec.getFood(), 6)
	

if __name__ == '__main__':
    unittest.main()




