from vec import Vec
from values import *

class Entity:

    id_counter = -1

    def __init__(self, x, y):
        self.__id = self.__generateId()
        self.__position__ = Vec(x, y)
        self.__direction__ = Vec(0, 0)
    
    def __generateId(self):
        Entity.id_counter += 1
        return Entity.id_counter
    
    # Getters
    def id(self):
        return self.__id
    
    def pos(self):
        return self.__position__.copy()

    def dir(self):
        return self.__direction__.copy()

    # Operations
    def __eq__(self, other):
        return self.__id == other.__id
    
    def move(self, speed):
        self.__direction__.normalize()
        self.__position__ += (self.__direction__ * (speed / ticksPS))

    def distance(self, other):
        return self.__position__.distance(other.__position__)
    
    def moving_towards(self, other):
        return self.__direction__.dot(other.__position__ - self.__position__) > 0
    
    def direction_to(self, other):
        return other.__position__ - self.__position__
    
    def outside_map(self, radius):
        return self.__position__.outside2d(radius, 0, map_size_x, 0, map_size_y)
    
    def set_direction(self, d):
        self.__direction__ = d.copy()