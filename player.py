from bullet import Bullet
from entity import Entity
from consts import *

class Player(Entity):

    def __init__(self, pos):
        super().__init__(pos)
        self.lastShoot = 0
    
    def shoot(self, dir, bullets, tickCounter):
        if tickCounter - self.lastShoot < shootCooldown:
            return
        b = Bullet(self.pos, self)
        b.dir = dir
        bullets[b.id] = b
        self.lastShoot = tickCounter
    
    def nearBullets(self, radius, bList):
        retList = []
        for b in bList.values():
            if self.pos.distance(b.pos) <= radius:
                retList.append(b)
        return retList