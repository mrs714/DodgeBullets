from vec import Vec
from numpy import array, cross
from numpy.linalg import solve, norm
from math import sqrt



class Line3d:

    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

    def distance(self, other):
        crossProduct = self.vector.crossProduct3d(other.vector)
        return abs((other.point - self.point).dotProduct(crossProduct)/crossProduct.mod())
    
    def closestAltitude(self, other):

        p1, p2, p3 = self.point.x, self.point.y, self.point.z
        q1, q2, q3 = other.point.x, other.point.y, other.point.z
        v1, v2, v3 = self.vector.x, self.vector.y, self.vector.z
        u1, u2, u3 = other.vector.x, other.vector.y, other.vector.z

        return (2*(u1/u3 - v1/v3)*(p1 - q1 + (q3*u1)/u3 - (p3*v1)/v3) + 2*(u2/u3 - v2/v3)*(p2 - q2 + (q3*u2)/u3 - (p3*v2)/v3))/(2*(u1/u3 - v1/v3)**2 + 2*(u2/u3 - v2/v3)**2)
    
    def horizontalDistance(self, other, k = None):

        if k == None:
            k = self.closestAltitude(other)
        p1, p2, p3 = self.point.x, self.point.y, self.point.z
        q1, q2, q3 = other.point.x, other.point.y, other.point.z
        v1, v2, v3 = self.vector.x, self.vector.y, self.vector.z
        u1, u2, u3 = other.vector.x, other.vector.y, other.vector.z

        return sqrt((p1+(v1/v3)*(k-p3)-q1-(u1/u3)*(k-q3))**2+(p2+(v2/v3)*(k-p3)-q2-(u2/u3)*(k-q3))**2)
    
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