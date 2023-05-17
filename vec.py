from math import sqrt, sin, cos

class Vec:
    
    # x, y, z are the coordinates of the vector
    def __init__(self, x, y, z = 0):
        self.__x = x
        self.__y = y
        self.__z = z
    
    # getters
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def z(self):
        return self.__z

    def get_coords(self):
        return self.__x, self.__y, self.__z
    
    # basic operations
    def set_z(self, z):
        self.__z = z
    
    def flatten(self):
        self.__z = 0

    def flattened(self):
        return Vec(self.__x, self.__y, 0)

    def __add__(self, other):
        return Vec(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
    
    def __sub__(self, other):
        return Vec(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
    
    def __mul__(self, val):
        return Vec(self.__x*val, self.__y*val, self.__z*val)
    
    # complex operations
    def dot(self, other):
        return self.__x*other.__x + self.__y*other.__y + self.__z*other.__z
    
    def distance(self, other):
        return sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2 + (self.__z - other.__z)**2)
    
    def invert(self):
        self.__x = -self.__x
        self.__y = -self.__y
        self.__z = -self.__z

    def inverted(self):
        return Vec(-self.__x, -self.__y, -self.__z)
    
    def normalize(self):
        norm = self.norm()
        if norm == 0:
            return
        self.__x /= norm
        self.__y /= norm
        self.__z /= norm
    
    def normalized(self):
        norm = self.norm()
        if norm == 0:
            return Vec(0, 0, 0)
        return Vec(self.__x/norm, self.__y/norm, self.__z/norm)
    
    def norm(self):
        return sqrt(self.__x**2 + self.__y**2 + self.__z**2)
    
    def rotate2d(self, angle):
        self.__x, self.__y = self.__x*cos(angle) - self.__y*sin(angle), self.__x*sin(angle) + self.__y*cos(angle)

    def rotated2d(self, angle):
        return Vec(self.__x*cos(angle) - self.__y*sin(angle), self.__x*sin(angle) + self.__y*cos(angle), self.__z)
    
    def outside2d(self, radius, min_x, max_x, min_y, max_y):
        return self.__x < min_x + radius or self.__x > max_x - radius or self.__y < min_y + radius or self.__y > max_y - radius
    
    def copy(self):
        return Vec(self.__x, self.__y, self.__z)
    
    def __str__(self):
        return "x: " + str(self.__x) + " y: " + str(self.__y) + " z: " + str(self.__z)
    