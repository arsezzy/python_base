#!/usr/bin/python3

from abc import ABC, abstractmethod


class Clother(ABC):
    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clother):
    def __init__(self, param):
        self.size = param

    @property
    def get_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clother):
    def __init__(self, param):
        self.height = param

    @property
    def get_consumption(self):
        return 2 * self.height + 0.3


coat1 = Coat(13)
print(f"coat1 size is {coat1.size}")
print(f"consumtion for coat1 is {coat1.get_consumption}")
suit1 = Suit(170)
print(f"suit1 height is {suit1.height}")
print(f"consumtions for suit1 is {suit1.get_consumption}")

