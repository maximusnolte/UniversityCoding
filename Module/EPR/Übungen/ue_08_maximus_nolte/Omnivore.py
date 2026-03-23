__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import random

from EPR.Übungen.ue_08_maximus_nolte.Animal import Animal
from EPR.Übungen.ue_08_maximus_nolte.Carnivore import Carnivore
from EPR.Übungen.ue_08_maximus_nolte.Herbivore import Herbivore


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
        The method updates food levels via `eat`, may call `die` or
        `getInjured`
        on the prey, and prints status messages.

        Args:
            animals (Sequence[Animal]): Sequence of candidate prey animals.

        Returns:
            Animal | None:
                - The prey instance if it was successfully hunted and eaten.
                - The hunter instance if the hunter died as result of the hunt.
                - `None` if no successful hunt occurred or only
                injuring/poisoning happened.
        """
        if random.random() > 0.5:
            print(f"Omnivore {self.species} {self.id} decided not to hunt "
                  f"this "
                  f"time.")
            return None
        if self.food_level <= self.max_food *0.2:
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
                        print(f"{self.species} {self.id} hunted and ate "
                              f"animal {prey.id}.")
                        self.eat(prey.food_level)
                        prey.die()
                        return prey
                else:
                    print(f"Omnivore {self.species}{self.id} failed to hunt "
                          f"prey {prey.id} "
                          f"due "
                          f"to smaller size.")
                    return None
            elif prey.species == self.species:
                print(f"Omnivore {self.species} {self.id} cannot hunt "
                      f"prey {prey.id} of the "
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
                    print(f"Omnivore {self.species} {self.id} was killed "
                          f"by prey {prey.id} "
                          f"during a failed hunt.")
                    return self
                return None
        print(f"Omnivore {self.species} {self.id} is not hungry and cannot "
              f"hunt.")
        return None

    def hunt_or_search(self, animals, plants):
        if random.random() < 0.5:
            return self.hunt(animals)
        else:
            return self.searchFood(plants)

    def mate(self, partner):
        """Mate with another animal and produce an offspring instance.

        The method updates mating state (`mateable` and `mating_cooldown`) for
        the mating participant(s) and constructs a new instance of the same
        class as the parents with averaged characteristics. The offspring is
        returned with `id=None` and inherited species.

        Args:
            partner (Animal): The mating partner.

        Returns:
            Carnivore: A new `Carnivore` instance representing the offspring.
        """
        if self.gender:
            self.mateable = False
            self.mating_cooldown = self.mating_start_cooldown
            print(f"Animal {self.species} {self.id} has mated with Animal"
                  f" {partner.id}., "
                  f"cooldown is now {self.mating_cooldown} for self")

        elif partner.gender:
            partner.mateable = False
            partner.mating_cooldown = partner.mating_start_cooldown
            print(f"Animal{self.species}  {self.id} has mated with Animal"
                  f" {partner.id}, "
                  f"cooldown is now {partner.mating_cooldown} for partner")

        gender = random.choice([True, False])
        return self.__class__(
            id=None,
            max_age=(self.max_age + partner.max_age) // 2,
            size_mult=(self.size_mult + partner.size_mult) // 2,
            food_consumption=self.food_consumption,
            max_food=self.max_food,
            days_to_starve=self.days_to_starve,
            mating_start_cooldown=self.mating_start_cooldown,
            mating_age=self.mating_age,
            healing_rate=self.healing_rate,
            gender=gender,
            species=self.species,
            day_spawned=None,
            max_size=(self.max_size + partner.max_size) // 2,
            damage=self.damage
        )
