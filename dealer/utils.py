def compileSpecies(lop):
  """
    Compiles all the species boards from the list of players provided
    :param lop: a list of Player
    :return: a list of list where the list index represents the index of the player the species in that list come from
  """
  boards = []
  for player in lop:
    zoo = []
    for board in player.getSpeciesBoards():
      zoo.append(board)
    boards.append(zoo)
  return boards
