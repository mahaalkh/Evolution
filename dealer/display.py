from Tkinter import *
class Display(Frame):
  def __init__(self, master=None):
    """
    initializes the frame 
    """
    master = Tk()
    Frame.__init__(self, master)
    self.grid(row = 0, column = 0)
    self.pack() 
   
    scrollH = Scrollbar(self, orient = HORIZONTAL)
    scrollV = Scrollbar(self, orient = VERTICAL)
    scrollH.pack(side = BOTTOM, fill = X) 
    scrollV.pack(side = RIGHT, fill = Y) 
    self.canvas = Canvas(self, width = 100, height = 100)
    
    scrollH.config(command = self.canvas.xview)
    scrollV.config(command = self.canvas.yview)
    
    self.canvas.config(yscrollcommand = scrollV.set, xscrollcommand = scrollH.set)
    self.canvas.pack(side = LEFT, expand = True, fill = BOTH)

  def print_player(self, playerInfo):
    """
    packs the labels that reperesent the player 
    :param playerInfo: [String, [String, ...], [String, ...]]
    """
    [player_id_string, list_of_species_strings, list_of_cards_strings] = playerInfo
    player_id_label = Label(self.canvas, text = player_id_string)
    player_id_label.pack(side = BOTTOM)
    for species_string in list_of_species_strings:
      label1 = Label(self.canvas, text = species_string)
      label1.pack(side = BOTTOM)

    for card_string in list_of_cards_strings:
      label2 = Label(self.canvas, text = card_string)
      label2.pack(side = BOTTOM)

  def display_player(self, playerInfo):
    """
    displays the player based on the given player info
    :param playerInfo: [String, [String, ...], [String, ...]]
    """
    QUIT = Button(self.canvas, fg = "red", bg = "blue", text = "quit", command = self.quit)
    QUIT.pack(side = TOP)

    self.print_player(playerInfo)


  def display_dealer(self, dealerInfo) :
    """
    displays the dealer based on the given dealer info 
    :param dealerInfo: [String, [ [String, [String, ...], [String, ...]], ...], [String, ...]]
    """
    [watering_hole, list_of_player_strings, list_of_cards_strings]= dealerInfo
    self.QUIT = Button(self.canvas, fg = "red", bg = "blue", text = "quit", command = self.quit)
    self.QUIT.pack(side = TOP)

    self.watering_hole_label = Label(self.canvas, text = "watering hole: " + watering_hole)
    self.watering_hole_label.pack(side = BOTTOM)

    for player_info in list_of_player_strings:
      self.print_player(player_info)

    for card in list_of_cards_strings:
      self.card1 = Label(self.canvas, text = card)
      self.card1.pack(side = LEFT)


 
def spawnBoth(dealerInfo, playerInfo):
    """
    displays both the dealer and the player based in the given info
    :param dealerInfo: [String, [[String, [String, ...], [String, ...]], ...], [String, ...]]
    :param playerInfo: [String, [String, ...], [String, ...]]
    """
    displayPlayer = Display()
    displayDealer = Display()
    displayDealer.display_dealer(dealerInfo)
    displayPlayer.display_player(playerInfo)
    displayPlayer.master.mainloop(2) 
    displayDealer.master.mainloop()




