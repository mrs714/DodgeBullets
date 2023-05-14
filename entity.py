from vec import Vec
from consts import *

class Entity:

    id_counter = -1

    def __init__(self, pos):
        self.id = self.generateId()
        self.pos = pos
        self.dir = Vec(0, 0)
    
    def generateId(self):
        Entity.id_counter += 1
        return Entity.id_counter

    def __eq__(self, other):
        return self.id == other.id
    
    def move(self, speed):
        self.dir.normalize()
        self.pos += self.dir * (speed / ticksPS)
