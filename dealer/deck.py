import random


import trait
import trait_card


NUMCARNIVORECARDS = 17
CARNIVOREFOODNUMMAX = 8
CARNIVOREFOODNUMMIN = -8

NUMEACHREG = 7
REGFOODNUMMIN = -3
REGFOODNUMMAX = 3

def generateDeck():
  """
  generates a random deck of trait cards for the game
  """
  carnivoreCards = []
  nonCarnivores = []

  for i in range(NUMCARNIVORECARDS):
    carnivoreCards.append(trait_card.TraitCard(trait.Trait.carnivore, random.randint(CARNIVOREFOODNUMMIN, CARNIVOREFOODNUMMAX)))

  for t in list(trait.Trait):
    if not (t is trait.Trait.carnivore):
      for i in range(NUMEACHREG):
        nonCarnivores.append(trait_card.TraitCard(t, random.randint(REGFOODNUMMIN, REGFOODNUMMAX)))

  carnivoreCards.extend(nonCarnivores)
  generatedDeck = sorted(carnivoreCards, cmp = compareTraitCard, reverse = True)
  return generatedDeck

def compareTraitCard(card1, card2):
  """
  compares the trait cards
  :param card1: TraitCard
  :param card2: TraitCard
  :return: boolean
  """
  trait_card1 = card1.getTrait().value
  trait_card2 = card2.getTrait().value

  if trait_card1 > trait_card2:
    return -1
  elif trait_card1 < trait_card2:
    return 1
  else:
    if card1.getFoodPoints() < card2.getFoodPoints():
      return 1
    elif card1.getFoodPoints() > card2.getFoodPoints():
      return -1
    else:
      return 0

