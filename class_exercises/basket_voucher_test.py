import unittest

from class_exercises import basket_voucher


class MyTestCase(unittest.TestCase):
    def test_that_class_can_be_created(self):
        basket = basket_voucher.Voucher(4)
        self.assertIsNotNone(basket)
        self.assertIsInstance(basket, basket_voucher.Voucher)

    def test_that_class_can_add_to_basket(self):
        basket = basket_voucher.Voucher(3)
        basket.add("Shoe")
        self.assertEqual("Shoe", basket.items)


if __name__ == '__main__':
    unittest.main()
