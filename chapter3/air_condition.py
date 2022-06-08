class AirConditioner:

    def __init__(self):
        self.temperature = 16
        self.is_on = None

    def power_on(self):
        self.is_on = True

    def power_off(self):
        self.is_on = False

    def increase_temp(self):
        increment_by = 1
        self.temperature += increment_by
        if self.temperature > 30:
            self.temperature = 30

    def decrease_temp(self):
        decrement_by = 1
        self.temperature -= decrement_by
        if self.temperature < 16:
            self.temperature = 16
