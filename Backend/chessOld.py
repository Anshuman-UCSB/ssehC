class Piece:
    def __init__(self, pieceType:str = "null", team:int = -1, id:int = 0):
        self.type = pieceType #type
        self.team = team #0 if white, 1 if black
        self.id = id     #Individual piece, if placeholder then 0, if piece, 1->32
        self.lastTimeMoved = 0
    
    def toStr(self):
        if self.id == 0:
            return {"type":"null"}
        return {"type":self.type, "team":self.team, "id":self.id, "last moved":self.lastTimeMoved}

class Game:
    def __init__(self):
        self.board = [[Piece() for x in range(8)] for y in range(8)]
        pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for i in range(1,9):
            self.board[0][i-1] = Piece(pieces[i-1], 1, i)
        for i in range(9,17):
            self.board[1][i-9] = Piece("pawn", 1, i)
        for i in range(17,25):
            self.board[6][i-17] = Piece("pawn", 0, i)
        for i in range(25,33):
            self.board[7][i-25] = Piece(pieces[i-25], 0, i)

        self.time = 0
                
    def debugPrint(self):
        printMap = {
            "queen" :"Q",
            "king"  :"K",
            "pawn"  :"p",
            "rook"  :"R",
            "bishop":"B",
            "knight":"K",
            "null"  :" "
        }
        print("██████████")
        for row in self.board:
            print("█", end="")
            for item in row:
                print(printMap[item.type.lower()], end = "")
            print("█")
        print("██████████")

    def debugPrintMoves(self, x, y):
        printMap = {
            "queen" :"Q",
            "king"  :"K",
            "pawn"  :"p",
            "rook"  :"R",
            "bishop":"B",
            "knight":"K",
            "null"  :" "
        }

        moves = self.getMoves(x,y)
        print("██████████")
        for y in range(len(self.board)):
            print("█", end="")
            for x in range(len(self.board[y])):
                if((x,y) not in moves):
                    print(printMap[self.board[y][x].type.lower()], end = "")
                else:
                    print("#",end="")
            print("█")
        print("██████████")

    def coordInBoard(self, x, y):
        return (0<=x and x<=7 and 0<=y and y<=7)

    def getMoves(self, x, y):
        p = self.board[y][x]
        if(p.id == 0):
            return []
        enemy = 0 if p.team ==1 else 1
        if p.type == "knight":
            deltas = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2, -1), (-2, 1), (-1, 2)]
            out = []
            for delta in deltas:
                newX = x+delta[0]
                newY = y+delta[1]
                if self.coordInBoard(newX, newY) and self.board[newY][newX].team != p.team:
                    out.append((newX, newY))
            return out
        elif p.type == "queen":
            out = []
            dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1, 1)]
            for direction in dirs:
                dX = x
                dY = y
                while True:
                    dX+=direction[0]
                    dY+=direction[1]
                    if(self.coordInBoard(dX, dY) == False):
                        break
                    if(self.board[dY][dX].team == self.board[y][x].team):
                        break
                    if(self.board[dY][dX].team == enemy):
                        out.append((dX,dY))
                        break
                    out.append((dX,dY))
            return out
        elif p.type == "rook":
            out = []
            dirs = [(0,1), (1,0), (0,-1), (-1,0)]
            for direction in dirs:
                dX = x
                dY = y
                while True:
                    dX+=direction[0]
                    dY+=direction[1]
                    if(self.coordInBoard(dX, dY) == False):
                        break
                    if(self.board[dY][dX].team == self.board[y][x].team):
                        break
                    if(self.board[dY][dX].team == enemy):
                        out.append((dX,dY))
                        break
                    out.append((dX,dY))
            return out
        elif p.type == "pawn":
            out =[]
            dY = -1 if p.team ==0 else 1
            captures = [(-1, dY), (1, dY)]
            for move in captures:
                if(self.coordInBoard(move[0], move[1]) and self.board[y+move[1]][x+move[0]].team != -1):
                    out.append(y+move[1], x+move[0])
            if self.coordInBoard(x, y+dY) and self.board[y+dY][x].team == -1:
                out.append(y+dY, x)
                if p.lastTimeMoved == 0:
                    if self.board[y+2*dY][x].team == -1:
                        out.append(y+2*dY, x)
            "now en passant"
            checkSquares = [(x+1, y), (x-1, y)]
            for move in checkSquares:
                if(self.coordInBoard(move[0], move[1])):
                    if self.board[move[1]][move[0]]
            return out

        return "error"
            


if __name__ == '__main__':
    g = Game()
    coord = (5, 3)
    g.board[1][3] = Piece()
    g.board[coord[1]][coord[0]] = Piece("queen", 1, 12)
    g.board[0][3] = Piece()
    g.debugPrint()
    print(g.board[coord[1]][coord[0]].toStr())
    print(g.getMoves(coord[0], coord[1]))
    g.debugPrintMoves(coord[0], coord[1])