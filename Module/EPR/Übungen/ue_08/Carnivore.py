"""
This module provides the `Carnivore` class, a specialization of `Animal`
that hunts other animals, can inflict damage (and poison if venomous),
and can mate to produce offspring. Hunting and mating behaviors interact
with other animal instances in the simulation.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import random

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.Herbivore import Herbivore


class Carnivore(Animal):
    """A carnivorous animal that hunts other animals and reproduces.

    Attributes:
        venomous (bool): Whether this carnivore can poison prey when injuring.
        damage (int | float): Amount of damage inflicted on injured prey.
        Inherits attributes from `Animal` such as `id`, `species`, `gender`,
        `max_size`, `food_level`, `max_food`, `size_mult`, `mating_*` fields, etc.
    """

    def __init__(self, venomous: bool, damage, **animal_args):
        """Initialize a new Carnivore.

        Args:
            venomous (bool): If True, successful injures may apply poison.
            damage (int | float): Damage applied to prey when injuring.
            **animal_args: Keyword arguments forwarded to the `Animal`
                superclass constructor (e.g. `id`, `species`, `max_size`, ...).

        Returns:
            None
        """
        self.venomous = venomous
        self.damage = damage
        super().__init__(**animal_args)

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
        if self.food_level <= self.max_food * 0.3:
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
                    if random.random() < 0.3:
                        prey.getInjured(self.damage)
                        if self.venomous:
                            prey.poisoned = True
                            print(f"Prey {prey.species}{prey.id} has been "
                                  f"poisoned by "
                                  f"carnivore {self.id}")
                            return None
                        return None
                    else:
                        print(f"{self.species}{self.id} hunted and ate "
                              f"animal {prey.species}{prey.id}.")
                        self.eat(prey.food_level)
                        prey.die()
                        return prey
                else:
                    print(f"Carnivore {self.species}{self.id} failed to hunt prey {prey.species}{prey.id} due "
                          f"to smaller size.")
                    return None
            elif prey.species == self.species:
                print(f"Carnivore {self.species}{self.id} cannot hunt prey "
                      f"{prey.species}{prey.id} of the "
                      f"same species.")
                return None
            else:
                if size > prey_size:
                    if random.random() < 0.4:
                        prey.getInjured(self.damage)
                        if (self.venomous and isinstance(prey, Carnivore) and not
                        prey.venomous):
                            prey.poisoned = True
                            print(f"Prey {prey.species}{prey.id} has been "
                                  f"poisoned by "
                                  f"carnivore {self.id}")
                            return None
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
            print(f"Animal {self.id} has mated with Animal {partner.id}., "
                  f"cooldown is now {self.mating_cooldown} for self")

        elif partner.gender:
            partner.mateable = False
            partner.mating_cooldown = partner.mating_start_cooldown
            print(f"Animal {self.id} has mated with Animal {partner.id}, "
                  f"cooldown is now {partner.mating_cooldown} for partner")

        gender = random.choice([True, False])
        return self.__class__(
            id=None,
            max_age= (self.max_age + partner.max_age) // 2,
            size_mult= (self.size_mult + partner.size_mult) // 2,
            food_consumption=self.food_consumption,
            max_food=self.max_food,
            days_to_starve=self.days_to_starve,
            mating_start_cooldown=self.mating_start_cooldown,
            mating_age=self.mating_age,
            healing_rate=self.healing_rate,
            gender=gender,
            species=self.species,
            day_spawned=None,
            max_size = (self.max_size + partner.max_size) // 2,
            venomous = self.venomous,
            damage = self.damage
        )
