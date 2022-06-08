class PetrolPurchase:
    def __init__(self, name):
        self.amount = 0
        self.name = name
        self.location = "Abuja"
        self.petrol_type = "Car Diesel"

    def purchase(self, location, petrol_type, quantity_in_litres, price_per_litre, percent_discount):
        self.petrol_type = petrol_type
        self.location = location
        self.amount = quantity_in_litres * price_per_litre - (percent_discount * quantity_in_litres * price_per_litre)
