from PySide2 import QtCore
from typing import List
from model import Issue
import typing


class IssueModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, issues: List[Issue]=[], **kwargs):
        super(IssueModel, self).__init__(*args, **kwargs)
        self.__issues: List[Issue] = issues
        self.__column_names: List[str] = ["Kwestia", "Ocena"]

    def rowCount(self, parent: QtCore.QModelIndex=...):
        return len(self.issues)

    def columnCount(self, parent: QtCore.QModelIndex=...):
        return 2

    def data(self, index: QtCore.QModelIndex, role: int=...):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return self.issues[index.row()].name
            elif index.column() == 1:
                return self.issues[index.row()].rating

    def setData(self, index: QtCore.QModelIndex, value: typing.Any, role: int=...):
        if role == QtCore.Qt.EditRole:
            try:
                int(value)
                self.issues[index.row()].rating = min(max(int(value), 0), 100)
                return True
            except ValueError:
                return False

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int=...):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.column_names[section]

    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
        elif index.column() == 1:
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def sort(self, column: int, order: QtCore.Qt.SortOrder=...):
        if column == 0:
            if order == QtCore.Qt.AscendingOrder:
                self.issues.sort(key=lambda option: option.name)
            elif order == QtCore.Qt.DescendingOrder:
                self.issues.sort(key=lambda option: option.name, reverse=True)
        elif column == 1:
            if order == QtCore.Qt.AscendingOrder:
                self.issues.sort(key=lambda option: option.rating)
            elif order == QtCore.Qt.DescendingOrder:
                self.issues.sort(key=lambda option: option.rating, reverse=True)
        self.layoutChanged.emit()

    @property
    def issues(self) -> List[Issue]:
        return self.__issues

    @issues.setter
    def issues(self, value):
        self.__issues = value

    @property
    def column_names(self) -> List[str]:
        return self.__column_names
