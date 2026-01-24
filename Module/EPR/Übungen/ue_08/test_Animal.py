__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import unittest

from EPR.Übungen.ue_08.Animal import Animal


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.animal1 = Animal(False, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                               id=1,
                               species="Wolf",
                               max_size=100)

    def test_eat(self):
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

    def test_getInjured(self):
        # should start at full health
        self.assertEqual(self.animal1.alive, True)
        self.assertEqual(self.animal1.health, 100)
        # should reduce health correctly
        self.animal1.getInjured(30)
        self.assertEqual(self.animal1.health, 70)
        # should die if damage exceeds current health
        self.animal1.getInjured(70)
        self.assertEqual(self.animal1.health, 0)
        self.assertEqual(self.animal1.alive, False)
        # Assuming die() sets
        # health to 0

    def test_heal(self):
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

    def test_calculateSize(self):
        # should calculate size based on age and size_mult
        self.animal1.current_age = 10
        expected_size = self.animal1.size_mult * self.animal1.current_age
        self.assertEqual(self.animal1.calculateSize(), expected_size)
        # should not exceed max_size
        self.animal1.current_age = 100
        self.assertEqual(self.animal1.calculateSize(),
                         self.animal1.max_size)

    def test_age(self):
        # should age correctly and set mateable status
        current_day = 20
        age = self.animal1.age(current_day)
        if age is not None:
            self.assertTrue(self.animal1.alive)
            self.assertEqual(age, 21)
            self.animal1.mating_cooldown = 0
            self.animal1.max_age = 22
        else:
            self.assertFalse(self.animal1.alive)  # Animal should be dead

    def test_mate(self):
        self.animal1.mateable = True
        partner = Animal(True, 0, 15, 3, 10, 10, 2, 2, 1.2, 5,
                          id=2,
                          species="Wolf",
                          max_size=100)
        partner.mateable = True
        child = self.animal1.mate(partner)
        self.assertEqual(self.animal1.species, child.species)
        (self.assertEqual(((self.animal1.max_size + partner.max_size) // 2),
         child.max_size))
        self.assertIn(child.gender, [True, False])
        self.assertEqual(child.alive, True)
        self.assertEqual(child.health, 100)
        self.assertEqual(child.food_level, child.max_food)
        self.assertEqual(child.size_mult, (self.animal1.size_mult +
                                           partner.size_mult) // 2)
        self.assertEqual(child.poisoned, False)
        self.assertEqual(child.food_consumption, self.animal1.food_consumption)
        self.assertEqual(child.days_to_starve, self.animal1.days_to_starve)
        self.assertEqual(child.day_spawned, None)
        self.assertEqual(child.max_age, (self.animal1.max_age +
                                         partner.max_age) // 2)

        self.assertEqual(child.current_age, 1)
        self.assertEqual(child.mateable, False)
        self.assertEqual(child.mating_age, self.animal1.mating_age)
        self.assertEqual(child.mating_start_cooldown,
                         child.mating_start_cooldown)


if __name__ == '__main__':
    unittest.main()
