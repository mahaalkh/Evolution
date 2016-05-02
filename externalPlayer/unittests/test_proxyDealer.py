
import json, sys, os, unittest
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from  proxyDealer import ProxyDealer

sys.path.insert(0, os.path.join(this_package_path, '../../dealer'))
from trait import Trait
from trait_card import TraitCard
from species import Species
from processing import process_output


class TestProxyDealer(unittest.TestCase):
  def setUp(self):
    self.pDealer = ProxyDealer()

    self.card1 = TraitCard(Trait.ambush, -2)
    self.card2 = TraitCard(Trait.carnivore, -8)
    self.card3 = TraitCard(Trait.ambush, 0)

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

  def tearDown(self):
    del self.pDealer

  def testNew(self):
    pass

  def testStart(self):
    self.pDealer.new("TODO")
    self.pDealer.start(json.dumps([12,
                                    [[["food",2],
                                          ["body",2],
                                          ["population",2],
                                          ["traits",["carnivore"]]]],
                                    [[2, "long-neck"]]]))
    self.assertEqual(self.pDealer.getExternalPlayer().getFoodBag(), 12)
    self.assertEqual(len(self.pDealer.getExternalPlayer().getSpeciesBoards()), 1)
    self.assertEqual(self.pDealer.getExternalPlayer().getSpeciesBoards()[0].getFood(), 2)
    self.assertEqual(self.pDealer.getExternalPlayer().getSpeciesBoards()[0].getPopulation(), 2)
    self.assertEqual(self.pDealer.getExternalPlayer().getSpeciesBoards()[0].getBodySize(), 2)
    self.assertEqual(len(self.pDealer.getExternalPlayer().getSpeciesBoards()[0].getTraits()), 1)
    self.assertEqual(self.pDealer.getExternalPlayer().getSpeciesBoards()[0].getTraits()[0], Trait.carnivore)
    self.assertEqual(len(self.pDealer.getExternalPlayer().getHand()), 1)
    self.assertEqual(self.pDealer.getExternalPlayer().getHand()[0].getFoodPoints(), 2)
    self.assertEqual(self.pDealer.getExternalPlayer().getHand()[0].getTrait(), Trait.long_neck)

  def testChoose(self):
    self.pDealer.new("TODO")
    self.pDealer.start(json.dumps([12,
                                    process_output.make_los_json([self.species1, self.speciescarni1, self.speciesfat]),
                                    process_output.make_loc_json([self.card1, self.card2, self.card3])]))
    action4 = self.pDealer.choose(json.dumps([[], []]))
    self.assertEqual(action4, json.dumps([0, [],[], [[2, 1]], []]))

  def testFeedNext(self):
    self.pDealer.new("TODO")
    feeding = self.pDealer.feedNext(json.dumps([12,
                                   process_output.make_los_json([self.species1, self.speciescarni1, self.speciesfat]),
                                   process_output.make_loc_json([self.card1, self.card2, self.card3]),
                                   9,
                                   process_output.make_lolos_json([[self.speciesfull1], [self.specieshorns1], [self.species2]])
                                   ]))
    self.assertEqual(feeding, json.dumps([2, 2]))

    self.assertEqual(self.pDealer.getExternalPlayer().getFoodBag(), 12)
    self.assertEqual(len(self.pDealer.getExternalPlayer().getSpeciesBoards()), 3)


if __name__ == '__main__':
    unittest.main()


