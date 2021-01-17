from game import Game
from coord import Coord
from piece import Piece
from CLI import printGame,printValidMoves,printPossibleMoves
import testSets

def clearGame(g:Game):
    for c in [Coord(x,y) for x in range(8) for y in range(8)]:
        g.setSquare(c, Piece())

if __name__ == "__main__":
    g = Game()

    printGame(g)
    for move in testSets.QUEENING_TEST:
        if(g.makeMove(move[0], move[1])):
            print("Able to make move")
        else:
            print("Unable to make move")
        printGame(g)
        
        if(g.winner!=-1):
            print(g.winner, "won!")
            break
    for move in g.log:
        print(f"Move [{move[2]}] {move[0]} -> {move[1]}    Score: {move[3]}")