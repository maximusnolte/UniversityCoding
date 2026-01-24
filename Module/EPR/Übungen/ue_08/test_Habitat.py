__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import unittest
from unittest.mock import patch

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.Carnivore import Carnivore
from EPR.Übungen.ue_08.Habitat import Habitat
from EPR.Übungen.ue_08.Herbivore import Herbivore
from EPR.Übungen.ue_08.Plant import Plant


class TestHabitat(unittest.TestCase):
    def setUp(self):
        self.habitat = Habitat(1000, [], [], 0)
        self.plant1 = Plant(2, 5, 1, id=1, species="Fern", max_size=10)
        self.plant2 = Plant(1, 2, 1, id=2, species="Moss", max_size=5)
        self.animal1 = Carnivore(False, 4, gender=False, day_spawned=0,
                                 max_age=15,
                                 mating_age=3, mating_start_cooldown=10,
                                 max_food=10, food_consumption=2,
                                 days_to_starve=2,
                                 size_mult=1.2, healing_rate=5,
                                 id=1,
                                 species="Wolf",
                                 max_size=100)
        self.animal2 = Carnivore(False, 4, gender=True, day_spawned=0,
                                 max_age=15,
                                 mating_age=3, mating_start_cooldown=10,
                                 max_food=10, food_consumption=2,
                                 days_to_starve=2,
                                 size_mult=1.2, healing_rate=5,
                                 id=2,
                                 species="Wolf",
                                 max_size=100)
        self.animal3 = Herbivore(gender=True, day_spawned=0, max_age=10,
                                 mating_age=2, mating_start_cooldown=5,
                                 max_food=5,
                                 food_consumption=1, days_to_starve=1,
                                 size_mult=1.4, healing_rate=3, id=3,
                                 species="Deer",
                                 max_size=80)

    def cleanup(self):
        self.habitat.despawnAnimal(self.animal1)
        self.habitat.despawnAnimal(self.animal2)
        self.habitat.despawnAnimal(self.animal3)
        self.habitat.despawnPlant(self.plant1)
        self.habitat.despawnPlant(self.plant2)

    def test_01_spawnPlant(self):
        self.habitat.spawnPlant(self.plant1)
        self.assertIn(self.plant1, self.habitat.plants)

    def test_02_despawnPlant(self):
        self.habitat.spawnPlant(self.plant1)
        self.habitat.despawnPlant(self.plant1)
        self.assertNotIn(self.plant1, self.habitat.plants)
        self.habitat.despawnPlant(self.plant1)

    def test_03_calculateUsedSize(self):
        self.habitat.spawnPlant(self.plant1)
        self.habitat.spawnPlant(self.plant2)
        used_size = self.habitat.calculateUsedSize()
        self.assertEqual(used_size, self.plant1.size + self.plant2.size)
        self.habitat.despawnPlant(self.plant1)
        used_size = self.habitat.calculateUsedSize()
        self.assertEqual(used_size, self.plant2.size)

    def test_04_spawnAnimal(self):
        self.habitat.spawnAnimal(self.animal1)
        self.assertIn(self.animal1, self.habitat.animals)

    def test_05_despawnAnimal(self):
        self.habitat.spawnAnimal(self.animal1)
        self.habitat.despawnAnimal(self.animal1)
        self.assertNotIn(self.animal1, self.habitat.animals)
        self.habitat.despawnAnimal(self.animal1)

    def test_06_checkMate(self):
        self.animal1.mateable = True
        self.animal2.mateable = True
        self.assertTrue(self.habitat.checkMate(self.animal1, self.animal2))
        animal3 = Animal(True, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                         id=2,
                         species="Fox",
                         max_size=80)
        self.assertFalse(self.habitat.checkMate(self.animal1, animal3))

    def test_07_updatePlantsCycle(self):
        self.habitat.spawnPlant(self.plant1)
        initial_size = self.plant1.size
        self.habitat.updatePlantsCycle()
        self.assertGreater(self.plant1.size, initial_size)

    def test_08_starvation(self):
        dead_animals = []
        self.assertTrue(self.animal1.alive)
        self.habitat.handle_starvation(self.animal1, dead_animals)
        self.assertEqual(self.animal1.food_level, self.animal1.max_food -
                         self.animal1.food_consumption)
        self.assertNotIn(self.animal1, dead_animals)
        self.animal1.food_level = 1
        self.habitat.handle_starvation(self.animal1, dead_animals)
        self.assertIn(self.animal1, dead_animals)
        self.assertFalse(self.animal1.alive)

    def test_09_handle_cooldowns_and_heal(self):
        self.animal1.mating_cooldown = 2
        self.habitat.handle_cooldowns_and_heal(self.animal1)
        self.assertEqual(self.animal1.mating_cooldown, 1)
        self.animal1.health = 5
        self.habitat.handle_cooldowns_and_heal(self.animal1)
        self.assertGreater(self.animal1.health, 5)

    @patch("EPR.Übungen.ue_08.Carnivore.random.random")
    def test_10_handle_hunting_or_eating(self, mock_carnivore_random):
        # Carnivore hunts herbivore, more tests for hunting in Carnivore tests
        dead_animals = []
        mock_carnivore_random.return_value = 0.5
        self.habitat.spawnAnimal(self.animal1)
        self.habitat.spawnAnimal(self.animal3)

        self.animal1.current_age = 1
        self.animal1.food_level = 0
        val = self.habitat.handle_hunting_or_eating(self.animal1,  # carnivore
                                                    # too small to hunt prey
                                                    dead_animals)
        self.assertNotIn(self.animal3, dead_animals)
        self.animal1.current_age = self.animal1.max_age
        val = self.habitat.handle_hunting_or_eating(self.animal1,
                                                    dead_animals)
        self.assertIn(self.animal3, dead_animals)

        # Herbivore eats plant, more tests for eating in Herbivore tests
        self.habitat.spawnAnimal(self.animal3)
        self.habitat.spawnPlant(self.plant1)
        self.plant1.size = self.plant1.max_size
        self.habitat.handle_hunting_or_eating(self.animal3, dead_animals)
        self.animal3.food_level = 0
        self.habitat.handle_hunting_or_eating(self.animal3, dead_animals)
        self.assertGreater(self.animal3.food_level, 0)
        self.assertLess(self.plant1.size, self.plant1.max_size)
        self.plant1.size = self.plant1.min_size
        self.animal3.food_level = 0
        self.habitat.handle_hunting_or_eating(self.animal3, dead_animals)
        self.assertGreater(self.animal3.food_level, 0)
        self.assertFalse(self.plant1.alive)

    @patch("EPR.Übungen.ue_08.Animal.random.random")
    def test_11_handle_aging(self, mock_animal_random):
        # More tests for aging in Animal tests
        dead_animals = []
        new_animals = []
        current_day = 10

        self.habitat.spawnAnimal(self.animal3)
        mock_animal_random.return_value = 0.5
        self.habitat.handle_aging_and_mating(self.animal3,
                                             current_day,
                                             dead_animals,
                                             new_animals)
        mock_animal_random.return_value = 0.4
        self.habitat.handle_aging_and_mating(self.animal3,
                                             current_day + 1,
                                             dead_animals,
                                             new_animals)
        self.assertIn(self.animal3, dead_animals)

    @patch("EPR.Übungen.ue_08.Habitat.random.random")
    def test_12_handle_mating(self, mock_habitat_random):
        dead_animals = []
        new_animals = []
        current_day = 10
        self.habitat.spawnAnimal(self.animal1)
        self.habitat.spawnAnimal(self.animal2)
        self.animal1.mateable = True
        self.animal1.gender = False
        self.animal2.mateable = True
        mock_habitat_random.return_value = 0.3
        self.habitat.handle_aging_and_mating(self.animal1,
                                             current_day,
                                             dead_animals,
                                             new_animals)
        self.assertGreater(len(new_animals), 0)

        new_animals = []
        self.habitat.despawnAnimal(self.animal2)
        self.habitat.handle_aging_and_mating(self.animal1,
                                             current_day,
                                             dead_animals,
                                             new_animals)
        self.assertEqual(len(new_animals), 0)

    def test_13_handle_animal(self):
        self.animal1.alive = False
        self.habitat.spawnAnimal(self.animal1)
        dead_animals, new_animals = self.habitat.update_animals_cycle(10)
        self.assertIn(self.animal1, dead_animals)

    def test_14_apply_spawns_despawns(self):
        self.habitat.spawnAnimal(self.animal1)
        dead_animals = [self.animal1]
        new_animals = [self.animal2]
        self.habitat.spawnPlant(self.plant1)
        dead_plants = [self.plant1]
        new_plants = [self.plant2]
        self.habitat.apply_spawns_despawns(dead_plants, dead_animals,
                                           new_plants, new_animals)
        self.assertNotIn(self.animal1, self.habitat.animals)
        self.assertIn(self.animal2, self.habitat.animals)

        self.assertNotIn(self.plant1, self.habitat.plants)
        self.assertIn(self.plant2, self.habitat.plants)
        self.assertEqual(dead_animals, [])
        self.assertEqual(dead_plants, [])
        self.assertEqual(new_animals, [])
        self.assertEqual(new_plants, [])


if __name__ == '__main__':
    unittest.main()
