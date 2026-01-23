"""
This module provides the `Herbivore` class, a specialization of `Animal`
that searches for and consumes plant-based food sources.
"""
import random

from EPR.Übungen.ue_08.Animal import Animal



class Herbivore(Animal):
    """A herbivorous animal that feeds on plant objects.

    The Herbivore class extends `Animal` and implements plant-searching
    behavior. Instances rely on attributes and methods from the base
    `Animal` class such as `max_food`, `food_level`, and `eat`.

    Attributes:
        Inherits attributes from `Animal`.
    """
    def __init__(self, **animal_args):
        """Initialize a new Herbivore.
               Args:
                   **animal_args: Keyword arguments forwarded to the `Animal`
                       superclass constructor.
               Returns:
                   None
               """
        super().__init__(**animal_args)

    def searchFood(self, plants):
        """Search for a plant to eat and consume part of it.

        The method selects a random plant from `plants`, checks whether it
        is available (alive and with positive size), computes how much food
        can be taken without exceeding the herbivore's needs, updates the
        herbivore's food level via `eat`, and reduces the plant's size via
        `getEaten`.

        Args:
            plants (Sequence): A sequence of plant objects.
        Returns:
            None: The plant that was eaten, or `None` if no
            suitable plant was found or no food was taken.
        """

        food_required = self.max_food - self.food_level
        if food_required <= 0:
            print("Herbivore is not hungry.")
            return None
        plant = random.choice(plants)
        if not plant.alive or plant.size <= 0:
            print(f"Plant {plant.id} is not available for eating.")
            return None

        max_food_from_plant = plant.size * plant.food_value

        food_taken = min(food_required, max_food_from_plant)
        if food_taken <= 0:
            return None

        size_eaten = food_taken / plant.food_value

        self.eat(food_taken)
        plant.getEaten(size_eaten)

        return plant



