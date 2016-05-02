#Representation of a trait card for the Evolution game
import trait
from validate import validateCard, validateTrait

class TraitCard:
  """
  represents a trait card
  """
  def __init__(self, trait, food_points):
    """
    Initializes a trait card with valid food points and trait.
    :param food_points: int between -8 and 8 inclusive
    :param trait: Trait
    """
    if validateCard(trait, food_points):
      self.food_points = food_points
      self.trait = trait

  def getTrait(self):
    """
    returns the trait field
    """
    return self.trait

  def setTrait(self, trait):
    """
    sets the trait field to the given trait if the trait is a valid trait
    :param trait: Trait
    """
    if validateTrait(trait):
      self.trait = trait

  def getFoodPoints(self):
    """
    returns the food_points field
    """
    return self.food_points

  def setFoodPoints(self, food_points):
    """
    sets the food_points field to the given food_points if the new food_points is valid
    :param food_points: int between -8 and 8
    """
    if validateCard(self.trait, food_points):
      self.food_points = food_points

  def display_card(self):
    """
    displays this card
    """
    points = "food points: " + str(self.getFoodPoints())
    t = "trait: " + self.getTrait().value
    points_and_traits = points + ", " + t

    return "card: " + points_and_traits









