import random

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.BerryBush import BerryBush


class Herbivore(Animal):
    def __init__(self, **animal_args):
        super().__init__(**animal_args)


    def searchFood(self, plants):
        if not plants:
            return None

        plant = random.choice(plants)
        if not plant.alive or plant.size <= 0:
            return None

        food_required = self.max_food - self.food_level
        if food_required <= 0:
            return None

        max_food_from_plant = plant.size * plant.food_value


        food_taken = min(food_required, max_food_from_plant)
        if food_taken <= 0:
            return None

        size_eaten = food_taken / plant.food_value

        self.eat(food_taken)
        plant.getEaten(size_eaten)

        return plant



