import unittest
from . import television


class TelevisionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.shinko = television.Television()

    def test_that_class_can_be_created(self):
        self.assertIsNotNone(self.shinko)
        self.assertIsInstance(self.shinko, television.Television)

    def test_that_television_isOn(self):
        self.shinko.power_on()
        self.assertTrue(self.shinko.is_on)

    def test_that_television_canTurnOff(self):
        self.shinko.power_off()
        self.assertFalse(self.shinko.is_on)

    def test_that_television_can_increaseVolume(self):
        self.shinko.power_on()
        self.assertTrue(self.shinko.is_on)
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.assertEqual(6, self.shinko.volume)

    def test_that_television_increasingVolumeAbove10RemainsAt10(self):
        self.shinko.power_on()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.assertEqual(10, self.shinko.volume)

    def test_that_television_can_reduce_volume(self):
        self.shinko.power_on()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.increase_volume()
        self.shinko.reduce_volume()
        self.assertEqual(4, self.shinko.volume)

    def test_that_television_decreasingVolumeBelowZeroRemainsAtZero(self):
        self.shinko.power_on()
        self.shinko.reduce_volume()
        self.assertEqual(0, self.shinko.volume)

    def test_that_television_can_mute_volume(self):
        self.shinko.power_on()
        self.shinko.increase_volume()
        self.shinko.mute_volume()
        self.assertFalse(self.shinko.volume)

    def test_that_television_can_unmute_volume(self):
        self.shinko.power_on()
        self.shinko.increase_volume()
        self.shinko.mute_volume()
        self.shinko.unmute_volume()
        self.assertTrue(self.shinko.volume)


if __name__ == '__main__':
    unittest.main()
