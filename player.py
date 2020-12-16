import json
<<<<<<< HEAD
import deck
=======
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = {}
  
    def draw(self, deck, discard=None):
        if discard:
            for item in discard:
<<<<<<< HEAD
                self.hand[item] = deck.draw_card()
            return self.hand
        else:
            for i in range(1, 6):
                self.hand[i] = deck.draw_card()
            return self.hand
               
    def discard_dialog(self, deck):
        dialog = input("Enter the number of each card you wish to discard separated by a comma then press enter: ")
        discard = dialog.split(',')
        discard = [item.strip(' ') for item in discard]
        if len(discard) > 4:
            print("error, you cannot discard more than 4 cards")
            discard = []
            self.discard_dialog(deck)
=======
                self.hand[item] = Deck.drawCard(self)
        else:
            for i in range(1, 6):
                self.hand[i] = Deck.drawCard(self)            
    
    def discard_dialog(self):
        dialog = input("Enter the number of each card you wish to discard separated by a comma then press enter: ")
        discard = dialog.split(',')
        discard = [item.strip(' ') for item in discard]
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08
        for d in discard:
            self.hand.pop(int(d))
        self.draw(deck, discard)

<<<<<<< HEAD
    def show_hand(self):
        print(json.dumps(self.hand, indent=3))
=======
    def showHand(self):
        print(json.dumps(bob.hand, indent=3))
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08
