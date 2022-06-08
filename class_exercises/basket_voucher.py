class Voucher:
    def __init__(self, voucher_limit):

        self.items = None
        self.voucher_limit = voucher_limit

    def add(self, item):
        basket = []
        self.voucher_limit = len(basket)
        self.items = item
        basket.append(item)
