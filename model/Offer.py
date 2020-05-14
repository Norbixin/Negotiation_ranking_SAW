from .Option import Option
from typing import List


class Offer:
    def __init__(self):
        self.__options: List[Option] = []
        self.__rating: int = 0

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def options(self) -> List[Option]:
        return self.__options

    def add_option(self, option: Option):
        self.options.append(option)

    def calculate_rating(self):
        self.__rating = 0
        for option in self.options:
            self.rating += option.rating

    def __copy__(self):
        copied_offer = Offer()
        copied_offer.rating = self.rating
        for option in self.options:
            copied_offer.add_option(option)
        return copied_offer
