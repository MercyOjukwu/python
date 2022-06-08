import unittest
from chapter4 import credit_limit


class CreditLimitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = credit_limit.CreditLimit("Mercy", "12345")

    def test_that_object_exists(self):
        self.assertIsNotNone(self.account)
        self.assertIsInstance(self.account, credit_limit.CreditLimit)

    def test_that_account_hasAName(self):
        name = self.account.name
        self.assertEqual("Mercy", name)

    def test_that_account_has_accountNumber(self):
        account_no = self.account.account_no
        self.assertEqual("12345", account_no)

    def test_that_class_can_deposit_into_account(self):
        self.account.deposit(5000)
        self.assertEqual(5_000, self.account.credit_balance)

    def test_that_class_can_setCreditLimit(self):
        self.account.deposit(10_000)
        self.assertEqual(5_000, self.account.credit_limit)

    def test_that_class_buy_goods(self):
        self.account.deposit(10_000)
        self.account.buy_goods(2_000)
        self.assertEqual(8_000, self.account.credit_balance)

    def test_that_buyingGoodsAboveCreditLimit_raises_error(self):
        self.account.deposit(10_000)
        self.assertRaises(ValueError, self.account.buy_goods, 6_000)


if __name__ == '__main__':
    unittest.main()
