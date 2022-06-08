class AutomaticBike:
    
    def __init__(self):
        self.speed = 0
        self.is_on = None

    def power_on(self):
        self.is_on = True

    def power_off(self):
        self.is_on = False

    def accelerate(self):
        increment_by = 1
        self.speed += increment_by
        if self.speed > 20:
            self.speed = 20

    def decelerate(self):
        decrement_by = 1
        self.speed -= decrement_by
        if self.speed < 0:
            self.speed = 0
