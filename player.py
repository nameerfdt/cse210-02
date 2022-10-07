class Player:
    '''A player 
    
    The responsibility of the player is to guess if next card is higher or lower.
    
    Attributes:
        name (str): The name of the player
        score (int): Starts at 300
        guess (string): high/lo (h/l)
    '''

    def __init__(self):
        '''Constructs a new instance of player.
    
        Args:
            self (Player): an instance of player
        '''

        self.name = ""
        self.score = 300
        self.guess = ""


    def make_guess(self):
        '''Asks player if next card higher or lower
        
        Args:
            self (Player): an instance of player
        '''
        check_guess = False
        while not check_guess:
            self.guess = input('Higher or Lower? (h/l): ')
            if self.guess.lower() == "h" or self.guess.lower() == "l":
                check_guess = True
            else:
                print("\nThat was not a valid input, please try again.\n")
        