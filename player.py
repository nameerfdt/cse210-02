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

        self.guess = input('Higher or Lower: (h/l)')
        