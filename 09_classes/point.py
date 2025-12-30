import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f'({self.x}, {self.y})'
        
    def move(self, angle, distance):
        self.x = self.x + distance * math.cos(angle)
        self.y = self.y +distance * math.sin(angle)


if __name__ == '__main__':
    p = Point(4, 3)
    print(p)
    p.move(0.785398, 1.42)
    print(p)
