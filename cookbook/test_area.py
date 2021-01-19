#https://stackoverflow.com/questions/8953844/import-module-from-subfolder
#relative absolute import

import unittest
from .cercle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.1),pi * 2.1 ** 2)

#in CLI python -m unittest test_area  OR  python -m unittest (thnaks to test discovery)
    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError,circle_area,3+5j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"Toto")
