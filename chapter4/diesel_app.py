class DieselApp:
    def __init__(self):
        self.total_amount = 0

    def calculateAmountOfPetrol(self, no_of_litres):
        price_per_litre = 100
        self.total_amount = no_of_litres * price_per_litre
