import unittest

from class_exercises.account import Account
from . import account


class AccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account_one = Account("Mary")
        self.account_two = Account("Joseph")

    def test_that_account_can_be_created(self):
        self.assertIsNotNone(self.account_one)
        self.assertIsInstance(self.account_one, account.Account)

    def test_that_account_has_a_name(self):
        name = self.account_one.name
        self.assertEqual("Mary", name)

    def test_that_account_can_deposit(self):
        self.account_one.deposit(2000)
        self.assertEqual(2000, self.account_one.balance)

    def test_that_negative_raises_error(self):
        self.assertRaises(ValueError, self.account_one.deposit, -1000)
        self.assertEqual(0, self.account_one.balance)

    def test_that_account_withdraw(self):
        self.account_one.deposit(5000)
        self.account_one.withdraw(2000)
        self.assertEqual(3000, self.account_one.balance)

    def test_that_negativeWithdrawAmount_raises_error(self):
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.withdraw, -1000)

    def test_that_withdrawAmountGreaterThanBalance_raises_error(self):
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.withdraw, 10_000)

    def test_that_account_can_load_airtime(self):
        self.account_one.deposit(2000)
        self.account_one.load_airtime(500)

        self.assertEqual(1500, self.account_one.balance)

    def test_that_loadingAirtimeAmountMoreThanBalance_raises_error(self):
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.load_airtime, 10_000)

    def test_that_loadingNegativeAirtimeAmount_raises_error(self):
        self.account_one = account.Account("Mercy")
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.load_airtime, -2000)

    def test_that_account_can_transfer(self):
        self.account_one.deposit(5_000)
        self.account_one.transfer(2_000, self.account_two)
        self.assertEqual(3_000, self.account_one.balance)
        self.assertEqual(2_000, self.account_two.balance)

    def test_that_accountTransferringNegativeValue_raises_error(self):
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.transfer, -1000, self.account_two)

    def test_that_accountTransferringAmountGreaterThanBalance_raises_error(self):
        self.account_one.deposit(5000)
        self.assertRaises(ValueError, self.account_one.transfer, 10_000, self.account_two)


if __name__ == '__main__':
    unittest.main()
