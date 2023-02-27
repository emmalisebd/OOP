import random
# class definition file - only save don't run
# The Coin class simulates a coin that can
# be flipped.


class Coin:  # name of class should start with upper case letter
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):     # init creates attributes for the object
        self.__sideup = 'Heads'  # setting value of sideup to Heads
        # __ make the attribute hidden/private - must change them all to private for consistency

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
        return self.__sideup

        # get / accessor methods return the value of an attribute
