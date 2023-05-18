from bullet import Bullet
from entity import Entity
from values import *

class Player(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__lastShoot = 0
        self.__health = 100
    
    def shoot(self, dir):
        if context.tickCounter - self.__lastShoot >= shootCooldown:
            b = Bullet(self.__position__.x(), self.__position__.y(), self)
            b.__direction__ = dir
            self.__lastShoot = context.tickCounter
            context.bullets[b.id()] = b
        
    def closeBullets(self, radius):
        return {id: b for id, b in context.bullets.items() if self.distance(b) <= radius}
    
    def get_health(self):
        return self.__health
    
    def remove_health(self, amount):
        self.__health -= amount