from Die import Die
from Player import Player        
def main():
    die1 = Die()
    die2 = Die()
    die3 = Die()
    numPlayers = 0
    while True :
        numPlayersS = input( "Input the number of players" )
        if numPlayersS.isdigit() :
            numPlayers = int(numPlayersS)
            break
    #Initialize Player Array
    playList = []
    for i in range(0, numPlayers) :
        playList.append( Player( input( "Please give the name for Player " + str( i+1 ) ) ) )
    #Actual Game Code
    gamePlay = True
    i = 0
    while gamePlay :
        #Cycles through players
        if i == numPlayers :
            i = 0
        playList[i].isTurn = True
        while playList[i].isTurn :
            die1Value = die1.__str__()
            die2Value = die2.__str__()
            die3Value = die3.__str__()
            print ( playList[i].name, "rolled a " + str(die1Value), str(die2Value), str(die3Value) )
            die12Sum = die1Value + die2Value
            die13Sum = die1Value + die3Value
            die23Sum = die2Value + die3Value
            die123Sum = die12Sum + die3Value
            madeChange = False
            playList[i].canPlay = True
            while playList[i].canPlay :
                if len( playList[i].board ) == 0 :
                    playList[i].canPlay = False
                    playList[i].isTurn = False
                    print (playList[i].name, "wins!")
                    return 0
                if die1Value == playList[i].board[0] or die2Value == playList[i].board[0] or die3Value == playList[i].board[0] or  die12Sum == playList[i].board[0] or die23Sum == playList[i].board[0] or die13Sum == playList[i].board[0] or die123Sum == playList[i].board[0] :
                    print (str(playList[i].board[0]) + " removed")
                    removeValue = playList[i].board[0]
                    playList[i].board.pop(0)
                    print (playList[i].board)
                    if removeValue == 12 and playList[i].board[0] == 12 :
                        playList[i].canPlay = False
                        isTurn = False
                        madeChange = False
                    else :
                        playList[i].canPlay = True
                        madeChange = True
                else :
                    playList[i].canPlay = False
            if madeChange :
                playList[i].isTurn = True
            else :
                playList[i].isTurn = False
        print (playList[i].name, "ends their turn.")
        i = i +1
main()



