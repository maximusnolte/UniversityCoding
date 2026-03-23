__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import contextlib
import copy
from time import sleep

from EPR.Übungen.ue_08_maximus_nolte.BerryBush import BerryBush
from EPR.Übungen.ue_08_maximus_nolte.Carnivore import Carnivore
from EPR.Übungen.ue_08_maximus_nolte.Habitat import Habitat
from EPR.Übungen.ue_08_maximus_nolte.Herbivore import Herbivore
from EPR.Übungen.ue_08_maximus_nolte.Omnivore import Omnivore
from EPR.Übungen.ue_08_maximus_nolte.Plant import Plant


class Ecosystem:

    def __init__(self, round_speed, habitat_size, start_plants,
                 start_animals, skip_rounds):
        self.round_speed = round_speed
        self.current_round = 1
        self.skip_rounds = skip_rounds
        self.habitat = Habitat(habitat_size, start_plants,
                               start_animals, round_speed)
        print(f"Initial Start with: {len(start_plants)} plants and "
              f"{len(start_animals)} animals. ")
        print(f"Used Plant-Size: {self.habitat.calculateUsedSize()}")
        print(f"Animal Capacity: {self.habitat.calculateAnimalCapacity()}")

    def simulateRound(self):
        is_multiple = (self.skip_rounds > 0
                       and self.current_round % self.skip_rounds == 0)

        # Update immer ausführen
        with (contextlib.redirect_stdout(None) if not is_multiple
              else contextlib.ExitStack()):
            self.habitat.update(self.current_round)

        # Nur bei Vielfachen ausgeben
        if is_multiple or self.skip_rounds == 0:
            print(f"Simulating Round {self.current_round}...")
            print(f"Round {self.current_round} finished.")
            print(f"Plants: {len(self.habitat.plants)} | Animals: "
                  f"{len(self.habitat.animals)}")
            print(f"Used Plant-Size: {self.habitat.calculateUsedSize()}")
            print(f"Animal Capacity: {self.habitat.calculateAnimalCapacity()}")
            if (len(self.habitat.animals) == 0
                    and len(self.habitat.plants) == 0):
                print("All life in the ecosystem has perished.")
                return
            print("--------------------------------------------------")

        self.current_round += 1
        sleep(self.round_speed)


if __name__ == '__main__':

    start_plants = []

    berry_bush = BerryBush(0.2, food_value=5, regen_rate=2, id=None,
                           min_size=2, species="BerryBush", max_size=10)
    grass = Plant(1, 1, 1, id=None, species="Grass", max_size=2)

    tree = Plant(4, 2, 0.5, id=None, species="Tree", max_size=20)

    for i in range(10):
        start_plants.append(copy.deepcopy(berry_bush))
        start_plants[i].id = i+1

    for i in range(10, 30):
        start_plants.append(copy.deepcopy(grass))
        start_plants[i].id = i+1

    for i in range(30, 40):
        start_plants.append(copy.deepcopy(tree))
        start_plants[i].id = i+1

    start_animals = []

    komodo_dragon = Carnivore(True, 3, gender=False,
                              day_spawned=0, max_age=15, mating_age=3,
                              mating_start_cooldown=10, max_food=10,
                              food_consumption=2, days_to_starve=8,
                              size_mult=1.4, healing_rate=5, id=None,
                              species="Komodo_dragon", max_size=100)

    bear = Omnivore(10, gender=False, day_spawned=0,
                    max_age=50, mating_age=10, mating_start_cooldown=15,
                    max_food=15, food_consumption=3, days_to_starve=10,
                    size_mult=1.5, healing_rate=4, id=None,
                    species="Bear", max_size=150)

    deer = Herbivore(gender=False, day_spawned=0, max_age=50, mating_age=5,
                     mating_start_cooldown=5,
                     max_food=8, food_consumption=1, days_to_starve=5,
                     size_mult=1.2, healing_rate=2, id=None,
                     species="Deer", max_size=80)

    for i in range(10):
        start_animals.append(copy.deepcopy(komodo_dragon))
        start_animals[i].id = i+1
        if i % 2 == 0:
            start_animals[i].gender = True
    for i in range(10, 20):
        start_animals.append(copy.deepcopy(bear))
        start_animals[i].id = i+1
        if i % 2 == 0:
            start_animals[i].gender = True
    for i in range(20, 40):
        start_animals.append(copy.deepcopy(deer))
        start_animals[i].id = i+1
        if i % 2 == 0:
            start_animals[i].gender = True

    rounds = input("Rounds: ")
    while not rounds.isdigit():
        rounds = input("Rounds: ")
    rounds = int(rounds)
    round_speed = input("Round Speed (seconds): ")
    while not round_speed.replace('.', '', 1).isdigit():
        round_speed = input("Round Speed (seconds): ")
    round_speed = float(round_speed)
    skip_rounds = input("Skip rounds, how many(1 is full output): ")
    while not skip_rounds.isdigit():
        skip_rounds = input("Skip every ___ round:(1 is full output): ")
    skip_rounds = int(skip_rounds)
    ecosystem = Ecosystem(round_speed, 100, start_plants,
                          start_animals, skip_rounds)
    for _ in range(rounds):
        ecosystem.simulateRound()
