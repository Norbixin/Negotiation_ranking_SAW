from PySide2 import QtWidgets, QtCore
from typing import List
from model import Issue, Offer, Option
from .ChooseItemDelegate import ChooseItemDelegate


class ChooseTableView(QtWidgets.QTableView):
    updateScore = QtCore.Signal(int)

    def __init__(self, *args, issues: List[Issue]=[], **kwargs):
        QtWidgets.QTableView.__init__(self, *args, **kwargs)
        self.__issues: List[Issue] = issues
        self.__offer: Offer = Offer()
        self.__update_widgets: bool = True
        self.setItemDelegateForRow(0, ChooseItemDelegate(self, issues=issues))
        self.update_offer()

    @QtCore.Slot()
    def currentIndexChanged(self, row: int):
        if len(self.offer.options) < len(self.issues):
            self.update_offer()
        column = self.sender().column
        self.offer.options.pop(column)
        self.offer.options.insert(column, self.issues[column].options[row])
        self.offer.calculate_rating()
        self.updateScore.emit(self.offer.rating)

    @property
    def issues(self):
        return self.__issues

    @property
    def offer(self):
        return self.__offer

    @offer.setter
    def offer(self, value):
        self.__offer = value

    @property
    def update_widgets(self):
        return self.__update_widgets

    @update_widgets.setter
    def update_widgets(self, value):
        self.__update_widgets = value

    def update_offer(self):
        self.__offer = Offer()
        for issue in self.issues:
            if len(issue.options) == 0:
                self.offer.add_option(Option(""))
            else:
                self.offer.add_option(issue.options[0])
        self.offer.calculate_rating()
