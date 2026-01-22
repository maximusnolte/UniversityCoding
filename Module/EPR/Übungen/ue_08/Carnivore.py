import random

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.Herbivore import Herbivore


class Carnivore(Animal):

    def __init__(self, venomous: bool, damage, **animal_args):
        self.venomous = venomous
        self.damage = damage
        super().__init__(**animal_args)

    def hunt(self, animals):
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
                    if self.venomous:
                        prey.poisoned = True
                        print(f"Prey {prey.id} has been poisoned by "
                              f"carnivore {self.id}")
                        return None
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
                    if (self.venomous and isinstance(prey, Carnivore) and not
                    prey.venomous):
                        prey.poisoned = True
                        print(f"Prey {prey.id} has been poisoned by "
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

    def mate(self, partner):
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