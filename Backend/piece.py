from coord import Coord
class Piece:
    def __init__(self, name:str = "null", team:int = -1, id:int = -1, timeMoved:int = 0):
        self.name = name
        self.team = team
        self.id = id
        self.timeMoved = timeMoved

    def __str__(self):
        return "{" + f"Name: {self.name}, team: {self.team}, id: {self.id}, Last time: {self.timeMoved}"+"}"
    
    def getCopy(self):
        return Piece(self.name, self.team, self.id, self.timeMoved)