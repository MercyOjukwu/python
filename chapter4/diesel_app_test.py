import unittest
from . import diesel_app


class DieselAppTest(unittest.TestCase):
    def setUp(self) -> None:
        self.diesel = diesel_app.DieselApp()

    def test_object_exists_in_class(self):
        self.assertIsNotNone(self.diesel)
        self.assertIsInstance(self.diesel, diesel_app.DieselApp)

    def test_that_class_can_calculate_amountOfPetrolUsed(self):
        self.diesel.calculateAmountOfPetrol(5)
        self.assertEqual(500, self.diesel.total_amount)


if __name__ == '__main__':
    unittest.main()
