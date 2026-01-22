import random

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.BerryBush import BerryBush


class Herbivore(Animal):
    def __init__(self, **animal_args):
        super().__init__(**animal_args)

    def searchFood(self, plants):
        plant = random.choice(plants)
        food_requiered = self.max_food - self.food_level
        food = min(food_requiered, plant.food_value*plant.size)
        if isinstance(plant, BerryBush):
            if random.random() < plant.poison_chance:
                self.poisoned = True
                return None
        self.eat(food)
        plant.getEaten(food)
        return plant


