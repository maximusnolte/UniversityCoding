import unittest
from unittest.mock import patch

from EPR.Übungen.ue_08.Carnivore import Carnivore
from EPR.Übungen.ue_08.Herbivore import Herbivore


class TestCarnivore(unittest.TestCase):
    def setUp(self):
        self.carnivore = Carnivore(True, 4, gender=False, day_spawned=0,
                                 max_age=15,
                                 mating_age=3, mating_start_cooldown=10,
                                 max_food=10, food_consumption=2, days_to_starve=2,
                                 size_mult=1.2, healing_rate=5,
                              id=1,
                              species="Komododragon",
                              max_size=100)
        self.carnivore2 = Carnivore(True, 4, gender=False, day_spawned=0,
                                   max_age=15,
                                   mating_age=3, mating_start_cooldown=10,
                                   max_food=10, food_consumption=2,
                                   days_to_starve=2,
                                   size_mult=1.2, healing_rate=5,
                                   id=2,
                                   species="Komododragon",
                                   max_size=100)
        self.prey1 = Herbivore(gender=True, day_spawned=0, max_age=10,
                                 mating_age=2, mating_start_cooldown=5,
                                 max_food=5,
                                 food_consumption=1, days_to_starve=1,
                                 size_mult=1.4, healing_rate=3, id=3,
                                 species="Deer",
                                 max_size=80)

        self.animals = [self.carnivore, self.carnivore2, self.prey1]


    @patch("EPR.Übungen.ue_08.Carnivore.random.choice")
    @patch("EPR.Übungen.ue_08.Carnivore.random.random")
    def test_hunt(self, mock_random, mock_choice):
        self.carnivore.food_level = self.carnivore.max_food
        mock_random.return_value = 0.2
        result = self.carnivore.hunt(self.animals)
        self.assertIsNone(result)  # not hungry
        self.carnivore.food_level = 0
        result = self.carnivore.hunt([self.carnivore])
        self.assertIsNone(result) # no prey available
        mock_choice.return_value = self.prey1
        result = self.carnivore.hunt(self.animals)
        self.assertIsNone(result) # prey is too big
        self.carnivore.current_age = 10
        result = self.carnivore.hunt(self.animals)
        self.assertEqual(result, self.prey1)
        mock_random.return_value = 0.01
        result = self.carnivore.hunt(self.animals)
        self.assertEqual(self.prey1.poisoned, True)
        self.assertIsNone(result) #prey poisoned, due to failed hunt
        mock_choice.return_value = self.carnivore2
        result = self.carnivore.hunt(self.animals)
        self.assertIsNone(result) #cannot hunt same species
        self.carnivore.current_age = 1
        self.carnivore2.species = "Wolf"
        self.carnivore2.size_mult = 100
        result = self.carnivore.hunt(self.animals) #failed hunt against bigger carnivore
        self.assertEqual(result, self.carnivore)
        self.assertFalse(self.carnivore.alive)

