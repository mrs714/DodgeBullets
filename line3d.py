from math import sqrt
from vec import Vec

class Line3d:

    # point is a Vec object indicating a random point of the line
    # vector is a Vec object indicating the direction of the line
    def __init__(self, pt_x, pt_y, pt_z, vec_x, vec_y, vec_z):
        self.__point = Vec(pt_x, pt_y, pt_z)
        self.__vector = Vec(vec_x, vec_y, vec_z)
    
    # getters
    def point(self):
        return self.__point.get_coords()
    
    def vector(self):
        return self.__vector.get_coords()
    
    def closestAltitude(self, other):
        p1, p2, p3 = self.point()
        q1, q2, q3 = other.point()
        v1, v2, v3 = self.vector()
        u1, u2, u3 = other.vector()

        # k when derivative of distance is 0 -> k for the min distance
        return (2*(u1/u3 - v1/v3)*(p1 - q1 + (q3*u1)/u3 - (p3*v1)/v3) + 2*(u2/u3 - v2/v3)*(p2 - q2 + (q3*u2)/u3 - (p3*v2)/v3))/(2*(u1/u3 - v1/v3)**2 + 2*(u2/u3 - v2/v3)**2)
    
    def horizontalDistance(self, other, k = None):
        if k == None:
            k = self.closestAltitude(other)
            
        p1, p2, p3 = self.point()
        q1, q2, q3 = other.point()
        v1, v2, v3 = self.vector()
        u1, u2, u3 = other.vector()

        # distance of the intersections with the plane z = k
        return sqrt((p1+(v1/v3)*(k-p3)-q1-(u1/u3)*(k-q3))**2+(p2+(v2/v3)*(k-p3)-q2-(u2/u3)*(k-q3))**2)
    
    def normalize_vector(self):
        self.__vector.normalize()

    def get_point_from_value(self, value):
        return (self.__point + (self.__vector.normalized() * value)).get_coords()
    
    def __str__(self):
        return "point: " + str(self.__point) + " vector: " + str(self.__vector)