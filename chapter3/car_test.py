import unittest
from . import car


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.volvo = car.AutoCar()

    def test_that_class_can_be_created(self):
        self.assertIsNotNone(self.volvo)  # add assertion here
        self.assertIsInstance(self.volvo, car.AutoCar)

    def test_that_car_can_power_on(self):
        self.volvo.power_on()
        self.assertTrue(self.volvo.is_on)

    def test_that_car_can_power_off(self):
        self.volvo.power_off()
        self.assertFalse(self.volvo.is_on)


if __name__ == '__main__':
    unittest.main()
