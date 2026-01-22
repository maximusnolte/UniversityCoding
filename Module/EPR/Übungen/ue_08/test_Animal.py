import unittest

from EPR.Übungen.ue_08.Animal import Animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.animal1 = Animal( False, 0, 15, 3, 0, 10, 2, 2, 1.2, 5,
                               id = 1,
                               species="Wolf",
                               max_size=100)

    def test_animal_eat(self):
        # should start at max_food
        self.assertEqual(self.animal1.food_level, self.animal1.max_food)
        # should not exceed max_food
        self.animal1.eat(5)
        self.assertNotEqual(self.animal1.food_level, self.animal1.max_food +
                            5)
        # should be max_food now
        self.animal1.food_level -= 5
        self.animal1.eat(5)
        self.assertEqual(self.animal1.food_level, self.animal1.max_food)

    def test_animal_get_injured(self):
        # should start at full health
        self.assertEqual(self.animal1.alive, True)
        self.assertEqual(self.animal1.health, 100)
        # should reduce health correctly
        self.animal1.getInjured(30)
        self.assertEqual(self.animal1.health, 70)
        # should die if damage exceeds current health
        self.animal1.getInjured(70)
        self.assertEqual(self.animal1.health, 0)
        self.assertEqual(self.animal1.alive, False)# Assuming die() sets
        # health to 0

    def test_animal_heal(self):
        # should heal if food level is sufficient and not poisoned
        self.animal1.health = 50
        self.animal1.food_level = self.animal1.max_food
        self.animal1.heal()
        self.assertEqual(self.animal1.health, 55)  # healing_rate is 5
        # should not exceed max health
        self.animal1.health = 99
        self.animal1.heal()
        self.assertEqual(self.animal1.health, 100)
        # should lose health if food level is low
        self.animal1.health = 50
        self.animal1.poisoned = True
        self.animal1.heal()
        self.assertEqual(self.animal1.health, 45)  # healing_rate is 5

    def test_animal_calculateSize(self):
        # should calculate size based on age and size_mult
        self.animal1.current_age = 10
        expected_size = self.animal1.size_mult * self.animal1.current_age
        self.assertEqual(self.animal1.calculateSize(), expected_size)
        # should not exceed max_size
        self.animal1.current_age = 100
        self.assertEqual(self.animal1.calculateSize(),
                         self.animal1.max_size)

    def test_animal_age(self):
        pass

