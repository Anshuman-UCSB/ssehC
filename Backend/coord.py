class Coord:
    def __init__(self, x:int, y:int):
        self.x = int(x)
        self.y = int(y)
    
    def isValid(self):
        return self.x >=0 and self.x<=7 and self.y >=0 and self.y <=7

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        out = Coord(self.x, self.y)
        out.x+=other.x
        out.y+=other.y
        return out
    
    def __eq__(self, other):
        return self.x==other.x and self.y == other.y