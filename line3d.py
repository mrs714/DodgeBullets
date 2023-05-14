from vec import Vec

class Line3d:

    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

    def distance(self, other):
        crossProduct = self.vector.crossProduct3d(other.vector)
        return abs((other.point - self.point).dotProduct(crossProduct)/crossProduct.mod())
    
    def intersects(self, other, radius):
        return self.distance(other) <= radius