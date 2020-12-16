<<<<<<< HEAD
from deck import Deck
from card import Card
from player import Player


deck = Deck()
player = Player("Bob")

player.draw(deck)
player.show_hand()
player.discard_dialog(deck)
player.show_hand()
=======
from .deck import Deck
from .card import Card
from .player import Player


deck = Deck()
bob = Player("Bob")

bob.draw(deck)
bob.showHand()
bob.discard_dialog()
bob.showHand()
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08
