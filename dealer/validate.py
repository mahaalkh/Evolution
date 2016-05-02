import trait
INRange = True
def validateTrait(given_trait):
  """
  validates the given trait
  :param given_trait: Trait
  :return: boolean
  """
  if isinstance(given_trait, trait.Trait):
    return True
  else:
    raise ValueError("invalid trait")

def validateCard(given_trait, given_food_points):
  """
  validates the given trait and food points
  :param trait: Trait
  :param food_points: int
  :return: boolean
  """
  if validateTrait(given_trait):
    if ((given_trait is trait.Trait.carnivore) and not ((given_food_points <= 8) or (given_food_points >= -8))
     or not ((given_food_points <= 3) or (given_food_points >= -3))):
        raise ValueError("invalid trait and food_points")
    return True


def validateListOfPlayers(given_listOfPlayers):
  """
  validates the list of players length
  :param given_listOfPlayers: [Player, ...]
  :return: boolean
  """
  len_list = len(given_listOfPlayers)
  if not ((len_list <= 8) or (len_list >= 3)):
    raise ValueError("invalid list of players")
  for player in given_listOfPlayers:
    validatePlayerSpecies(player)
  return True

def validateDeck(deck):
  """
  validates the deck
  :param deck: [TraitCard, ...]
  :return: boolean
  """
  for card in deck:
    validateCard(card.getTrait(), card.getFoodPoints())
  return True

def validatePlayerSpecies(player):
  """
  validates that the species in the player are not extinct
  :param player: Player
  :return: boolean
  """
  species_boards = player.getSpeciesBoards()
  for species in species_boards:
    if species.getPopulation() <= 0:
      raise ValueError("players has extinct species")
  return True

def validatePositive(num):
  """
  validates that the the given number is positive
  :param num: int
  :return: boolean
  """
  if num < 0:
    raise ValueError("Cannot set food to a negative value")
  return True

def validateRange_1_7(num):
  """
  validate that the given number is in the range between 1 and 7
  :param num: int
  :return: boolean
  """
  return not ((num <= 0) or (num > 7))

def validateRange_0_7(num):
  """
  validate that the given number is in the range between 1 and 7
  :param num: int
  :return: boolean
  """
  if (num < 0) or (num > 7):
      raise ValueError("Cannot set population to a negative value or a value greater than 7")
  return True

def validateNatural(n):
  """
  checks that n is a natural number
  :param n: Any
  :return: boolean
  """
  if isinstance(n, int) and (not isinstance(n, bool)):
    return n >= 0
  return False

def formatElement(loA, size, inRange):
  """
  check that the format of the list of growth is correct
  :param loGrowth: [Json, ...]
  :param size: int
  :param inRange: boolean which indicates if the len of loA could be any number from 1 to size
  :return: boolean
  """
  if not isinstance(loA, list):
    return False
  for g in loA:
    if not isinstance(g, list):
      return False
    elif inRange:
      if not len(g) in range(1, size + 1):
        return False
    elif not len(g) == size:
        return False
    for i in g:
      if not validateNatural(i):
        return False

  return True



def formatAction4(action4):
  """
  checks that the format of action4 is correct
  :param action4: Json
  :return: boolean
  """
  try:
    [whCard, logp, logb, lobt, lort] = action4
    validList = [validateNatural(whCard),
                formatElement(logp, 2, not INRange),
                formatElement(logb, 2, not INRange),
                formatElement(lobt, 4, INRange),
                formatElement(lort, 3, not INRange)]
    return all(validList)
  except Exception:
    return False


def formatFeedingChoice(feedingChoice):
  """
  checks if the format of feedingChoice is correct
  :param feedingChoice: Json
  :return: boolean, string
  """
  if (feedingChoice == False) and isinstance(feedingChoice, bool):
    return (True, "bool")

  elif validateNatural(feedingChoice):
    return (True, "int")

  elif formatElement([feedingChoice], 3, INRange):
    return (True, "list")

  return (False, False)


def validateList(lobt, player):
  """
  checks that the lobt is valid
  :param lobt: [[int, ...], ...]
  :param player: Player
  """
  num = 0
  for bt in lobt:
    for i in bt:
      if not (i in range(len(player.getHand()))):
        return (False, False)
    num += 1
  return (True, num)

def validateFatFeeding(feedingChoice, player, wh):
  """
  checks if the fattissue feeding choice is valid
  :param feedingChoice: FeedingChoice
  :param player: Player
  :param wh: int
  :return: bool
  """
  if feedingChoice[0] in range(len(player.getSpeciesBoards())):
    return (feedingChoice[1] in range(wh + 1)) and player.getSpeciesBoards()[feedingChoice[0]].hasTrait(trait.Trait.fat_tissue)
  return False

def  validateCarniFeeding(feedingChoice, player, lolos):
  if feedingChoice[0] in range(len(player.getSpeciesBoards())):
    if feedingChoice[1] in range(len(lolos)):
      return ((feedingChoice[2] in range(len(lolos[feedingChoice[1]])))
              and player.getSpeciesBoards()[feedingChoice[0]].hasTrait(trait.Trait.carnivore))
  return False

def validateFeedingChoice(feedingChoice, player, lolos, wh):
  """
  validates the information in feedingChoice
  :param feedingChoice: feedingChoice
  :param player: Player
  :param lolos: [[Species, ...], ...]
  :param wh: int
  :return: boolean
  """
  format = formatFeedingChoice(feedingChoice)
  if format[0]:
    if format[1] == "int":
      return feedingChoice in range(len(player.getSpeciesBoards()))
    elif format[1] == "list":
      if len(feedingChoice) == 2:
        return validateFatFeeding(feedingChoice, player, wh)
      elif len(feedingChoice) == 3:
        return validateCarniFeeding(feedingChoice, player, lolos)
      else:
        return False

  return format[0]

def validateGrowth(loGrowth, player, extraSp):
  """
  checks if a loGrowth is valid
  :param loGrowth: [G, ...], G is either a GP or a GB
  :param player: Player
  :param extraSp: int
  :return: boolean
  """
  for growth in loGrowth:
    [specIndex, cardIndex] = growth
    if not ((specIndex in range(len(player.getSpeciesBoards())+extraSp)) and (cardIndex in range(len(player.getHand())))):
      return False

  return True


def validateRT(lort, player, extraSp):
  """
  checks that the lort is valid
  :param lort: [RT, ...]
  :param player: Player
  :param extraSp: int
  """
  for rt in lort:
    [specIndex, traitIndex, cardIndex] = rt
    if ((specIndex in range(len(player.getSpeciesBoards()))) and (cardIndex in range(len(player.getHand())))):
      if not (traitIndex in range(len(player.getSpeciesBoards()[specIndex].getTraits()))):
        return False
    elif not ((specIndex in range(len(player.getSpeciesBoards())+extraSp)) and (cardIndex in range(len(player.getHand())))):
      return False

  return True


def validateAction4(action4, player):
  """
  checks that the content and format of action4 is valid
  :param action4: Json
  :param player: Player
  :return: boolean
  """
  if formatAction4(action4):
    [wh, logp, logb, lobt, lort] = action4
    vBT = validateList(lobt, player)
    if vBT[0]:
      numAdd = vBT[1]
      lst =  [wh in range(len(player.getHand())),
              validateGrowth(logp, player, numAdd),
              validateGrowth(logb, player, numAdd),
              validateRT(lort, player, numAdd)]
      return all(lst)

  return False














