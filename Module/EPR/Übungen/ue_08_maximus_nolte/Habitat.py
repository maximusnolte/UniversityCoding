"""
Module containing the Habitat class which manages
plants and animals in a habitat.
The Habitat is responsible for spawning/despawning, resource calculations,
daily update cycles (plants and animals), and interactions such as feeding,
hunting, mating and aging.
"""

__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import random
from time import sleep

from EPR.Übungen.ue_08_maximus_nolte.Animal import Animal
from EPR.Übungen.ue_08_maximus_nolte.Carnivore import Carnivore
from EPR.Übungen.ue_08_maximus_nolte.Herbivore import Herbivore
from EPR.Übungen.ue_08_maximus_nolte.Omnivore import Omnivore


class Habitat:
    """Represents a habitat that contains plants and animals.

    Attributes:
        size (int): Maximum capacity/size of the habitat
         (units consistent with plant.size).
        plants (list): List of plant objects currently in the habitat.
        animals (list): List of animal objects currently in the habitat.
    """

    def __init__(self, size, plants, animals, round_speed):
        """Initialize a Habitat with a given size.

        Args:
            size (int): The maximum available size/resource capacity
            of the habitat.
        """
        self.size = size
        self.plants = plants
        self.animals = animals
        self.round_speed = round_speed

    def spawnPlant(self, plant):
        """Add a plant to the habitat.

        Args:
            plant: Plant instance to add. Assumes the plant contains an `id`.
        """
        self.plants.append(plant)
        print(f"Spawned plant {plant.id} in habitat.")

    def despawnPlant(self, plant):
        """Remove a plant from the habitat by matching its id.

        If no matching plant is found, a message is printed.

        Args:
            plant: Plant instance (or an object with `id`) to remove.
        """
        for p in self.plants:
            if p.id == plant.id:
                self.plants.remove(p)
                print(f"Plant {p.id} despawned.")
                break
        else:
            print(
                f"Tried to despawn plant with ID: {plant.id}, "
                f"but Plant not found.")

    def calculateUsedSize(self):
        """Calculate the total size currently used by all plants.

        Returns:
            int or float: Sum of `size` for each plant in the habitat.
        """
        used_size = 0
        for p in self.plants:
            used_size += p.size
        return used_size

    def spawnAnimal(self, animal):
        """Add an animal to the habitat.

        Args:
            animal: Animal instance to add. Assumes the animal contains
            an `id`.
        """
        for a in self.animals:
            if a.id == animal.id:
                return
        self.animals.append(animal)
        print(f"Spawned animal {animal.id} in habitat.")

    def despawnAnimal(self, animal):
        """Remove an animal from the habitat by matching its id.

        If no matching animal is found, a message is printed.

        Args:
            animal: Animal instance (or an object with `id`) to remove.
        """
        for a in self.animals:
            if a.id == animal.id:
                self.animals.remove(a)
                print(f"Animal {a.id} despawned.")
                break
        else:
            print(f"Tried to despawn animal with ID:{animal.id}, but Animal "
                  f"not found.")

    def calculateAnimalCapacityHerbivores(self):
        """Estimate how many herbivores the habitat can sustain
        based on plant food.

        Computes total available plant food and divides by
        the average consumption
        of herbivores currently present.

        Returns:
            int: Estimated number of herbivores supportable.
            Returns 0 if no herbivores
                 or total consumption is zero.
        """
        food_available = sum(p.size for p in self.plants)
        herbivores = [a for a in self.animals if isinstance(a, Herbivore)]
        total_consumption = sum(a.food_consumption for a in herbivores)

        if total_consumption == 0:
            return 0

        avg_consumption = total_consumption / len(herbivores)

        return int(food_available / avg_consumption)

    def calculateAnimalCapacityOmnivore(self):
        """Estimate how many omnivores the habitat can sustain.

        Food available includes plant size plus current animal
        food levels (carrion/available meat).
        Uses the average consumption of omnivores present.

        Returns:
            int: Estimated number of omnivores supportable. Returns
            0 if no omnivores
                 or total consumption is zero.
        """
        food_available = sum(p.size for p in self.plants) + sum(a.food_level
                                                                for a in
                                                                self.animals)
        omnivores = [a for a in self.animals if isinstance(a, Omnivore)]
        total_consumption = sum(a.food_consumption for a in omnivores)

        if total_consumption == 0:
            return 0

        avg_consumption = total_consumption / len(omnivores)

        return int((food_available / 2) / avg_consumption)

    def calculateAnimalCapacityCarnivore(self):
        """Estimate how many carnivores the habitat can sustain.

        Food available is the total food level across animals (prey biomass).
        Uses the average consumption of carnivores present.

        Returns:
            int: Estimated number of carnivores supportable. Returns 0
            if no carnivores
                 or total consumption is zero.
        """
        food_available = sum(a.food_level for a in self.animals)
        carnivores = [a for a in self.animals if isinstance(a, Carnivore)]
        total_consumption = sum(a.food_consumption for a in carnivores)

        if total_consumption == 0:
            return 0

        avg_consumption = total_consumption / len(carnivores)

        return int(food_available / avg_consumption)

    def calculateAnimalCapacity(self):
        """Aggregate capacity estimate for all animal types.

        Returns:
            int: Sum of herbivore, omnivore and carnivore capacity estimates.
        """
        herbivore_capacity = self.calculateAnimalCapacityHerbivores()
        omnivore_capacity = self.calculateAnimalCapacityOmnivore()
        carnivore_capacity = self.calculateAnimalCapacityCarnivore()
        return ((herbivore_capacity + omnivore_capacity + carnivore_capacity)
                / 2)

    def checkMate(self, animal1, animal2):
        """Check whether two animals are eligible to mate.

        Conditions considered:
          - same species
          - both mateable
          - neither poisoned
          - different gender
          - both alive

        Args:
            animal1: First animal instance.
            animal2: Second animal instance.

        Returns:
            bool: True if mating is allowed according to the conditions.
        """
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
        """Advance one growth/reproduction cycle for all plants.

        Each alive plant regenerates and may reproduce. New offspring
        are assigned
        a provisional id and are only created if there is room in the habitat.

        Returns:
            tuple: (dead_plants, new_plants)
                dead_plants: list of plant instances that died this cycle.
                new_plants: list of offspring instances that should be spawned.
        """
        dead_plants = []
        new_plants = []

        out_buffer = []
        no_reproduce_buffer = []
        for p in self.plants:
            if p.alive:
                p.regenerate()
                offspring = p.reproduce()

                if offspring is not None:
                    offspring.id = len(self.plants) + 1
                    if (self.calculateUsedSize() +
                            offspring.min_size <= self.size):
                        new_plants.append(offspring)
                        sleep(self.round_speed)
                        print(f"Plant {p.id} has spawned offspring. with id "
                              f"{offspring.id}")

                    else:
                        out_buffer.append("Tried to spawn plant offspring, "
                                          "but habitat is full")

                else:
                    no_reproduce_buffer.append(p.id)

            else:
                dead_plants.append(p)
        out = ""
        for id in no_reproduce_buffer:
            out = out + str(id) + ", "
        print("Plants: " + out + " did not reproduce this cycle.")
        return dead_plants, new_plants

    def handle_starvation(self, a, dead_animals):
        """Apply starvation logic to an animal for one cycle.

        Reduces `food_level` by `food_consumption`.
        If the animal starves (food_level <= 0),
        it is marked dead and appended to `dead_animals`.

        Args:
            a: Animal instance to process.
            dead_animals: List to append dead animals to.

        Returns:
            bool: True if the animal died of starvation
            this cycle, False otherwise.
        """
        a.food_level -= a.food_consumption
        if a.food_level <= 0:
            print(f"Animal {a.id} has starved to death.")
            a.alive = False
            dead_animals.append(a)
            return True
        return False

    def handle_cooldowns_and_heal(self, a):
        """Decrease mating cooldowns and apply healing for an animal.

        Args:
            a: Animal instance to update.
        """
        if a.mating_cooldown > 0:
            a.mating_cooldown -= 1
        a.heal()

    def handle_hunting_or_eating(self, a, dead_animals):
        """Let an animal perform its feeding behavior.

        - Carnivores attempt to hunt other animals; successful
        hunts append the prey to dead_animals.
        - Herbivores search for plants and consume them.
        - Omnivores will either hunt or eat plants depending on availability.

        Args:
            a: Animal instance performing the action.
            dead_animals: List to append animals that are killed/eaten.
        """
        if isinstance(a, Carnivore):
            target = a.hunt(self.animals)
            if target is not None:
                dead_animals.append(target)
                sleep(self.round_speed)

        elif isinstance(a, Herbivore):
            food = a.searchFood(self.plants)
            if food is not None:
                print(f"{a.species}{a.id} ate plant {food.species}{food.id}.")
                sleep(self.round_speed)
                if not food.alive:
                    print(
                        f"Plant {food.species}{food.id} has been fully eaten")
        elif isinstance(a, Omnivore):
            target = a.hunt_or_search(self.animals, self.plants)
            if isinstance(target, Animal):
                dead_animals.append(target)
            elif target is None:
                print(f"Omnivore {a.species}{a.id} found no food this cycle.")

    def handle_aging_and_mating(self, a, current_day, dead_animals,
                                new_animals):
        """Process aging and potential mating for an animal.

        - `a.age(current_day)` is called and if it returns None,
        the animal died of old age.
        - If the animal is mateable and of the designated gender (
        male/female logic),
          it searches for partners and may produce offspring
          (added to new_animals).

        Note: A capacity check is performed before mating to
        avoid overpopulation.

        Args:
            a: Animal instance to process.
            current_day: Current simulation day (passed to age).
            dead_animals: List to append animals that died this cycle.
            new_animals: List to append newly produced offspring.
        """
        val = a.age(current_day)
        if val is None:
            print(f"Animal {a.species} {a.id} has died of old age.")
            dead_animals.append(a)
            return

        print(f"Animal {a.species} {a.id} is now {val} days old.")

        if a.mateable and not a.gender:
            if self.calculateAnimalCapacity() - len(self.animals) > 0:
                if random.random() < 0.8:
                    print(f"Animal {a.species} {a.id} is looking for a mate.")
                    sleep(self.round_speed)
                    partners = []
                    for partner in self.animals:
                        if self.checkMate(partner, a):
                            partners.append(partner)

                    if len(partners) == 0:
                        print(f"Animal {a.species} {a.id} found no mates.")
                        return

                    partner = random.choice(partners)
                    child = a.mate(partner)
                    child.id = len(self.animals) + 1
                    child.day_spawned = current_day
                    new_animals.append(child)
                    print(
                        f"Animal {a.species} {a.id} has mated with"
                        f" {partner.id} to produce offspring {child.id}.")

    def update_animals_cycle(self, current_day):
        """Advance one cycle for all animals: starvation, cooldowns/healing,
        feeding, aging and mating.

        Iterates through animals and collects those that die or are newly born.

        Args:
            current_day: Current simulation day to pass to aging logic.

        Returns:
            tuple: (dead_animals, new_animals)
                dead_animals: list of animals that died this cycle.
                new_animals: list of newly created animal instances.
        """
        dead_animals = []
        new_animals = []
        processed_animals = []

        for a in self.animals:
            if a in processed_animals:
                continue
            processed_animals.append(a)
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
        """Perform a full habitat update for the given day.

        Updates plant cycles and animal cycles, then applies
        spawns and despawns
        collected during the cycles.

        Args:
            current_day: Current simulation day.
        """
        dead_plants, new_plants = self.updatePlantsCycle()
        dead_animals, new_animals = self.update_animals_cycle(current_day)

        self.apply_spawns_despawns(dead_plants, dead_animals, new_plants,
                                   new_animals)

    def apply_spawns_despawns(self, dead_plants, dead_animals, new_plants,
                              new_animals):
        """Apply changes: remove dead entities and add new ones to the habitat.

        Also clears the provided lists after applying the changes.

        Args:
            dead_plants: List of plants to remove.
            dead_animals: List of animals to remove.
            new_plants: List of plant offspring to spawn.
            new_animals: List of animal offspring to spawn.
        """
        for dp in dead_plants:
            self.despawnPlant(dp)
        for da in dead_animals:
            self.despawnAnimal(da)
        for np in new_plants:
            self.spawnPlant(np)
        for na in new_animals:
            self.spawnAnimal(na)
        dead_animals.clear()
        dead_plants.clear()
        new_animals.clear()
        new_plants.clear()
