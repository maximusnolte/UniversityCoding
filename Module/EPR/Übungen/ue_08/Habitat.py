import random

from EPR.Übungen.ue_08.Carnivore import Carnivore
from EPR.Übungen.ue_08.Herbivore import Herbivore
from EPR.Übungen.ue_08.Omnivore import Omnivore


class Habitat:

    def __init__(self, size):
        self.size = size
        self.plants = []
        self.animals = []

    def calculateUsedSize(self):
        used_size = 0
        for p in self.plants:
            used_size += p.size
        return used_size

    def spawnPlant(self, plant):
        self.plants.append(plant)
        print(f"Spawned plant {plant.id} in habitat.")

    def spawnAnimal(self, animal):
        self.animals.append(animal)
        print(f"Spawned animal {animal.id} in habitat.")

    def despawnPlant(self, plant):
        for p in self.plants:
            if p.id == plant.id:
                self.plants.remove(p)
                print(f"Plant {p.id} despawned.")
                break
        else:
            print(
                f"Tried to despawn plant with ID: {plant.id}, but Plant not found.")

    def despawnAnimal(self, animal):
        for a in self.animals:
            if a.id == animal.id:
                self.animals.remove(a)
                print(f"Animal {a.id} despawned.")
                break
        else:
            print(f"Tried to despawn animal with ID:{animal.id}, but Animal "
                  f"not found.")

    def calculateAnimalCapacity(self):
        food_available = sum(p.size for p in self.plants)
        total_consumption = sum(a.food_consumption for a in self.animals)

        if total_consumption == 0:
            return 0

        avg_consumption = total_consumption / len(self.animals)

        return int(food_available / avg_consumption)


    def checkMate(self, animal1, animal2):
        return (
                animal1.species == animal2.species and
                animal1.mateable and
                animal2.mateable and
                not animal1.poisoned and
                not animal2.poisoned and
                animal1.gender != animal2.gender and
                animal1.alive and animal2.alive
        )

    def update(self, current_day):
        dead_plants = []
        new_plants = []

        for p in self.plants:
            if p.alive:
                p.regenerate()
                offspring = p.reproduce()
                if offspring is not None:
                    offspring.id = len(self.plants) + 1
                    if self.calculateUsedSize() + offspring.min_size <= self.size:
                        new_plants.append(offspring)
                        print(f"Plant {p.id} has spawned offspring.")
                    else:
                        print("Tried to spawn plant offspring, but habitat is full ")
                else:
                    print(f"Plant {p.id} did not reproduce this cycle.")
            else:
                dead_plants.append(p)

        dead_animals = []
        new_animals = []

        for a in self.animals:
            if a.alive:
                a.food_level -= a.food_consumption
                if a.food_level <= 0:
                    print(f"Animal {a.id} has starved to death.")
                    a.alive = False
                    dead_animals.append(a)
                    continue
                if a.mating_cooldown > 0:
                    a.mating_cooldown -= 1

                a.heal()
                if isinstance(a, Carnivore):
                   target = a.hunt(self.animals)
                   if target is not None:
                       dead_animals.append(target)

                elif isinstance(a, Herbivore):
                   food = a.searchFood(self.plants)
                   if food is not None and food.alive:
                         print(f"{a.id} ate plant {food.id}.")
                         if not food.alive:
                              print(f"Plant {food.id} has been fully eaten and removed from habitat.")
                              dead_plants.append(food)


                val = a.age(current_day)
                if val is None:
                    print(f"Animal {a.id} has died of old age.")
                    dead_animals.append(a)
                else:
                    print(f"Animal {a.id} is now {val} days old.")
                    if a.mateable and a.gender == False:
                        if self.calculateAnimalCapacity() - len(self.animals) > 0 :
                            if random.random() < 0.5:
                                partners = []
                                for partner in self.animals:
                                    if self.checkMate(partner, a):
                                        partners.append(partner)
                                if len(partners) == 0:
                                    print(f"Animal {a.id} found no mates.")
                                    continue
                                else:
                                    partner = random.choice(partners)
                                    child = a.mate(partner)
                                    child.id = len(self.animals) + 1
                                    child.day_spawned = current_day
                                    new_animals.append(child)
                                    print(f"Animal {a.id} has mated with {partner.id} to produce offspring {child.id}.")

            else:
                dead_animals.append(a)

        for dp in dead_plants:
            self.despawnPlant(dp)
        for da in dead_animals:
            self.despawnAnimal(da)
        for np in new_plants:
            self.spawnPlant(np)
        for na in new_animals:
            self.spawnAnimal(na)