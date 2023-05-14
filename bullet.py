from entity import Entity

class Bullet(Entity):

    def __init__(self, pos, owner):
        super().__init__(pos)
        self.owner = owner
    