import unittest

from . import petrol_purchase


class PetrolPurchaseTest(unittest.TestCase):
    def test_that_class_can_be_created(self):
        filling_station = petrol_purchase.PetrolPurchase("Total")
        self.assertIsNotNone(filling_station)
        self.assertIsInstance(filling_station, petrol_purchase.PetrolPurchase)

    def test_that_class_can_purchase_petrol(self):
        station = petrol_purchase.PetrolPurchase("Total")
        station.purchase("Abuja", "car diesel", 5, 100.0, 0.20)
        self.assertEqual(400, station.amount)


if __name__ == '__main__':
    unittest.main()
