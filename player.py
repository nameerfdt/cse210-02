class Player:
    '''A player 
    
    The responsibility of the player is to guess if next card is higher or lower.
    
    Attributes:
        name (str): The name of the player
        score (int): Starts at 300
        guess (string): high/lo (h/l)
    '''

    def __init__(player):
        '''Constructs a new instance of player.
    
        Args:
            self (Player): an instance of player
        '''

        player.name = ""
        player.score = 0
        player.guess = ""


    def name(player):
        '''Updated the player name.
    
        Args:
            self (Player): an instance of player
        '''

        player.name = input('What is your name? ')
        print (player.name.capitalize())

    def score(player):
        '''Displays starting score.
        
        Args:
            self (Player): an instance of player
        '''

        # player starts game with 300 points
        player.score = 300

    def guess(player):
        '''Asks player if next card higher or lower
        
        Args:
            self (Player): an instance of player
        '''

        player.guess = input('Higher or Lower: (h/l)')
        