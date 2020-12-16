import json
import deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = {}
  
    def draw(self, deck, discard=None):
        if discard:
            for item in discard:
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
        for d in discard:
            self.hand.pop(int(d))
        self.draw(deck, discard)

    def show_hand(self):
        print(json.dumps(self.hand, indent=3))
