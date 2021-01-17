from coord import Coord
SCHOLARS_MATE = [
    [Coord(5,6), Coord(5,4)],
    [Coord(4,1), Coord(4,3)],
    [Coord(6,6), Coord(6,4)],
    [Coord(3,0), Coord(7,4)]
]

QUEENING_TEST = [
    [Coord(4,6), Coord(4,4)],
    [Coord(3,1), Coord(3,3)],
    [Coord(4,4), Coord(3,3)],
    [Coord(4,1), Coord(4,2)],
    [Coord(3,3), Coord(4,2)],
    [Coord(3,0), Coord(3,1)],
    [Coord(4,2), Coord(3,1)],
    [Coord(6,0), Coord(5,2)], #invalid knight move
    [Coord(4,0), Coord(3,0)],
    [Coord(3,1), Coord(2,0)]
]

REPETITION_TEST = [
    [Coord(0,4), Coord(0,5)],
    [Coord(6,6), Coord(5,5)],
    [Coord(0,5), Coord(0,4)],
    [Coord(5,5), Coord(6,6)],
    [Coord(0,4), Coord(0,5)],
    [Coord(6,6), Coord(5,5)],
    [Coord(0,5), Coord(0,4)],
    [Coord(5,5), Coord(6,6)],
    [Coord(0,4), Coord(0,5)],
    [Coord(6,6), Coord(5,5)],
    [Coord(0,5), Coord(0,4)],
    [Coord(5,5), Coord(6,6)]
]

