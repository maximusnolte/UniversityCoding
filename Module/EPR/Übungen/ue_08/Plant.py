import random

from EPR.Übungen.ue_08.LivingThing import LivingThing


class Plant(LivingThing):

    def __init__(self, min_size, food_value, regen_rate,
                 **living_thing_args):
        self.min_size = min_size
        self.size = min_size
        self.food_value = food_value
        self.regen_rate = regen_rate
        super().__init__(**living_thing_args)

    def regenerate(self):
        if self.alive:
            if (self.size + self.regen_rate) < self.max_size:
                self.size += self.regen_rate
            else:
                self.size = self.max_size

    def getEaten(self, amount):
        self.size -= amount
        if self.size < self.min_size:
            self.die()
            return None
        print(f"{self.id} has been eaten for {amount} size.")
        return self.size

    def reproduce(self):
        if self.size == self.max_size:
            if random.random() < 0.5:
                return self.__class__(
                    id=None,
                    min_size=self.min_size,
                    food_value=self.food_value,
                    regen_rate=self.regen_rate,
                    max_size=self.max_size,
                    species=self.species
                )
        return None
