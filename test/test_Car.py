from unittest import TestCase
import sys
import os
test_dir = os.path.dirname(__file__)
project_dir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(test_dir, project_dir)))
from src import Car


class TestCar(TestCase):

    def setUp(self):
        print(sys.path)
        # self.car = Car()

# class TestInit(TestCar):
#     def test_initial_speed(self):
#         self.assertEqual(self.car.speed, 0)
#
#     def test_initial_odometer(self):
#         self.assertEqual(self.car.odometer, 0)
#
#     def test_initial_time(self):
#         self.assertEqual(self.car.time, 0)
#         self.assertEqual(self.car.time, 0)
#
#
# class TestAccelerate(TestCar):
#     def test_accelerate_from_zero(self):
#         self.car.accelerate()
#         self.assertEqual(self.car.speed, 5)
#
#     def test_multiple_accelerates(self):
#         for _ in range(3):
#             self.car.accelerate()
#         self.assertEqual(self.car.speed, 15)
#
