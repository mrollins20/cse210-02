from game.card import Card


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        next_card (int): The value of a given card.
    """
    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.previous_value = 0
        self.next_card = 0
        for i in range(13):
            card = Card()
            if self.cards[i] != self.next_card[i]:
                self.cards.append(card)
                self.previous_value.append(card)
            else:
                pass
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        hilo = input("Higher or lower? [h/l] ")
        draw_cards = input("Draw again? [y/n] ")
        self.is_playing = (draw_cards == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card = self.cards[i]
        card.draw_card()
        
        if card.value >= self.previous_value:
            self.score += card.points
        self.total_score += self.score
    
    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to draw again.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "
        
        print(f"You drew: {values}")
        print(f"Your score is: {self.self_score}\n")
        self.is_playing == (self.score > 0)