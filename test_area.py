print("Début de l\'exercice ".center(80,"-"))
print("Développeur : Mazen Boubaker".center(80,"-"))
print(" Utests ".center(80,"-"))

import unittest
from cercle import cercle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(cercle_area(1), pi)
        self.assertAlmostEqual(cercle_area(0), 0)
        self.assertAlmostEqual(cercle_area(2.1), pi * 2.1 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, cercle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, cercle_area, 3+5j)
        self.assertRaises(TypeError, cercle_area, True)
        self.assertRaises(TypeError, cercle_area, "toto")


