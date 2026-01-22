import random

from EPR.Übungen.ue_08.Carnivore import Carnivore
from EPR.Übungen.ue_08.Herbivore import Herbivore
from EPR.Übungen.ue_08.Omnivore import Omnivore


class Habitat:

    def __init__(self, size):
        self.size = size
        self.plants = []
        self.animals = []

    def spawnPlant(self, plant):
        self.plants.append(plant)
        print(f"Spawned plant {plant.id} in habitat.")

    def despawnPlant(self, plant):
        for p in self.plants:
            if p.id == plant.id:
                self.plants.remove(p)
                print(f"Plant {p.id} despawned.")
                break
        else:
            print(
                f"Tried to despawn plant with ID: {plant.id}, but Plant not found.")

    def calculateUsedSize(self):
        used_size = 0
        for p in self.plants:
            used_size += p.size
        return used_size

    def spawnAnimal(self, animal):
        self.animals.append(animal)
        print(f"Spawned animal {animal.id} in habitat.")

    def despawnAnimal(self, animal):
        for a in self.animals:
            if a.id == animal.id:
                self.animals.remove(a)
                print(f"Animal {a.id} despawned.")
                break
        else:
            print(f"Tried to despawn animal with ID:{animal.id}, but Animal "
                  f"not found.")

    #TODO zwischen den verschiedenen Tierarten unterscheiden
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

    def updatePlantsCycle(self):
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
                        print(f"Plant {p.id} has spawned offspring. with id "
                              f"{offspring.id}")
                    else:
                        print(
                            "Tried to spawn plant offspring, but habitat is full ")
                else:
                    print(f"Plant {p.id} did not reproduce this cycle.")
            else:
                dead_plants.append(p)

        return dead_plants, new_plants


    def update_animals_cycle(self, current_day):
        dead_animals = []
        new_animals = []

        for a in self.animals:
            if not a.alive:
                dead_animals.append(a)
                continue

            if self.handle_starvation(a, dead_animals):
                continue

            self.handle_cooldowns_and_heal(a)
            self.handle_hunting_or_eating(a, dead_animals)
            self.handle_aging_and_mating(a, current_day, dead_animals,
                                         new_animals)

        return dead_animals, new_animals


    def update(self, current_day):
        dead_plants, new_plants = self.updatePlantsCycle()
        dead_animals, new_animals = self.update_animals_cycle(current_day)

        self.apply_spawns_despawns(dead_plants, dead_animals, new_plants,
                                   new_animals)




    def handle_starvation(self, a, dead_animals):
        a.food_level -= a.food_consumption
        if a.food_level <= 0:
            print(f"Animal {a.id} has starved to death.")
            a.alive = False
            dead_animals.append(a)
            return True
        return False

    def handle_cooldowns_and_heal(self, a):
        if a.mating_cooldown > 0:
            a.mating_cooldown -= 1
        a.heal()

    def handle_hunting_or_eating(self, a, dead_animals):
        if isinstance(a, Carnivore):
            target = a.hunt(self.animals)
            if target is not None:
                dead_animals.append(target)

        elif isinstance(a, Herbivore):
            food = a.searchFood(self.plants)
            if food is not None and food.alive:
                print(f"{a.id} ate plant {food.id}.")
                # Original-Logik beibehalten, auch wenn sie bisschen weird ist:
                if not food.alive:
                    print(
                        f"Plant {food.id} has been fully eaten and removed from habitat.")
                    dead_plants = []  # not used here; see note below

    def handle_aging_and_mating(self, a, current_day, dead_animals,
                                new_animals):
        val = a.age(current_day)
        if val is None:
            print(f"Animal {a.id} has died of old age.")
            dead_animals.append(a)
            return

        print(f"Animal {a.id} is now {val} days old.")

        # Mating-Block 1:1 aus deiner Logik übernommen
        if a.mateable and a.gender == False:
            if self.calculateAnimalCapacity() - len(self.animals) > 0:
                if random.random() < 0.5:
                    partners = []
                    for partner in self.animals:
                        if self.checkMate(partner, a):
                            partners.append(partner)

                    if len(partners) == 0:
                        print(f"Animal {a.id} found no mates.")
                        return

                    partner = random.choice(partners)
                    child = a.mate(partner)
                    child.id = len(self.animals) + 1
                    child.day_spawned = current_day
                    new_animals.append(child)
                    print(
                        f"Animal {a.id} has mated with {partner.id} to produce offspring {child.id}.")

    def apply_spawns_despawns(self, dead_plants, dead_animals, new_plants,
                              new_animals):
        for dp in dead_plants:
            self.despawnPlant(dp)
        for da in dead_animals:
            self.despawnAnimal(da)
        for np in new_plants:
            self.spawnPlant(np)
        for na in new_animals:
            self.spawnAnimal(na)
