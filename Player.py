class Player:
    def __init__( self, playerName ):
        self.name = playerName
        self.board = [ 0 ] * 24
        for i in range( 0, 12 ):
            self.board[i] = i + 1
        for i in range( 12, 24 ):
            self.board[i] = 24 - i
        self.isTurn = False
        self.canPlay = True
