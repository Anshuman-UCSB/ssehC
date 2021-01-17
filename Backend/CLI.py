from game import Game
from coord import Coord
from piece import Piece
from colorama import Fore, Back, Style


def chooseSprite(p:Piece):
    if(p.team != -1):
        pieceMap = {
            "knight":"♘",
            "rook":"♖",
            "bishop":"♗",
            "king":"♔",
            "queen":"♕",
            "pawn":"♙"
        }
        return pieceMap[p.name]
    # elif(p.team == 1):
    #     pieceMap = {
    #         "knight":"♞",
    #         "rook":"♜",
    #         "bishop":"♝",
    #         "king":"♚",
    #         "queen":"♛",
    #         "pawn":"♟︎"
    #     }
    #     return pieceMap[p.name]
    return " "
def printGame(g:Game):    
    b = g.board
    print(Style.BRIGHT,end="")
    print(Fore.RED+"        Black  "+Fore.RESET)
    print("    0 1 2 3 4 5 6 7")
    print("  "+"▄"*18)
    for y in range(len(b)):
        print(f"{y} █", end="")
        for x in range(len(b[y])):
            print(Back.LIGHTBLACK_EX if (x+y)%2 == 1 else Back.BLACK, end="")
            if(b[y][x].team == 1):
                print(Fore.RED,end="")
            elif(b[y][x].team == 0):
                print(Fore.BLUE,end="")
            print(chooseSprite(b[y][x]), end =" ")
            print(Back.RESET+Fore.RESET,end = "")
        print("█")
    print("  "+"▀"*18)
    print(Fore.BLUE+"        White  "+Fore.RESET)
    print(Style.RESET_ALL,end="")

def printPossibleMoves(g:Game, c:Coord):
    moves = g.getPossibleMoves(c)
    b = g.board
    print(Style.BRIGHT,end="")
    print(Fore.RED+"        Black  "+Fore.RESET)
    print("    0 1 2 3 4 5 6 7")
    print("  "+"▄"*18)
    for y in range(len(b)):
        print(f"{y} █", end="")
        for x in range(len(b[y])):
            print(Back.LIGHTBLACK_EX if (x+y)%2 == 1 else Back.BLACK, end="")
            if(Coord(x,y) in moves):
                print(Back.LIGHTMAGENTA_EX,end="")
            elif(Coord(x,y) == c):
                print(Back.LIGHTCYAN_EX,end="")
            if(b[y][x].team == 1):
                print(Fore.RED,end="")
            elif(b[y][x].team == 0):
                print(Fore.BLUE,end="")
            print(chooseSprite(b[y][x]), end =" ")
            print(Back.RESET+Fore.RESET,end = "")
        print("█")
    print("  "+"▀"*18)
    print(Fore.BLUE+"        White  "+Fore.RESET)
    print(Style.RESET_ALL,end="")

def printValidMoves(g:Game, c:Coord):
    moves = g.getValidMoves(c)
    b = g.board
    print(Style.BRIGHT,end="")
    print(Fore.RED+"        Black  "+Fore.RESET)
    print("    0 1 2 3 4 5 6 7")
    print("  "+"▄"*18)
    for y in range(len(b)):
        print(f"{y} █", end="")
        for x in range(len(b[y])):
            print(Back.LIGHTBLACK_EX if (x+y)%2 == 1 else Back.BLACK, end="")
            if(Coord(x,y) in moves):
                print(Back.LIGHTMAGENTA_EX,end="")
            elif(Coord(x,y) == c):
                print(Back.LIGHTCYAN_EX,end="")
            if(b[y][x].team == 1):
                print(Fore.RED,end="")
            elif(b[y][x].team == 0):
                print(Fore.BLUE,end="")
            print(chooseSprite(b[y][x]), end =" ")
            print(Back.RESET+Fore.RESET,end = "")
        print("█")
    print("  "+"▀"*18)
    print(Fore.BLUE+"        White  "+Fore.RESET)
    print(Style.RESET_ALL,end="")