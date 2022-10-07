from welcome import Welcome
from player import Player
from deck import Deck

class Director:
    """A in-between controller for the Hilo game.
    Handles all calculations as a dealer would. Gives elements to
    other classes for storage and calling."""

    def __init__(self):
        """Creates Director"""
        self.update_total = 0
        self.current_card = 0
        self.previous_card = 0
        self.welcome = Welcome()
        self.player = Player()
        self.deck = Deck()
        self.continue_game = True
        
    def start_game(self):
        """Starts Game and calls setup scripts"""
        self.welcome.start()
        self.player.name = self.welcome.get_name()
        self.welcome.display_rules()
        self.game()

    def compare_card(self):
        """Compares Cards to see if Player was Correct"""
        guess = self.player.guess
        if guess.lower() == "h":
            if self.current_card >= self.previous_card:
                return True
            else:
                return False
        elif guess.lower() == "l":
            if self.current_card <= self.previous_card:
                return True
            else:
                return False
    
    def display_card(self):
        """Displays output to player. Calls other scripts in related."""
        print("\n---------------------------------------------------")
        print(f"\nThe Current Card is a {self.previous_card}.")
        self.player.make_guess()
        self.update_score()
        if self.update_total == 100:
            print(f"\nYou were correct! You drew a {self.current_card}! 100 points for you {self.player.name}!")
        elif self.update_total == -75:
            print(f"\nBad luck, you were incorrect! You drew a {self.current_card}! You lose 75 points {self.player.name}.")
        if self.player.score < 0:
            self.continue_game = False
            print(f"\nSorry, Game Over! Your score went below 0 at a total of {self.player.score} points. Play again sometime!")
        elif self.player.score >= 0:
            continue_check = False
            while not continue_check:
                continue_game = input(f"\nYour current score is {self.player.score}, {self.player.name}.\nWould you like to continue playing? (y or n): ")
                if continue_game.lower() == "y" or continue_game.lower() == "n":
                    continue_check = True
                else:
                    print("\nThat was not a valid input, please try again.\n")
            if continue_game.lower() == "n":
                print(f"\nThanks for playing, {self.player.name}.\nYou ended the game with a total of {self.player.score} points!\nPlease play again sometime!")
                self.continue_game = False

    def draw_cards(self):
        """Calls the deck.draw_card script to draw the needed cards for play."""
        if self.previous_card == 0:
            self.previous_card = self.deck.draw_card()
        else:
            self.previous_card = self.current_card
        self.current_card = self.deck.draw_card()
    
    def update_score(self):
        """Calls compare card and changes the added total to what is needed."""
        if self.compare_card():
            self.update_total = 100
        else:
            self.update_total = -75
        self.player.score += self.update_total

    def game(self):
        """Loops game commands until continue_game is False."""
        while self.continue_game:
            self.draw_cards()
            self.display_card()