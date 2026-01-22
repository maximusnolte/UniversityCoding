
class LivingThing:

    def __init__(self, id, species, max_size):
        self.id = id
        self.species = species
        self.max_size = max_size
        self.alive = True

    def die(self):
        self.alive = False
        return f"{self.id} has died."
