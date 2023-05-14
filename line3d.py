from vec import Vec
from numpy import array, cross
from numpy.linalg import solve, norm



class Line3d:

    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

    def distance(self, other):
        crossProduct = self.vector.crossProduct3d(other.vector)
        return abs((other.point - self.point).dotProduct(crossProduct)/crossProduct.mod())
    
    def intersects(self, other, radius):
        return self.distance(other) <= radius
    
    def intersection(self, other):
        # define lines A and B by two points
        XA0 = array([self.point.x, self.point.y, self.point.z])
        XA1 = array([self.point.x + self.vector.x, self.point.y + self.vector.y, self.point.z + self.vector.z])
        XB0 = array([other.point.x, other.point.y, other.point.z])
        XB1 = array([other.point.x + other.vector.x, other.point.y + other.vector.y, other.point.z + other.vector.z])

        # compute unit vectors of directions of lines A and B
        UA = (XA1 - XA0) / norm(XA1 - XA0)
        UB = (XB1 - XB0) / norm(XB1 - XB0)
        # find unit direction vector for line C, which is perpendicular to lines A and B
        UC = cross(UB, UA); UC /= norm(UC)

        # solve the system derived in user2255770's answer from StackExchange: https://math.stackexchange.com/q/1993990
        RHS = XB0 - XA0
        LHS = array([UA, -UB, UC]).T
        sol = (solve(LHS, RHS))
        return Vec(sol[0], sol[1], sol[2])
    
    def __str__(self):
        return "point: " + str(self.point) + " vector: " + str(self.vector)