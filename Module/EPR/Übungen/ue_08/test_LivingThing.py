__author__ = "8722674, Nolte, 8729305, Dmytryszyn"

import unittest

from EPR.Übungen.ue_08.LivingThing import LivingThing


class TestLivingThing(unittest.TestCase):
    def setUp(self):
        self.livingthing1 = LivingThing(1, "Human", 180)
        self.assertEqual(self.livingthing1.alive, True)
        self.assertEqual(self.livingthing1.id, 1)
        self.assertEqual(self.livingthing1.species, "Human")
        self.assertEqual(self.livingthing1.max_size, 180)

    def test_die(self):
        self.livingthing1.alive = True
        self.assertEqual(self.livingthing1.alive, True)
        result = self.livingthing1.die()
        self.assertEqual(self.livingthing1.alive, False)
        self.assertEqual(result, "1 has died.")


if __name__ == '__main__':
    unittest.main()
