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
        if len(self.animals) < self.animal_capacity:
            self.animals.append(animal)
            print(f"Spawned animal {animal.id} in habitat.")
        else:
            print(f"Tried to spawn animal, but habitat is at full capacity.")


    def despawnPlant(self, plant):
        for p in self.plants:
            if p.id == plant.id:
                self.plants.remove(p)
                print("Plant {p.id} despawned.")
        else:
            print(f"Tried to despawn plant with ID: {plant.id}, but Plant not "
                  f"found.")

    def despawnAnimal(self, animal):
        for a in self.animals:
            if a.id == animal.id:
                self.animals.remove(a)
                print("Animal {a.id} despawned.")
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

    def handleMating(self):
        pass

    def checkMate(self, animal1, animal2):
        return (
                isinstance(animal1, type(animal2)) and
                animal1.mateable and
                animal2.mateable and
                not animal1.poisoned and
                not animal2.poisoned and
                animal1.gender != animal2.gender
        )

    def update(self, current_day):

        for p in self.plants:
            p.regenerate()
            offspring = p.reproduce()
            if offspring is not None:
                offspring.id = len(self.plants) + 1
                if self.calculateUsedSize() < self.size - offspring.min_size:
                    self.spawnPlant(offspring)
                    print(f"Plant {p.id} has spawned offspring.")
                else:
                    print("Tried to spawn plant offspring, but habitat is full ")
            else:
                print(f"Plant {p.id} did not reproduce this cycle.")

        for a in self.animals:
            a.heal()
            if isinstance(a, Carnivore):
               prey = a.hunt(self.animals)
               if prey is not None:

                   self.despawnAnimal(prey)
            elif isinstance(a, Herbivore):
               food = a.searchFood(self.plants)
               if food is not None:
                     print(f"{a.id} ate plant {food.id}.")
                     if food.size <= 0:
                          self.despawnPlant(food)
                          print(f"Plant {food.id} has been fully eaten and removed from habitat.")
            age = a.age(current_day)
            if age is None:
                print(f"Animal {a.id} has died of old age.")
                self.despawnAnimal(a)
            else:
                print(f"Animal {a.id} is now {a.age} days old.")
                if age <= a.max_age / 2:
                    if self.calculateAnimalCapacity() - len(self.animals) > 0 :
                        if random.random() < 0.5:
                            pass
                        #TODO Mating process




