from .deck import Deck
from .card import Card
from .player import Player


deck = Deck()
bob = Player("Bob")

bob.draw(deck)
bob.showHand()
bob.discard_dialog()
bob.showHand()
