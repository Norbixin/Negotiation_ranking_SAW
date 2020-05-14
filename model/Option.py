class Option:
    def __init__(self, name: str):
        self.__rating: int = 0
        self.__name: str = name

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, value: int):
        self.__rating = value

    @property
    def name(self) -> str:
        return self.__name
