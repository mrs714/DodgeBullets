from entity import Entity
from consts import *

class Player(Entity):

    def __init__(self, pos):
        super().__init__(pos)
    
    def move(self, dir):
        pass
    
    def shoot(self):
        pass
    
    def nearBullets(self, radius, entList):
        retList = []
        for ent in entList:
            if self.pos.distance(ent.pos) <= radius:
                retList.append(ent)
        return retList