import random

cards = {}
<<<<<<< HEAD


class Deck:
    def __init__(self):
=======
class Deck:
    def __init__(self):       
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08
        self.build()

    def build(self):
        CARD_MAP = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King",
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
        }
        card_num = 1
        for suit in ["Spades", "Diamonds", "Hearts", "Clubs"]:
            for card_value in range(1, 14):
                cards[card_num] = {
                    "card_id": card_num,
                    "value": CARD_MAP[card_value],
                    "suit": suit,
                }
                card_num += 1

<<<<<<< HEAD
    def draw_card(self):
        return cards.pop(random.choice(list(cards.keys())))
=======
    def drawCard(self):
        return cards.pop(random.choice(list(cards.keys())))
>>>>>>> 7f49d37cda32b9086c05bc3f5b1554fa88e36a08
