from math import sqrt, acos, pi

class Vector():
    def __init__(self, a, b):
        self.x = b.x - a.x
        self.y = b.y - a.y

    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

# вычисление угла между двумя прямыми
def angle(a1, a2, b1, b2):
    a = Vector(a1, a2)
    b = Vector(b1, b2)
    cos = round((a.x * b.x + a.y * b.y) / (a.length * b.length), 8)
    return acos(cos) * (180 / pi)
