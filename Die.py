from random import randint
class Die:
    def __init__( self ):
        self.side = 0
    def roll( self ):
        self.side = randint(1, 6)
    def __str__ ( self ):
        self.roll()
        return(self.side)
#die = Die()
#die.__str__()
