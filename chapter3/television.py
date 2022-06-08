class Television:
    def __init__(self):
        self.volume = 0
        self.is_on = None

    def power_on(self):
        self.is_on = True

    def power_off(self):
        self.is_on = False

    def increase_volume(self):
        incrementing_step = 2
        self.volume += incrementing_step
        if self.volume > 10:
            self.volume = 10

    def reduce_volume(self):
        reduction_step = 2
        self.volume -= reduction_step
        if self.volume < 0:
            self.volume = 0

    def mute_volume(self):
        self.volume = 0

    def unmute_volume(self):
        self.volume = True
