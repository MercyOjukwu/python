class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount can not be negative.")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount can not be negative.")
        elif amount > self.balance:
            raise ValueError("Amount can not be greater than account balance.")
        self.balance -= amount

    def load_airtime(self, airtime_amount):
        if airtime_amount > self.balance:
            raise ValueError("Airtime amount can not be greater than account balance.")
        elif airtime_amount < 0:
            raise ValueError("Amount can not be negative.")
        self.balance -= airtime_amount

    def transfer(self, amount, account_two):
        if amount < 0:
            raise ValueError("Amount can not be negative.")
        elif amount > self.balance:
            raise ValueError("Amount can not be greater than account balance.")
        self.balance -= amount
        account_two.balance += amount
