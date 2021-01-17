from game import *

inpMap = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
}

def clearScreen():
    print('\033c',end="")

def parseToCoord(inp:str):
    try:
        c = Coord(-1, -1)
        c.x = inpMap[inp[0]]
        c.y = 8-int(inp[1])
        return c
    except:
        return "uh oh"

g = Game()
printGame(g)
while g.winner == -1:
    clearScreen()
    printGame(g)
    try:
        if(g.turn == 0):
            # print("White move: ")
            c = Coord(-1, -1)
            while c.x == -1 or c.y == -1:
                inp = input("Select Square\n > ")
                c = parseToCoord(inp)
                print(c)
            clearScreen()
            if(g.getSquare(c).team != g.turn):
                raise("wrong team")
            printValidMoves(g, c)
            inp = input("Move to where?\n > ")
            to = parseToCoord(inp)
            g.makeMove(c, to)
        elif(g.turn == 1):
            # print("White move: ")
            c = Coord(-1, -1)
            while c.x == -1 or c.y == -1:
                inp = input("Select Square\n > ")
                c = parseToCoord(inp)
                print(c)
            clearScreen()
            if(g.getSquare(c).team != g.turn):
                raise("wrong team")
            printValidMoves(g, c)
            inp = input("Move to where?\n > ")
            to = parseToCoord(inp)
            g.makeMove(c, to)
            
    except KeyboardInterrupt:
        clearScreen()
        print("\n\nGoodbye!")
        exit(0)
    except:
        pass
clearScreen()
printGame(g)
g.checkWin()
input("\npress any key to exit")