import unittest

from EPR.Übungen.ue_08.Herbivore import Herbivore
from EPR.Übungen.ue_08.Plant import Plant


class TestHerbivore(unittest.TestCase):

    def setUp(self):
        self.herbivore = Herbivore(gender=True, day_spawned=0, max_age=10,
                                 mating_age=2, mating_start_cooldown=5,
                                 max_food=5,
                                 food_consumption=1, days_to_starve=1,
                                 size_mult=1.0, healing_rate=3, id=3,
                                 species="Deer",
                                 max_size=80)

    def test_searchFood(self):
        self.plant1 = Plant(2, 5, 1, id=1, species="Fern", max_size=10)
        self.plant2 = Plant(1, 2, 1, id=2, species="Moss", max_size=5)
        self.plants = [self.plant1, self.plant2]
        val = self.herbivore.searchFood(self.plants)
        self.assertIsNone(val) # Herbivore is not hungry.
        self.herbivore.food_level = 0
        val = self.herbivore.searchFood(self.plants)
        self.assertIsNotNone(val)  # Herbivore should eat something

if __name__ == '__main__':
    unittest.main()