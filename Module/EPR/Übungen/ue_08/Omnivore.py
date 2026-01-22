import random

from EPR.Übungen.ue_08.BerryBush import BerryBush
from EPR.Übungen.ue_08.Animal import Animal


class Omnivore(Animal):

    def __init__(self, **animal_args):
        super().__init__(**animal_args)

    def searchFood(self, plants):
        plant = random.choice(plants)
        food_required = self.max_food - self.food_level
        self.eat(plant)
        plant.getEaten(food_required)

        if isinstance(plant, BerryBush):
            if random.random() < 1.0 < 1.0 - plant.poison_chance:
                return (f"{self.id} "
                        f"found poisonous berries and is getting sick.")
        return f"{self.id} is searching for plants to eat."
#TODO complete the class implementation