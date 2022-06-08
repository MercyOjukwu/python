class CreditLimit:
    def __init__(self, name, account_no):
        self.credit_balance = 0
        self.credit_limit = 0
        self.account_no = account_no
        self.name = name

    def deposit(self, amount):
        self.credit_balance += amount
        self.credit_limit = self.credit_balance // 2

    def buy_goods(self, amount):
        self.credit_balance -= amount
        if amount > self.credit_limit:
            raise ValueError("Credit Limit exceeded")
