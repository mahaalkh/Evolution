import os, sys
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, 'dealer/'))

import trait
import species
import sillyPlayer
import compareSpecies

IS_FAT = True
class Strategy:
  def __init__(self):
    pass

  def sortByLex(self, loa, isFat):
    """
    Sorts the given list of fat_tissue animals in lexographical order
    :param loa: list of Species
    :param isFat: boolean which indicates if this is a fat food comparison
    :return: a list of Species containing all the same species as the given loa, of the same length as loa
    """
    sloa = []
    if(len(loa) == 0):
      return loa
    sloa.append(loa[0])

    for animal in loa[1:]:
      for board in sloa:
	compared = compareSpecies.whichCaseFatCompare(animal, board) if isFat else compareSpecies.whichCaseFoodCompare(animal, board)
        if (compared == 1) or (compared == 0) or (compared == -1):
          sloa.insert(sloa.index(board), animal)
          break
        elif (sloa.index(board) == (len(sloa) - 1)):
          sloa.append(animal)
          break
    return sloa

  def stereotypeAnimals(self, lob):
    """
      sorts hungry animals into the right catagory (fat_species, carnivore, herbivore)
      :param lob: a list of species
      :return: 3 lists of species of hungery animals the first of which contains only fat_tissue species, the second of which
        contains only carnivore species, and the third of which containing all animals not fitting into the prior two catagories
    """
    fat_species = []
    carnivores = []
    herbivores = []

    for animal in lob:
      if (animal.hasTrait(trait.Trait.fat_tissue)
        and (animal.getFatFood() < animal.getBodySize())):
        fat_species.append(animal)
      elif (animal.getFood() < animal.getPopulation()):
        if (animal.hasTrait(trait.Trait.carnivore)):
          carnivores.append(animal)
        else:
          herbivores.append(animal)
    return (fat_species, carnivores, herbivores)

  def findFattest(self, fat_species, carnivores, herbivores):
    """
      Finds the fattest type of the most prioritized animal that is still hungry
      :param fat_species: lists of Species containing only Species with the fat_tissue trait
      :param carnivores: list of Species containing only Species with the carnivore trait
      :param herbivores: list of Species containing only Species which do not have either the fat_tissue or carnivore traits
      :return: A tuple of the fatest species of the most prioritized species (fat_tissue -> herbivore -> carnivore) and one of Trait.fat_tissue, Trait.carnivore, False
      corresponding to the trait that species posesses.
    """
    if fat_species:
      return (fat_species[0], trait.Trait.fat_tissue)
    elif herbivores:
      return (herbivores[0], False)
    elif carnivores:
      return (carnivores[0], trait.Trait.carnivore)
    else:
      return None

  def feedNext(self, lob):
    """
      Determines the next species that needs to be fed
      :param lob: a list of Species
      :return: A tuple of the fattest hungry species of the most prioritized species (fat_tissue -> herbivore -> carnivore) and one of Trait.fat_tissue, Trait.carnivore, False
      corresponding to the trait that species posesses.
    """
    fat_species = []
    carnivores = []
    herbivores = []
    fat_species, carnivores, herbivores = self.stereotypeAnimals(lob)

    fat_species = self.sortByLex(fat_species, IS_FAT)
    carnivores = self.sortByLex(carnivores, not IS_FAT)
    herbivores = self.sortByLex(herbivores, not IS_FAT)

    return self.findFattest(fat_species, carnivores, herbivores)


  def sortOpponentsSpecies(self, lopb):
    """
      Sorts the opponents species in order of fattest to skinniest
      :param lopb: a list of lists of Species
      :return: a list of lists ordered in lexigraphical order
    """
    sboards = []
    for zoo in lopb:
      sboards.append(self.sortByLex(zoo, not IS_FAT))
    return sboards


  def getNeighbors(self, boards, board):
    """
      Finds the neighbors of the given species
      :param boards: a list of species
      :param board: a Species belonging to the given Player
      :return: a tuple of the left then right neighbors to the given board in the given player
    """

    for species in boards:
      if species is board:
        index = boards.index(species)
        left = False
        right = False
        if index != 0:
          left = boards[index-1]
        if index != (len(boards) - 1):
          right = boards[index+1]
        return (left, right)
    raise Exception("Invalid Input")


  def compileList(self, canAttack, lolob):
    """
    Compiles a list of all the species that the given list of players has and makes those into a tuple of the players index, and the species index
    :param canAttack: a list of Species
    :param lop: a list of players
    :return: a list of tuples of an index in the given lop and an index of a species of one of the players list of species board
    """
    los = []
    for option in canAttack:
      [iplayer, ispecies, chosen] = option
      los.append(lolob[iplayer][ispecies])
    return los

  def mostTasty(self, canAttack, lolob):
    """
    Determines the best species to attack based on the given list
    :param canAttack: list of Species
    :param lop: list of players that have the given species in canAttack
    :return: a species
    """
    los = self.compileList(canAttack, lolob)
    sorted_list = self.sortByLex(los, not IS_FAT)
    victim = sorted_list[0]
    i = los.index(victim)

    return canAttack[i]



  def pickVictim(self, lors, lolob):
    """
    picks a victim for the given carnivore from the list of players' species
    :param lors: a list of species
    :param lolob: a list of lists of SpeciesBoard with a length between 3 and 8 inclusive
    :return: a species belonging to one of the players in the list of players that the carnivore
      can eat, and the player the species belongs to or False
    """

    #sort it in order of size.
    opponents = self.sortOpponentsSpecies(lolob)

    canAttack = []

    for chosen in lors:
      #go down the list until it finds something it can eat
      for i in range(len(opponents)):
        for j in range(len(opponents[i])):
          playerBoards = opponents[i]
          board = opponents[i][j]
          left, right = self.getNeighbors(playerBoards, board)
          if board.attackable(chosen, left, right):
            canAttack.append([i, lolob[i].index(board), chosen])

      if canAttack:
        return self.mostTasty(canAttack, lolob)

    return False

  def carnivoreFeeding(self, specBoards, lolos):
    fat, carni, herb = self.stereotypeAnimals(specBoards)
    carni = self.sortByLex(carni, not IS_FAT)
    return self.pickVictim(carni, lolos)

  def ammountFeedFat(self, chosen):
    return chosen.getBodySize() - chosen.getFatFood()
