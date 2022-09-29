from cards import Cards


class Director:
    """A person who directs the game.

    The responsibility of the Director is to control the sequence of play.

    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        current_card_value (int): The value of the current card.
        next_card_value (int): The value of the next card.
        hilo_value (string): The given value of a player-given input.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.score = 300
        self.current_card_value = 0
        self.next_card_value = 0
        self.hilo_value = ""

        for i in range(13):
            deck = Cards()
            self.cards.append(deck)
    
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
        """Prompt the user for a response to Higher or lower and ask the user if they want to draw another card.

        Args:
            self (Director): An instance of Director.
        """
        hi_lo = input("Higher or lower? [h/l] ")
        confirm_guess(deck, hi_lo)
        draw_card = input("Play again? [y/n] ")
        self.is_playing = (draw_card == "y")

    def do_updates(self):
        """Updates the player's score and current_card_value.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        for i in range(len(self.cards)):
            card = self.cards[i]
            
        

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to draw again.

        Args:
            self (Director): An instance of Director.
        """