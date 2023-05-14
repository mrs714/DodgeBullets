from math import sqrt
import numpy as np
from math import sin, cos

class Vec:
    
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dotProduct(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def inv(self):
        return Vec(-self.x, -self.y, -self.z)
    
    def normalize(self):
        norm = sqrt(self.x**2 + self.y**2 + self.z**2)
        self.x /= norm
        self.y /= norm
        self.z /= norm
    
    def crossProduct3d(self, u):
        a = np.array([self.x, self.y, self.z])
        b = np.array([u.x, u.y, u.z])
        c = np.cross(a, b)
        return Vec(c[0], c[1], c[2])
    
    def mod(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def rotation2d(self, angle):
        return Vec(self.x*cos(angle) - self.y*sin(angle), self.x*sin(angle) + self.y*cos(angle), self.z)