from deck import Deck
from card import Card
from player import Player


deck = Deck()
player = Player("Bob")

player.draw(deck)
player.show_hand()
player.discard_dialog(deck)
player.show_hand()
