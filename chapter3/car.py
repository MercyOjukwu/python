class AutoCar:
    def __init__(self):
        self.is_on = False

    def power_on(self):
        self.is_on = True

    def power_off(self):
        return self.is_on

