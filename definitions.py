import math

class Color:
    r: int
    g: int
    b: int
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b
        
    def __init__(self, color: tuple[int, int, int]):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        
         
class Point:
    x: int
    y: int
class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distSquare(self, point: Point) -> int:
        return (self.x-point.x)*(self.x-point.x) + (self.y-point.y)*(self.y-point.y)

class Pixel:
    color: Color
    point: Point
class Pixel:
    color: Color
    point: Point
    def __init__(self, color, point):
        self.color = color
        self.point = point