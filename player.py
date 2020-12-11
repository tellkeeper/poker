import json

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = {}
  
    def draw(self, deck, discard=None):
        if discard:
            for item in discard:
                self.hand[item] = Deck.drawCard(self)
        else:
            for i in range(1, 6):
                self.hand[i] = Deck.drawCard(self)            
    
    def discard_dialog(self):
        dialog = input("Enter the number of each card you wish to discard separated by a comma then press enter: ")
        discard = dialog.split(',')
        discard = [item.strip(' ') for item in discard]
        for d in discard:
            self.hand.pop(int(d))
        self.draw(deck, discard)

    def showHand(self):
        print(json.dumps(bob.hand, indent=3))
