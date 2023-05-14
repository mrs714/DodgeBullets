from math import sqrt

class Vec:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def inv(self):
        return Vec(-self.x, -self.y)
    
    def normalize(self):
        norm = sqrt(self.x**2 + self.y**2)
        return Vec(self.x/norm, self.y/norm)
    