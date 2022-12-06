from math import sqrt

class Point():
    def __init__(self, x, y, linkPoint = None):
        self.x = x
        self.y = y
        self.linkPoint = linkPoint

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

def dist(a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    return sqrt(dx ** 2 + dy ** 2)
