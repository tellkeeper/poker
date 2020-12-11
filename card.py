class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
    def __str__(self):
        return "{} of {}".format(self.value, self.suit)