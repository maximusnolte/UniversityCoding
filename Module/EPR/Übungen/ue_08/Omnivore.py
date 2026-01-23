import random

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.Carnivore import Carnivore
from EPR.Übungen.ue_08.Herbivore import Herbivore


class Omnivore(Animal):

    def __init__(self, damage, **animal_args):
        self.damage = damage
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

    def hunt(self, animals):
        """Attempt to hunt a prey from a sequence of animals.

        The method selects a prey (not the hunter itself) and compares sizes.
        Behavior varies depending on prey type and relative sizes:
          - If prey is a `Herbivore`, success conditions and a small random
            chance to injure (possibly poison) are applied.
          - If prey is same species, hunting is refused.
          - For other prey, a higher chance to injure (and possibly poison)
            is applied, with additional special-case handling when the prey
            is a larger `Carnivore` that can kill the hunter.
        The method updates food levels via `eat`, may call `die` or `getInjured`
        on the prey, and prints status messages.

        Args:
            animals (Sequence[Animal]): Sequence of candidate prey animals.

        Returns:
            Animal | None:
                - The prey instance if it was successfully hunted and eaten.
                - The hunter instance if the hunter died as result of the hunt.
                - `None` if no successful hunt occurred or only injuring/poisoning happened.
        """
        if self.food_level <= self.max_food / 2:
            prey = random.choice(animals)
            if len(animals) == 1:
                print("No other animals to hunt.")
                return None
            while prey.id == self.id:
                prey = random.choice(animals)
            prey_size = prey.calculateSize()
            size = self.calculateSize()
            if isinstance(prey, Herbivore):
                if size > prey_size:
                    if random.random() < 0.1:
                        prey.getInjured(self.damage)
                        return None
                    else:
                        print(f"{self.id} hunted and ate animal {prey.id}.")
                        self.eat(prey.food_level)
                        prey.die()
                        return prey
                else:
                    print(f"Carnivore {self.id} failed to hunt prey {prey.id} due "
                          f"to smaller size.")
                    return None
            elif prey.species == self.species:
                print(f"Carnivore {self.id} cannot hunt prey {prey.id} of the "
                      f"same species.")
                return None
            else:
                if size > prey_size:
                    if random.random() < 0.2:
                        prey.getInjured(self.damage)
                        return None
                    else:
                        self.eat(prey.food_level)
                        prey.die()
                        print(f"{self.id} hunted and ate animal {prey.id}.")
                        return prey
                if size*1.5 <= prey_size and isinstance(prey, Carnivore):
                    prey.eat(self.food_level)
                    self.die()
                    print(f"Carnivore {self.id} was killed by prey {prey.id} "
                          f"during a failed hunt.")
                    return self
                return None
        print("Carnivore is not hungry and cannot hunt.")
        return None

    def hunt_or_search(self, animals, plants):
        if random.random() < 0.5:
            return self.hunt(animals)
        else:
            return self.searchFood(plants)