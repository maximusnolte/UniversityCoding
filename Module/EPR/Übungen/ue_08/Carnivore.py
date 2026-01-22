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