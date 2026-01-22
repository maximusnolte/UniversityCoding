import unittest

from EPR.Übungen.ue_08.Animal import Animal
from EPR.Übungen.ue_08.Habitat import Habitat
from EPR.Übungen.ue_08.Plant import Plant


class TestHabitat(unittest.TestCase):
    def setUp(self):
        self.habitat = Habitat(size=1000)
        self.plant1 = Plant(2,5,1,id=1, species="Fern", max_size=10)
        self.plant2 = Plant(1, 2, 1, id=2, species="Moss", max_size=5)
        self.animal1 = Animal(False, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                              id=1,
                              species="Wolf",
                              max_size=100)
        self.animal2 = Animal(True, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                              id=1,
                              species="Wolf",
                              max_size=100)

    def test_spawnPlant(self):
        self.habitat.spawnPlant(self.plant1)
        self.assertIn(self.plant1, self.habitat.plants)

    def test_despawnPlant(self):
        self.habitat.spawnPlant(self.plant1)
        self.habitat.despawnPlant(self.plant1)
        self.assertNotIn(self.plant1, self.habitat.plants)
        self.habitat.despawnPlant(self.plant1)

    def test_calculateUsedSize(self):
        self.habitat.spawnPlant(self.plant1)
        self.habitat.spawnPlant(self.plant2)
        used_size = self.habitat.calculateUsedSize()
        self.assertEqual(used_size, self.plant1.size + self.plant2.size)
        self.habitat.despawnPlant(self.plant1)
        used_size = self.habitat.calculateUsedSize()
        self.assertEqual(used_size, self.plant2.size)

    def test_spawnAnimal(self):
        self.habitat.spawnAnimal(self.animal1)
        self.assertIn(self.animal1, self.habitat.animals)

    def test_despawnAnimal(self):
        self.habitat.spawnAnimal(self.animal1)
        self.habitat.despawnAnimal(self.animal1)
        self.assertNotIn(self.animal1, self.habitat.animals)
        self.habitat.despawnAnimal(self.animal1)

    def test_checkMate(self):
        self.animal1.mateable = True
        self.animal2.mateable = True
        self.assertTrue(self.habitat.checkMate(self.animal1, self.animal2))
        animal3 = Animal(True, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                         id=2,
                         species="Fox",
                         max_size=80)
        self.assertFalse(self.habitat.checkMate(self.animal1, animal3))

    def test_update_plants_cycle(self):
        self.habitat.spawnPlant(self.plant1)
        initial_size = self.plant1.size
        self.habitat.updatePlantsCycle()
        self.assertGreater(self.plant1.size, initial_size)
        for i in range(100):
            dead_plants, new_plants = self.habitat.updatePlantsCycle()


if __name__ == '__main__':
    unittest.main()

