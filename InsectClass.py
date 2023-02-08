import random
# class def file


class Insect:

    def __init__(self):
        self.wings = '2'
        self.legs = '4'
        self.flight = 0

    def len_flight(self):
        if random.randint(0, 10):
