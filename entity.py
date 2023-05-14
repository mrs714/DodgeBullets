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

    def intersection(self, other):

        A = self.pos
        B = self.pos + self.dir
        C = other.pos
        D = other.pos + other.dir

        # Line AB represented as a1x + b1y = c1
        a1 = B.y - A.y
        b1 = A.x - B.x
        c1 = a1*(A.x) + b1*(A.y)
    
        # Line CD represented as a2x + b2y = c2
        a2 = D.y - C.y
        b2 = C.x - D.x
        c2 = a2*(C.x) + b2*(C.y)
    
        determinant = a1*b2 - a2*b1
    
        if (determinant == 0):
            # The lines are parallel. This is simplified
            # by returning a pair of FLT_MAX
            return None
        else:
            x = (b2*c1 - b1*c2)/determinant
            y = (a1*c2 - a2*c1)/determinant
            return Vec(x, y)
    
    def mayCollide(self, other, radius):
        i = self.intersection(other)
        if i == None:
            return False
        self.dir.normalize()
        return (i - self.pos).x / self.dir.x >= -radius if self.dir.x != 0 else i.y >= -radius