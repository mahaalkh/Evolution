

class WateringHole:



  def __init__(self, amount, placedCards = None):
    """
    initializes the watering hole with the given amount and placedCards
    :param amount: int
    :param placedCards: [TraitCard, ...]
    """
    if amount < 0:
      self.amount = 0
    self.amount = amount
    if placedCards == None:
      self.placedCards = []
    else:
      self.placedCards = placedCards

  def setAmount(self, amount):
    """
    sets this watering hole's amount to the given amount
    :param amount: int
    """
    if amount < 0:
      self.amount = 0
    self.amount = amount

  def getAmount(self):
    """
    gets the amount of this watering hole
    :return: int
    """
    return self.amount

  def setPlacedCards(self, cards):
    """
    sets this watering hole's placedCards to the given cards
    :param cards: [TraitCard, ...]
    """
    self.placedCards = cards

  def getPlacedCards(self):
    """
    get this watering hole's placedCards
    :return: [TraitCard, ...]
    """
    return self.placedCards

  def addToPlacedCards(self, card):
    """
    adds a card to the placedCards
    :param card: TraitCard
    """
    self.getPlacedCards().append(card)


  def addToAmount(self, amount):
    """
    adds the amount to the watering hole
    :param amount: int
    """
    new_amount  = self.getAmount() + amount
    if new_amount < 0:
      self.setAmount(0)
    else:
      self.setAmount(new_amount)

  def turnOverCards(self):
    """
    adds the food points on the placedCards to the amount in this watering hole
    """
    for card in self.placedCards:
      amount = card.getFoodPoints()
      self.addToAmount(amount)

    self.setPlacedCards([])
