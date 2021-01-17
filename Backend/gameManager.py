from coord import Coord
from piece import Piece
from game import Game

def toJson(g:Game):
    """
    {
        "x":x,
        "y":y
    }:{
        "piece":"name"
        "team": 0(white) or 1(black),
        "background": "light", "dark", or "red"
    }
    """
    out = {"pieces":[]}
    out["turn"] = g.turn
    out["score"] = g.getScore()
    out["winner"] = g.winner
    # out["log"] = g.log
    for c in [Coord(x,y) for x in range(8) for y in range(8)]:
        piece = g.getSquare(c)
        if(piece.team != -1):
            out["pieces"].append({"x":c.x, "y":c.y, 
                "piece":piece.name, "team":piece.team,
                "background":"light" if (c.x+c.y)%2==0 else "dark"
            })
    
    return out
    # print(out)

class gameManager:
    def __init__(self):
        self.games = {}

    def addGame(self, id):
        self.games[id] = Game()
    
    def removeGame(self, id):
        del self.games[id]

    def getGame(self, id):
        return self.games[id]

if __name__ == "__main__":
    toJson(Game())