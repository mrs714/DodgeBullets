from vec import Vec

class Entity:

    id_counter = -1

    def __init__(self, pos):
        self.id = self.generateId()
        self.pos = pos
        self.dir = Vec(0, 0)
    
    def generateId(self):
        id_counter += 1
        return id_counter

    def __eq__(self, other):
        return self.id == other.id
