__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import unittest

from EPR.Übungen.ue_08.Plant import Plant


class PlantTest(unittest.TestCase):
    def setUp(self):
        self.plant1 = Plant(1, 2, 3, id=1, max_size=10, species="Fern")
        self.assertEqual(self.plant1.species, "Fern")
        self.assertEqual(self.plant1.id, 1)
        self.assertEqual(self.plant1.size, 1)
        self.assertEqual(self.plant1.min_size, 1)
        self.assertEqual(self.plant1.food_value, 2)
        self.assertEqual(self.plant1.regen_rate, 3)
        self.assertEqual(self.plant1.max_size, 10)

    def test_regenerate(self):
        self.plant1.regenerate()
        self.assertEqual(self.plant1.size, 4)
        self.plant1.size = 9
        self.plant1.regenerate()
        self.assertEqual(self.plant1.size, 10)

    def test_getEaten(self):
        self.plant1.regenerate()
        self.plant1.getEaten(2)
        self.assertEqual(self.plant1.size, 2)
        self.plant1.getEaten(2)
        self.assertFalse(self.plant1.alive)
        self.plant1.regenerate()
        self.assertEqual(self.plant1.size, 0)  # Dead plants do not regenerate
        self.assertFalse(self.plant1.alive)

    def test_reproduce(self):
        self.plant1.size = 10
        offspring = self.plant1.reproduce()
        if offspring is not None:
            self.assertIsInstance(offspring, Plant)
            self.assertEqual(offspring.species, "Fern")
            self.assertEqual(offspring.min_size, 1)
            self.assertEqual(offspring.food_value, 2)
            self.assertEqual(offspring.regen_rate, 3)
            self.assertEqual(offspring.max_size, 10)
        else:
            self.assertIsNone(offspring)

if __name__ == '__main__':
    unittest.main()