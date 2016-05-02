#Representation of the external player object for the Evolution game

import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../dealer/'))

import trait
import species
import strategy
import deck

IS_FAT = True
class SillyPlayer:
  species_boards = []
  food_bag = 0
  hand = []
  player_id = 0
  strat = None

  def __init__(self, ident, loSpeciesBoard, bag):
    """
    Initializes a player with a given id, list of species boards, and food bag
    :param ident: int
    :param loSpeciesBoard: list of Species
    :param bag: int greater than 0
    """
    self.species_boards = loSpeciesBoard
    self.food_bag = bag
    self.hand = []
    self.player_id = ident
    self.strat = strategy.Strategy()

  def setSpeciesBoards(self, loSpeciesBoard):
    """
    sets the list of species of this player to the given list of species
    :param loSpeciesBoard: [Species, ...]
    """
    self.species_boards = loSpeciesBoard

  def getSpeciesBoards(self):
    """
    gets the list of species of this player
    :return: [Species, ...]
    """
    return self.species_boards

  def addSpeciesBoard(self, board):
    """
    adds the species board to the player list of species
    :board: Species
    """
    self.species_boards.append(board)

  def setFoodBag(self, fb):
    """
    sets the food bag of the player to the given value
    :param fb: int
    """
    self.food_bag = fb

  def getFoodBag(self):
    """
    gets the food bag of this player
    :return: int
    """
    return self.food_bag

  def addToFoodBag(self, tokens):
    """
    adds points (tokens) to the food bag
    :param tokens: int
    """
    self.food_bag += tokens

  def setHand(self, cards):
    """
    sets the hand of the player to the given cards
    :param cards: [TraitCard, ...]
    """
    self.hand = cards

  def getHand(self):
    """
    gets the hand of the player
    :return: [TraitCard, ...]
    """
    return self.hand

  def addToHand(self, cards):
    """
    adds the given cards to this player's hand
    :param cards: [TraitCard, ...]
    """
    self.hand.extend(cards)

  def giveCard(self, i, sortedHand):
    """
    returns the card at the given index & deletes the card
    :param i: int that represents an index of a card in the players hand
    """
    card = sortedHand[i]
    indexCard = self.getHand().index(card)
    return card

  def removeCardsFromList(self, loc, lst):
    """
    removes a the cards from the given list
    :param loc: [TraitCard, ...]
    """
    for card in loc:
      lst.remove(card)

  def setPlayerId(self, ident):
    """
    sets the id of this player to the given ident
    """
    self.player_id = ident

  def getPlayerId(self):
    """
    gets the player's id
    :return: int
    """
    return self.player_id


  def setPlayerState(self, playerState):
    """
    sets the field of this player based on the given information in the playerState
    :param playerState: [int, [Species, ...], [TraitCard, ...]]
    """
    self.setFoodBag(playerState[0])
    self.setSpeciesBoards(playerState[1])
    self.setHand(playerState[2])

  def start(self, t):
    """
    initializes this player with t
    :param t: [int, int, [Species, ...], [TraitCard, ...]]
    """
    wh, b, s, tc = t
    state = [b, s, tc]
    self.setPlayerState(state)

  def choose(self, lolosB, lolosA):
    """
    chooses what to exchange the cards for
    :param loloB: [[Species, ...], ...]
    :param loloA: [[Species, ...], ...]
    :param playerState: [int, [TraitCard, ...], [Species]]
    :return: Action4
    """

    cardToRemove = []

    sortedHand = sorted(self.getHand(), cmp = deck.compareTraitCard, reverse = True)
    foodCardIndex = self.getHand().index(sortedHand[0])
    cardToRemove.append(self.giveCard(0, sortedHand))
    bt = [self.getHand().index(sortedHand[1]), self.getHand().index(sortedHand[2])]
    cardToRemove.append(self.giveCard(1, sortedHand))
    cardToRemove.append(self.giveCard(2, sortedHand))

    logp, logb, lort = [[], [], []]

    i = 3
    lenList = len(sortedHand)-3
    while (lenList and i<6):
      if(i == 3):
        logp.append([len(self.getSpeciesBoards()), self.getHand().index(sortedHand[i])])
        cardToRemove.append(self.giveCard(i, sortedHand))
      elif (i==4):
        logb.append([len(self.getSpeciesBoards()), self.getHand().index(sortedHand[i])])
        cardToRemove.append(self.giveCard(i, sortedHand))
      elif (i==5):
        lort.append([len(self.getSpeciesBoards()), 0, self.getHand().index(sortedHand[i])])
        cardToRemove.append(self.giveCard(i, sortedHand))
      i+=1
      lenList-=1
    return [foodCardIndex, logp, logb, [bt], lort]

  def feedNext(self, wateringHole, lolos, playerState):
    """
    chooses which species to feed next
    :param wateringHole: int
    :param lolos: [[Species, ...], ...]
    :param playerState: [int, [Species, ...], [TraitCard, ...]]
    :return: one of
                -False (if a player can't feed any species)
                -the index of a species in self.species_boards,
                -[the index of a species in self.species_boards with the trait fat_tissue, Nat]
                -[the index of a species in self.species_boards with the trait carnivore,
                    the index of the player in the given list of players,
                    and the index of an attackable species owned by the prior player]
    """
    self.setPlayerState(playerState)

    chosen, trait = self.strat.feedNext(self.getSpeciesBoards())
    ichosen = self.getSpeciesBoards().index(chosen)

    if (not trait):
      return ichosen
    elif (trait.carnivore is trait):
      victim = self.strat.carnivoreFeeding(self.getSpeciesBoards(), lolos)
      if (not victim):
        return False
      else:
        iplay, iboard, chosen = victim
        ichosen = self.getSpeciesBoards().index(chosen)
        return [ichosen, iplay, iboard]
    else:
      return [ichosen, min(wateringHole, self.strat.ammountFeedFat(chosen))]




