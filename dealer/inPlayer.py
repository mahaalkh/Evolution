#Representation of the player object for the Evolution game
import trait
import species
import deck
import validate

import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../externalPlayer/'))

from sillyPlayer import SillyPlayer

IS_FAT = True
class Player:
  species_boards = []
  food_bag = 0
  hand = []
  player_id = 0
  externalPlayer = None

  def __init__(self, ident, loSpeciesBoard, bag, externalPlayer = None, info = None):
    """
    Initializes a player with a given id, list of species boards, and food bag
    :param ident: int
    :param loSpeciesBoard: list of Species
    :param bag: int greater than 0
    :param externalPlayer: a an extenal player (SillyPlayer or ProxyPlayer)
    :param info: String
    """
    self.species_boards = loSpeciesBoard
    self.food_bag = bag
    self.hand = []
    self.player_id = ident
    if externalPlayer:
      self.externalPlayer = externalPlayer
    else:
      self.externalPlayer = SillyPlayer(1, [], 0)
    if info:
      self.info = info
    else:
      self.info = ""

  def getInfo(self):
    """
    gets the info field in this player 
    :return: String
    """
    return self.info

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

  def getExternalPlayer(self):
    """
    get the external player of this internal player 
    :return: SillyPlayer or ProxyPlayer
    """
    return self.externalPlayer

  def addToHand(self, cards):
    """
    adds the given cards to this player's hand
    :param cards: [TraitCard, ...]
    """
    self.hand.extend(cards)

  def giveCard(self, i):
    """
    returns the card at the given index & deletes the card
    :param i: int that represents an index of a card in the players hand
    :return: TraitCard
    """
    if i in range(len(self.getHand())):
        card = self.getHand()[i]
    else:
	     card = self.getHand()[len(self.getHand())-1]
    return card

  def removeCardsFromHand(self, loc):
    """
    removes a the cards from this player's hand
    :param loc: [TraitCard, ...]
    :effect: modifies this player's hand
    """
    for card in loc:
      	if card in self.getHand():
      		self.getHand().remove(card)


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


  def getSpeciesByIndex(self, i):
    """
    gets the species from the players list of species by index
    :param i: int
    :return: Species
    """
    return self.species_boards[i]

  def moveFatToFood(self):
    """
    Moves the fat from the fat food species to food
    """
    for animal in self.getSpeciesBoards():
      if animal.hasTrait(trait.Trait.fat_tissue):
        animal.moveFatFood()

  def removeSpeciesInLOS(self, species_index):
    """
    removes the species from the list of species in this player
    :param species: int which is the index of the species in the player species
    """
    species = self.getSpeciesByIndex(species_index)
    self.species_boards.remove(species)

  def getHungrySpeciesIndexes(self):
    """
    gets the hungry species of this player
    :return: [int, ...] which represents the indexes of the hungry species
    """
    player_species = self.getSpeciesBoards()
    hungry_species_indexes = []
    for i in range(len(player_species)):
      if player_species[i].isHungry():
        hungry_species_indexes.append(i)
    return hungry_species_indexes

  def increaseSpeciesPopulation(self, species_index, amount):
    """
    increased the population of the species at the given index
    :param species_index: int
    """
    species = self.getSpeciesByIndex(species_index)
    species.addToPopulation(amount)

  def increaseSpeciesBody(self, species_index, amount):
    """
    increased the population of the species at the given index
    :param species_index: int
    """
    species = self.getSpeciesByIndex(species_index)
    species.addToBody(amount)

  def reduceSpeciesPopulation(self, species_index, amount):
    """
    reduces the population of the species at the given index by the given ammount
    :param species_index: an int representing the index of one of this player's species
    :param amount: an int less then the population of the given species
    :return: Boolean
    """
    species = self.getSpeciesByIndex(species_index)
    return species.reducePopulation(amount)

  def starveSpecies(self):
    """
    makes the player's species have the population equal to the amount of food the species consumed
    :return: int 
    """
    deletedSpecies = 0
    for sp in self.getSpeciesBoards():
      if not sp.starve():
        self.getSpeciesBoards().remove(sp)
        deletedSpecies += 1
    return deletedSpecies

  def moveFoodToBag(self):
    """
    moves the food from the species to the player's food bag
    """
    food = 0
    for sp in self.getSpeciesBoards():
      food += sp.getFood()
      sp.setFood(0)
    self.setFoodBag(food)

  def addSpecies(self, species, bt):
    """
    Adds the traits to the given species and appends that species to the end of the species list
    :param species: a species board
    :param bt: a list of indexes corresponding to trait cards in this player's hand
    :return: [TraitCard, ...]
    """
    cards_to_discard = []
    card = self.giveCard(bt[0])
    cards_to_discard.append(card)
    for index_card in bt[1:]:
      card2 = self.giveCard(index_card)
      trait_to_add = card2.getTrait()
      species.addTrait(trait_to_add)
      cards_to_discard.append(card2)
    self.addSpeciesBoard(species)
    return cards_to_discard

  def replaceTrait(self, species_index, trait_index, card_index):
    """
    replaces the trait of the species with the given
    :param species_index: int
    :param trait_index: int
    :param card_index: int
    :return: TraitCard
    """
    species = self.getSpeciesByIndex(species_index)
    card = self.giveCard(card_index)
    trait_changed = card.getTrait()
    species.replaceTrait(trait_index, trait_changed)
    return card

  def grow(self, species_index, card_index, funct):
    """
    applies the given function on the species index
    :param species_index: int
    :param card_index: int
    :param funct: a function that takes in 2 numbers
    :return: TraitCard
    """
    card = self.giveCard(card_index)
    funct(species_index, 1)
    return card

  def apply_list(self, applylist, funct2):
    """
    adds the _ of the given species and discards the appropraite card
    :param applylist: [[String, int, int], ...]
    where the first is the index of species the second the index of the card
    :param funct2: a function that takes in  2 numbers
    :return: [TraitCard, ...]
    """

    cards_to_discard = []
    for g in applylist:
      [index_species, index_card] = g
      card = self.grow(index_species, index_card, funct2)
      cards_to_discard.append(card)

    return cards_to_discard

  def apply_rt_list(self, rt_list):
    """
    replaces the traits for the given species
    :param rt_list: [RT, ...]
    :return: [TraitCard, ...]
    """
    cards_to_discard = []
    for rt in rt_list:
      [species_index, trait_index, card_index] = rt
      card = self.replaceTrait(species_index, trait_index, card_index)
      cards_to_discard.append(card)

    return cards_to_discard

  def apply_action(self, player_action):
    """
    applies the appropriate actions
    :player_action: PlayerAction
    :return: [TraitCard, ...]
    """
    gp_list, gb_list, rt_list = player_action
    cards_to_discard = self.apply_rt_list(rt_list)
    cards_to_discard.extend(self.apply_list(gp_list, self.increaseSpeciesPopulation))
    cards_to_discard.extend(self.apply_list(gb_list, self.increaseSpeciesBody))
    return cards_to_discard

  def canFeed(self):
    """
    Checks if the call to feed follows the sequencing constraints
    throws an error if it doesn't match specs
    Returns: A boolean regarding if this player can feed a species or not
    """
    #checks if there are not enough species boards
    if (len(self.species_boards) != 0):

      #checks if there are an appropraite number of hungry animals
      hunger = False
      for animal in self.species_boards:
        if animal.getPopulation() > animal.getFood():
          hunger = True
        elif (animal.hasTrait(trait.Trait.fat_tissue)
          and (animal.getBodySize() > animal.getFatFood())):
          hunger = True

      return hunger
    return False


  def start(self, w, b, c):
    """
    add the given cards and the species board to the player and then tells the external player about the change
    :param w: int 
    :param b: Species
    :param c: [TraitCard, ...]
    """
    if b:
      self.addSpeciesBoard(b)
    self.addToHand(c)
    t = [w, self.getFoodBag(), self.getSpeciesBoards(), self.getHand()]
    self.externalPlayer.start(t)


  def choose(self, s):
    """
    queries the external player for its choice of using it's cards
    :param s: [[[Species, ...], ...], [[Species, ...], ...]]
    :return: Action4
    """
    action = self.externalPlayer.choose(s[0], s[1])
    if validate.validateAction4(action, self):
      return action
    else:
      return "delete"

  def feedNext(self, wateringHole, lolos):
    """
    queries the external player for its choice of which species to feed next
    :param wateringHole: int
    :param lop: [Player, ...] not containing this player
    :return: one of
      -False (if a player can't feed any species)
      -the index of a species in self.species_boards,
      -[the index of a species in self.species_boards with the trait fat_tissue, Nat]
      -[the index of a species in self.species_boards with the trait carnivore,
          the index of the player in the given list of players,
          and the index of an attackable species owned by the prior player]
    """
    if (not self.canFeed()):
      return None

    feedingChoice = self.externalPlayer.feedNext(wateringHole, lolos, [self.getFoodBag(), self.getSpeciesBoards(), self.getHand()])

    if validate.validateFeedingChoice(feedingChoice, self, lolos, wateringHole):
      return feedingChoice
    else:
      return "delete"


  def calculateScore(self):
    """
    calculates the score of this player
    :return: int
    """
    score = self.getFoodBag()
    for sp in self.getSpeciesBoards():
      score += sp.getPopulation()
      score += len(sp.getTraits())
    return score


  def player_strings(self):
    """
    returns the strings reperesentations of the fields in this player
    :return: [String, [String, ...], [String, ...]]
    """
    this_id = self.getPlayerId()
    this_food_bag = self.getFoodBag()
    this_hand = self.getHand()
    this_species = self.getSpeciesBoards()

    id_food_bag_string = "Player: " + "id: " + str(this_id) + ", food bag: " + str(this_food_bag)

    species_strings = []
    for species in this_species:
       species_strings.append(species.display_species())

    hand_strings = []
    if this_hand:
      for card in this_hand:
        hand_strings.append(card.display_card())

    return [id_food_bag_string, species_strings, hand_strings]

  def sortCards(self):
    sortedHand = sorted(self.getHand(), cmp = deck.compareTraitCard, reverse = True)
    return sortedHand

  


