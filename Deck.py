import random


class Deck:
    """A deck of cards with values between 1 and 13.

    The responsibility of Deck is to keep track of the drawn card, and drawing new cards.

    Attributes:
         card (int): The number value of the card
    """

    def __init__(self):
        """Constructs a new instance of Deck with a card

        Args:
            self (Die): An instance of Deck.
        """
        self.card = None

    def draw_card(self):
        """Generates a new random value

        Args:
            self (Deck): An instance of Deck.
        """
        self.card = random.randint(1, 13)
        return self.card


if __name__ == '__main__':
    deck = Deck()
    print(deck.draw_card())
