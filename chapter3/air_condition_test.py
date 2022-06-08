import unittest
from . import air_condition


class AirConditionerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.blueRay = air_condition.AirConditioner()

    def test_that_can_object_exists_in_class(self):
        self.assertIsNotNone(self.blueRay)
        self.assertIsInstance(self.blueRay, air_condition.AirConditioner)

    def test_that_airCondition_can_turnOn(self):
        self.blueRay.power_on()
        self.assertTrue(self.blueRay.is_on)

    def test_that_airConditioner_can_turnOff(self):
        self.blueRay.power_on()
        self.blueRay.power_off()
        self.assertFalse(self.blueRay.is_on)

    def test_that_airConditioner_can_increaseTemperature(self):
        self.blueRay.power_on()
        self.blueRay.increase_temp()
        self.assertEqual(17, self.blueRay.temperature)

    def test_that_airConditionerIncreasingTemperatureAboveThirty_remainsAt30(self):
        self.blueRay.power_on()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.assertEqual(30, self.blueRay.temperature)

    def test_that_airConditioner_can_decrease_temperature(self):
        self.blueRay.power_on()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.increase_temp()
        self.blueRay.decrease_temp()
        self.assertEqual(18, self.blueRay.temperature)

    def test_that_airConditionerDecreasingTemperatureBelow16_remainsAt16(self):
        self.blueRay.power_on()
        self.blueRay.decrease_temp()
        self.assertEqual(16, self.blueRay.temperature)


if __name__ == '__main__':
    unittest.main()
