# A Species (Species board) for the game Evolution

from trait import Trait
from random import randint
from validate import validatePositive, validateRange_1_7, validateTrait, validateRange_0_7

MAXTRAITS = 3
HARDSHELLLARGER = 3

class Species:
	food = 0
	population = 1
	bodysize = 0
	traits = []
	fat_food = 0

	def __init__(self, food, bodysize, population, traits):
		"""
		Initializes a species with the given food, bodysize, population, and traits
		:param food: int
		:param bodysize: int
		:param population: int
		:param traits: [TraitCard, ...]
		"""
		self.food = food
		if validateRange_1_7(population):
			self.population = population
		if validateRange_0_7(bodysize):
			self.bodysize = bodysize
		self.fat_food = 0
		self.traits = []
		for t in traits:
			if validateTrait(t):
				self.traits.append(t)


	def getFood(self):
		"""
		Get the number of food tokens of this species.
		:return: int
		"""
		return self.food

	def setFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		if validatePositive(nat):
			self.food = nat
		else:
			return False

	def addToFood(self, nat):
		"""
		Update the number of food tokens for this species.
		:param nat: int
		"""
		newFood = self.food + nat
		if validatePositive(nat):
			self.food = newFood

	def getFatFood(self):
		"""
		Get the number of fat_food tokens of this species.
		:return: int
		"""
		return self.fat_food

	def setFatFood(self, nat):
		"""
		Update the number of fat_food tokens for this species.
		:param nat: int
		"""
		if validatePositive(nat):
			self.fat_food = nat

	def addToFatFood(self, nat):
		"""
		Update the number of fat_food tokens for this species.
		:param nat: int
		"""
		newFood = self.fat_food + nat
		if validatePositive(nat):
			self.fat_food = newFood

	def addToPopulation(self, amount):
		newPop = self.getPopulation() + amount
		if validateRange_1_7(newPop):
				self.setPopulation(newPop)


	def addToBody(self, amount):
		newBody = self.getBodySize() + amount
		if validateRange_1_7(newBody):
			self.setBodySize(newBody)

	def isHungryForFood(self):
		"""
		checks if this species needs to be fed food
		:return: boolean
		"""
		return (self.getFood() < self.getPopulation())

	def isHungryForFat(self):
		"""
		checks if this species needs to store fat
		:return: boolean
		"""
		return  (self.hasTrait(Trait.fat_tissue) and (self.getFatFood() < self.getBodySize()))

	def isHungry(self):
		"""
		checks if this species needs to be fed
		:return: boolean
		"""
		return self.isHungryForFat() or self.isHungryForFood()

	def maximumFeed(self, is_fat):
		"""
		returns the maximum amount of "food" this species can take
		:param is_fat: boolean which indicates whether this is a fat food feeding
		:return: int
		"""
		maximum = (self.getBodySize() - self.getFatFood()) if is_fat else (self.getPopulation() - self.getFood())
		return maximum

	def getPopulation(self):
		"""
		Get the current population size for this species.
		:return: int
		"""
		return self.population

	def setPopulation(self, nat):
		"""
		Update the population size of this species.
		:param nat: int
		"""
		if validateRange_1_7(nat):
			self.population = nat

		return validateRange_1_7(nat)


	def reducePopulation(self, nat):
		"""
		Decreases the size of the population by the given number
		:pram nat: int
		"""
		newPop = self.population - nat
		if newPop < self.getFood():
		    self.setFood(newPop)
		return self.setPopulation(newPop)

	def starve(self):
		"""
		makes the population of this species equal to the amount of food consumed
		"""
		return self.setPopulation(self.getFood())


	def getBodySize(self):
		"""
		Get the current body size of this species.
		"""
		return self.bodysize

	def setBodySize(self, nat):
		"""
		Update the body size of this species.
		:param nat: int
		"""
		if validateRange_1_7(nat):
			self.bodysize = nat

	def getTraits(self):
		return self.traits

	def discardTrait(self, index):
		"""
		Choose a trait in the current set of self.traits to discard.
		:param index: int
		"""
		if index > len(self.traits):
			raise Exception("Not a valid index for traits")
		self.traits.pop(index)

	def setTraits(self, lot):
		"""
		Update the set of Traits this species has.
		:param lot: [Trait, ...]
		"""
		for trait in lot:
			if len(self.traits) < MAXTRAITS:
				self.traits.append(trait)
			else:
				#for now, FIFO
				self.discardTrait(0)
				self.traits.append(trait)

	def addTrait(self, t):
		"""
		adds a trait to this species traits
		:param t: Trait
		"""
		if len(self.getTraits()) < MAXTRAITS:
			self.getTraits().append(t)

		else:
			raise ValueError("cannot add more traits")

	def replaceTrait(self, index_trait, t):
		"""
		replaces the trait at the given index with the given trait
		:param index_trait: int
		:param t: Trait
		"""
		self.getTraits()[index_trait] = t
		if not self.hasTrait(Trait.fat_tissue):
			self.setFatFood(0)

	def hasTrait(self, t):
		"""
		checks if the species has the given trait
		:param t: Trait
		:return: boolean
		"""
		return (t in self.getTraits())

	def moveFatFood(self):
		"""
		moves the fat food to food. This species must be a fat_tissue species
		"""
		if (self.fat_food <= self.maximumFeed(False)):
			amountToFeed = self.fat_food
		else:
			amountToFeed = self.maximumFeed(False)
		self.food += amountToFeed
		self.fat_food = self.fat_food - amountToFeed

	def neighborsHelp(self, neighborLeft, neighborRight):
		"""
		Checks if a Species' neighbors can help prevent an attack
		:param neighborLeft: a Species
		:param neighborRight: a Species that is not NeighborLeft
		:return: Boolean
		"""
		for neighbor in [neighborLeft, neighborRight]:
			if neighbor:
				if Trait.warning_call in neighbor.traits:
					return True
		return False

	def canBurrow(self):
		"""
		Returns whether a defender can successfully use burrowing
		:param attacker: a Species with the carnivore trait
		:param defender: a species that is not the attacker
		:return: Boolean
		"""
		return  self.getFood() == self.getPopulation()

	def goodSymbiosis(self, neighborRight):
		"""
		Returns whether symbiosis helps the defender avoid attack, ie:
		if the neighbor to their right has a larger body size then the defender
		:param attacker: a Species with the carnivore trait
		:param defender: a species that is not the attacker
		:return: Boolean
		"""
		if neighborRight:
			return self.getBodySize() < neighborRight.getBodySize()
		return False

	def blockingShell(self, attacker):
		"""
		Returns whether a defender with hard_shell can defend against their attacker
		:param attacker: a Species with the carnivore trait
		:param defender: a species that is not the attacker
		:return: Boolean
		"""
		if attacker.hasTrait(Trait.pack_hunting):
			return (self.getBodySize() + HARDSHELLLARGER) >= (attacker.getBodySize() + attacker.getPopulation())
		else:
			return (attacker.getBodySize() - self.getBodySize()) <= HARDSHELLLARGER

	def herdingHelp(self, attacker):
		"""
		Returns whether a defender with herding can successfully block an attacker
		:param attacker: a Species with the carnivore trait
		:param defender: a Species not the attacker
		:return: Boolean
		"""
	 	return attacker.getPopulation() <= self.getPopulation()


	def canTheAttackerAttack(self, attacker, neighborLeft, neighborRight):
		"""
		checks if the attacker can attack this species
		:param attacker: Species
		:param neighborLeft: Species or False
		:param neighborRight: Species or False
		:return: Boolean
		"""
		neighborCanHelpDefender = (not attacker.hasTrait(Trait.ambush)) and (self.neighborsHelp(neighborLeft, neighborRight))
		climbingCanHelpDefender = (not attacker.hasTrait(Trait.climbing)) and (self.hasTrait(Trait.climbing))
		borrowingCanHelpDefender = (self.hasTrait(Trait.burrowing)) and self.canBurrow()
		symbiosisCanHelpDefender = (self.hasTrait(Trait.symbiosis)) and self.goodSymbiosis(neighborRight)
		hard_shellCanHelpDefender = (self.hasTrait(Trait.hard_shell)) and self.blockingShell(attacker)
		herdingCanHelpDefender = (self.hasTrait(Trait.herding)) and self.herdingHelp(attacker)

		canDefend = [neighborCanHelpDefender, climbingCanHelpDefender, borrowingCanHelpDefender,
					 symbiosisCanHelpDefender, hard_shellCanHelpDefender, herdingCanHelpDefender]

		return not any(canDefend)

	def attackable(self, attacker, neighborLeft, neighborRight):
		"""
		checks to see if this species can be attacked based on the situation
		:param attacker: Species
		:param neighborLeft: Species or False
		:param neighborRight: Species or False
		:return: boolean
		"""
		if attacker.hasTrait(Trait.carnivore):
			if attacker is self:
				raise Exception("A species cannot attack itself")
			return self.canTheAttackerAttack(attacker, neighborLeft, neighborRight)
		else:
			raise Exception("Attacking Species must be a carnivore")


	def display_species(self):
		"""
		returns a string representation of this species
		:return: String
		"""
		f = self.getFood()
		b = self.getBodySize()
		p = self.getPopulation()
		this_traits = self.getTraits()
		ff = self.getFatFood()
		traits_s = map(lambda t: t.value, this_traits)
		traits_str = ", ".join(traits_s)

		if ff:
			label_text = "food: " + str(f) + ", body size: "+ str(b) + ", population: " + str(p) + ", fat food: " + str(ff) + ", traits: [" + traits_str + "]"
		else:
			label_text = "food: " + str(f) + ", body size: "+ str(b) + ", population: " + str(p) + ", traits: [" + traits_str + "]"


		return "species: " + label_text
