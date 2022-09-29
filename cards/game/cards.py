import random
import turtle
from director import Director
def main():
    _t = turtle.Turtle()

class Cards:
    """A deck of 13 cards numbered 1-13.

    The responsibility of Cards is to keep track of the values of cards and points for it.

    Attributes:
        value (int): The number of the card.
        points (int): The number of points the player has.
        hilo (string): A string of 'h' or 'l'
    """
    def __init__(self):
        """Constructs a new instance of Cards.

        Args:
            self (Cards): An instance of Cards.
        """
        self.value = 0
        self.points = 0
        self.hilo = ""

    def draw_card(self):
        """Draws a random card to display.

        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 6)
        
    def confirm_guess(self, guess):
        """Uses the player's response to generate a boolean for point calculation.

        Args:
            self (Cards): An instance of Cards.
        """

        if self.hilo == guess:
            self.points += 100
        elif self.hilo != guess:
            self.points -= 75
        else:
            self.points += 0