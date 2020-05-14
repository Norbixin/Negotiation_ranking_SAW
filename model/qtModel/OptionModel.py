from PySide2 import QtCore
from typing import List
from model import Issue
import typing


class OptionModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, issues: List[Issue]=[], **kwargs):
        super(OptionModel, self).__init__(*args, **kwargs)
        self.__issues: List[Issue] = issues
        self.__issue_selected: int = -1

    def rowCount(self, parent: QtCore.QModelIndex=...):
        if self.issue_selected == -1:
            return 0
        return len(self.issues[self.issue_selected].options)

    def columnCount(self, parent: QtCore.QModelIndex=...):
        return 2

    def data(self, index: QtCore.QModelIndex, role: int=...):
        if role == QtCore.Qt.DisplayRole and self.issue_selected != -1:
            if index.column() == 0:
                return self.issues[self.issue_selected].options[index.row()].name
            elif index.column() == 1:
                return self.issues[self.issue_selected].options[index.row()].rating

    def setData(self, index: QtCore.QModelIndex, value: typing.Any, role: int=...):
        if role == QtCore.Qt.EditRole:
            try:
                int(value)
                self.issues[self.issue_selected].options[index.row()].rating = \
                    min(max(int(value), 0), self.issues[self.issue_selected].rating)
                return True
            except ValueError:
                return False

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int=...):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            if section == 0:
                return "Opcja"
            elif section == 1:
                return "Ocena"

    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def sort(self, column: int, order: QtCore.Qt.SortOrder=...):
        if self.issue_selected == -1:
            return
        if column == 0:
            if order == QtCore.Qt.AscendingOrder:
                self.issues[self.issue_selected].options.sort(key=lambda option: option.name)
            elif order == QtCore.Qt.DescendingOrder:
                self.issues[self.issue_selected].options.sort(key=lambda option: option.name, reverse=True)
        elif column == 1:
            if order == QtCore.Qt.AscendingOrder:
                self.issues[self.issue_selected].options.sort(key=lambda option: option.rating)
            elif order == QtCore.Qt.DescendingOrder:
                self.issues[self.issue_selected].options.sort(key=lambda option: option.rating, reverse=True)
        self.layoutChanged.emit()

    @property
    def issue_selected(self) -> int:
        return self.__issue_selected

    @issue_selected.setter
    def issue_selected(self, value):
        self.__issue_selected = value

    @property
    def issues(self) -> List[Issue]:
        return self.__issues
