from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_cons(self):
        pass

    def total_material(self, *args):
        """args - objects Clothes's classes"""
        total = 0
        for cloth in args:
            total += cloth.fabric_cons
        return total


class Coat(Clothes):

    @property
    def fabric_cons(self):
        return self.param / 6.5 + 0.5

class Suit(Clothes):

    @property
    def fabric_cons(self):
        return self.param * 2 + 0.3




coat = Coat(43)
suit = Suit(183)
print(coat.fabric_cons)
print(suit.fabric_cons)
print(coat.total_material(coat, suit))