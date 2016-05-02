# unit tests for the Player in Evolution
import unittest, os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
import dealer
import species
import trait
import inPlayer
import trait_card

class TestPlayer(unittest.TestCase):
	def setUp(self):
		self.player = inPlayer.Player(1, [], 0)

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

		self.opponent1 = inPlayer.Player(2, [], 0)
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
		self.assertEqual(self.player.feedNext(4, self.opponents), 0)

	def testSimpleCarnivore(self):
		self.player.setSpeciesBoards([self.carnivore])
		self.assertEqual(self.player.feedNext(4, self.opponents), [0, 0, 1])

	def testSimpleFatTissue(self):
		self.player.setSpeciesBoards([self.fat_tissue, self.fat_tissue2])
		self.assertEqual(self.player.feedNext(4, self.opponents), [1, 3])

	def testSimpleEmpty(self):
		self.assertEqual(self.player.feedNext(4, self.opponents), None)

	def testSimpleFull(self):
		self.carnivore.setFood(1)
		self.herbavore.setFood(1)
		self.player.setSpeciesBoards([self.herbavore, self.carnivore])
		self.assertEqual(self.player.feedNext(4, self.opponents), None)

	def testImpossibleCarnivoreAttack(self):
		self.player.setSpeciesBoards([self.carnivore])
		self.opponent1.setSpeciesBoards([self.opfatherb])
		self.assertEqual(self.player.feedNext(4, self.opponents), [0, 0, 1])

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

	def testGetHungrySpeciesIndexes(self):
		self.player.setSpeciesBoards([self.herbavore, self.herbavore4, self.herbavore3, self.herbavore2])
		result = self.player.getHungrySpeciesIndexes()
		self.assertEqual(result, [0, 3])

	def testGetSpeciesByIndex(self):
		self.player.setSpeciesBoards([self.herbavore, self.herbavore4, self.herbavore3, self.herbavore2])
		result = self.player.getSpeciesByIndex(0)
		self.assertEqual(result, self.herbavore)

	def testRemoveSpeciesInLOS(self):
		self.player.setSpeciesBoards([self.herbavore, self.herbavore4, self.herbavore3, self.herbavore2])
		self.player.removeSpeciesInLOS(0)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore4, self.herbavore3, self.herbavore2])

	def testAddSpecies(self):
		self.player.addToHand([self.fertileCard])
		discarded = self.player.addSpecies(self.herbavore, [0])

		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore])
		self.assertEqual(self.player.getHand(), [self.fertileCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(discarded, [self.fertileCard])

	def testAddSpecies1(self):
		self.player.addToHand([self.fertileCard, self.climbingCard])
		discarded = self.player.addSpecies(self.herbavore, [0])

		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(discarded, [self.fertileCard])

	def testAddSpecies2(self):
		self.player.addToHand([self.fertileCard, self.climbingCard])
		discarded = self.player.addSpecies(self.herbavore, [0, 1])

		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard])
		self.assertEqual(self.herbavore.getTraits(), [trait.Trait.climbing])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(discarded, [self.fertileCard, self.climbingCard])

	def testAddSpecies3(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		discarded = self.player.addSpecies(self.herbavore, [2, 3, 0, 4])

		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [trait.Trait.cooperation, trait.Trait.fertile, trait.Trait.long_neck])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(discarded, [self.carnivoreCard, self.cooperationCard, self.fertileCard, self.longNeckCard])


	def testReplaceTrait(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits])
		discarded = self.player.replaceTrait(1, 1, 0)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.fertile, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)
		self.assertEqual(discarded, self.fertileCard)

	def testGrow(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits])
		discarded = self.player.grow(1, 4, self.player.increaseSpeciesPopulation)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 2)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)
		self.assertEqual(discarded, self.longNeckCard)

	def testGrow1(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits])
		discarded = self.player.grow(1, 4, self.player.increaseSpeciesBody)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 1)
		self.assertEqual(discarded, self.longNeckCard)

	def testApplyList(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		discarded = self.player.apply_list([[0, 1], [1, 2], [2, 0]], self.player.increaseSpeciesBody)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 2)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 1)
		self.assertEqual(self.fat_tissue.getTraits(), [trait.Trait.fat_tissue])
		self.assertEqual(self.fat_tissue.getFood(), 0)
		self.assertEqual(self.fat_tissue.getPopulation(), 1)
		self.assertEqual(self.fat_tissue.getBodySize(), 2)
		self.assertEqual(discarded, [self.climbingCard, self.carnivoreCard, self.fertileCard])

	def testApplyList1(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		discarded = self.player.apply_list([[0, 1], [1, 2], [2, 0]], self.player.increaseSpeciesPopulation)
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 2)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 2)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)
		self.assertEqual(self.fat_tissue.getTraits(), [trait.Trait.fat_tissue])
		self.assertEqual(self.fat_tissue.getFood(), 0)
		self.assertEqual(self.fat_tissue.getPopulation(), 2)
		self.assertEqual(self.fat_tissue.getBodySize(), 1)
		self.assertEqual(discarded, [self.climbingCard, self.carnivoreCard, self.fertileCard])

	def testApplyRTList(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		discarded = self.player.apply_rt_list([[2, 0, 2], [1, 2, 1]])
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.climbing])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)
		self.assertEqual(self.fat_tissue.getTraits(), [trait.Trait.carnivore])
		self.assertEqual(self.fat_tissue.getFood(), 0)
		self.assertEqual(self.fat_tissue.getPopulation(), 1)
		self.assertEqual(self.fat_tissue.getBodySize(), 1)
		self.assertEqual(discarded, [self.carnivoreCard, self.climbingCard])


	def testApplyAction(self):
		self.player.addToHand([self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		discarded = self.player.apply_action([[[0, 0]],
												[[0, 3], [2, 4]],
												[[2, 0, 2], [1, 2, 1]]])
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue])
		self.assertEqual(self.player.getHand(), [self.fertileCard, self.climbingCard, self.carnivoreCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 2)
		self.assertEqual(self.herbavore.getBodySize(), 2)
		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.climbing])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)
		self.assertEqual(self.fat_tissue.getTraits(), [trait.Trait.carnivore])
		self.assertEqual(self.fat_tissue.getFood(), 0)
		self.assertEqual(self.fat_tissue.getPopulation(), 1)
		self.assertEqual(self.fat_tissue.getBodySize(), 2)
		self.assertEqual(discarded, [self.carnivoreCard, self.climbingCard, self.fertileCard, self.cooperationCard, self.longNeckCard])

	def testMoveFatToFood(self):
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2])
		self.fat_tissue2.addToFatFood(2)
		self.fat_tissue.addToFatFood(1)
		self.player.moveFatToFood()
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2])
		self.assertEqual(self.player.getHand(), [])

		self.assertEqual(self.herbavore.getTraits(), [])
		self.assertEqual(self.herbavore.getFood(), 0)
		self.assertEqual(self.herbavore.getPopulation(), 1)
		self.assertEqual(self.herbavore.getBodySize(), 1)

		self.assertEqual(self.speciesWith3Traits.getTraits(), [trait.Trait.cooperation, trait.Trait.burrowing, trait.Trait.ambush])
		self.assertEqual(self.speciesWith3Traits.getFood(), 0)
		self.assertEqual(self.speciesWith3Traits.getPopulation(), 1)
		self.assertEqual(self.speciesWith3Traits.getBodySize(), 0)

		self.assertEqual(self.fat_tissue.getTraits(), [trait.Trait.fat_tissue])
		self.assertEqual(self.fat_tissue.getFood(), 1)
		self.assertEqual(self.fat_tissue.getPopulation(), 1)
		self.assertEqual(self.fat_tissue.getBodySize(), 1)
		self.assertEqual(self.fat_tissue.getFatFood(), 0)

		self.assertEqual(self.fat_tissue2.getTraits(), [trait.Trait.fat_tissue])
		self.assertEqual(self.fat_tissue2.getFood(), 1)
		self.assertEqual(self.fat_tissue2.getPopulation(), 1)
		self.assertEqual(self.fat_tissue2.getBodySize(), 3)
		self.assertEqual(self.fat_tissue2.getFatFood(), 1)

	def testChoose1(self):
		self.player.start(1, False, [self.fertileCard, self.climbingCard, self.cooperationCard])
		self.assertEqual(self.player.getSpeciesBoards(), [])
		self.assertEqual(len(self.player.getHand()), 3)
		chosen =  self.player.choose([[], []])
		self.assertEqual(chosen, [1, [], [], [[2, 0]], []])

	def testChoose2(self):
		self.player.start(1, False, [self.fertileCard, self.climbingCard, self.cooperationCard, self.longNeckCard, self.carnivoreCard, self.ambushCard])
		chosen =  self.player.choose([[], []])
		self.assertEqual(chosen, [5, [[0, 2]], [[0, 0]], [[4, 1]], [[0, 0, 3]]])

	def testStart(self):
		self.player.setHand([self.fertileCard, self.carnivoreCard, self.ambushCard])
		self.player.setSpeciesBoards([self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2])

		self.player.start(9, self.herbavore2, [self.climbingCard, self.cooperationCard, self.longNeckCard])

		self.assertEqual(self.player.getHand(), [self.fertileCard, self.carnivoreCard, self.ambushCard, self.climbingCard, self.cooperationCard, self.longNeckCard])
		self.assertEqual(self.player.getSpeciesBoards(), [self.herbavore, self.speciesWith3Traits, self.fat_tissue, self.fat_tissue2, self.herbavore2])


if __name__ == '__main__':
	unittest.main()
