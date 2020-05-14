from .Option import Option
from typing import List


class Issue:
    def __init__(self, name: str):
        self.__rating: int = 0
        self.__options: List[Option] = []
        self.__name: str = name

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, value: int):
        self.__rating = value

    @property
    def options(self) -> List[Option]:
        return self.__options

    @property
    def name(self) -> str:
        return self.__name

    def add_option(self, option: Option):
        self.options.append(option)

    def validate(self) -> bool:
        return min(self.options) == 0 and max(self.options) == self.rating
