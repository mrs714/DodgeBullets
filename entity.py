from vec import Vec
from entitityType import EntityType

class Entity:

    def __init__(self, pos, type):
        self.pos = pos
        self.dir = Vec(0, 0)
        self.type = type
    
    def move(self, dir):
        pass

    def nearEntities(self, radius):
        pass
