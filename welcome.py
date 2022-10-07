class Welcome:
    # Welcome class for the hilo program.

    def __init__(self):
        pass

    def start(self):
        # Display program welcome message.
        print ("\n       »»————-　★　————-««")
        print (" ╔═════════════════════════════╗")
        print ("∞╢ Welcome to the hilo program ╟∞")
        print (" ╚═════════════════════════════╝")
        print ("  ✩｡:*•.─────  ❁ ❁  ─────.•*:｡✩")
        print ()
        print ("Designed by: Alex, Joshua, Tracy, and Mark")
        
    def get_name():
        name = input("\nPlease enter your name: ")
        return name

    def display_rules(self):
        print ("\nGame Rules:")
        print ("The player starts the game with 300 points.")
        print ("Individual cards are represented as a number from 1 to 13.")
        print ("The current card is displayed.")
        print ("The player guesses if the next one will be higher or lower.")
        print ("The next card is displayed.")
        print ("The player earns 100 points if they guessed correctly.")
        print ("The player loses 75 points if they guessed incorrectly.")
        print ("If a player reaches 0 points the game is over.")
        print ("If a player has more than 0 points they decide if they want to keep playing.")
        print ("If a player decides not to play again the game is over.")
