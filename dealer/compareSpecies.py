IS_FAT = True

def whichCaseFatCompare(species1, species2): 
  """
  Checks how the species compare to each other based on fattissue soecies comparison
  :param species1: Species
  :param species2: Species 
  :return: int 
  where 1 means more need for fat food, 0 means more need for food, -1 means greater population 
  """
  if (species1.maximumFeed(IS_FAT) > species2.maximumFeed(IS_FAT)):
      return 1
  elif (species1.maximumFeed(IS_FAT) == species2.maximumFeed(IS_FAT)):
      if (species1.getFood() > species2.getFood()): 
	  return 0
      elif (species1.getFood() == species2.getFood()): 
	  if (species1.getPopulation() > species2.getPopulation()): 
	      return -1
      else: 
	  return -2
  else: 
      return -2

def whichCaseFoodCompare(species1, species2): 
    """
    Checks how the species compare to each other based on non fatfood species comparison
    :param species1: Species
    :param species2: Species 
    :return: int where 1 means greater population, 0 means more need for food, -1 means greater body 
    """
    if (species1.getPopulation() > species2.getPopulation()):
        return 1
    elif (species1.getPopulation() == species2.getPopulation()):
        if (species1.getFood() > species2.getFood()):
            return 0
	elif (species1.getFood() == species2.getFood()): 
            if (species1.getBodySize() > species2.getBodySize()): 
	        return -1
        else: 
            return -2
    else: 
	return -2
	
