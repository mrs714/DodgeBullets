from entity import Entity

class Bullet(Entity):

    def __init__(self, x, y, owner):
        super().__init__(x, y)
        self.__owner = owner

    def owner(self):
        return self.__owner
    