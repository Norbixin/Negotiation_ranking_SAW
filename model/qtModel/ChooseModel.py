from PySide2 import QtCore
from typing import List
from model import Issue


class ChooseModel(QtCore.QAbstractTableModel):
    def __init__(self, issues: List[Issue]=[]):
        super(ChooseModel, self).__init__()
        self.__issues: List[Issue] = issues

    def rowCount(self, parent: QtCore.QModelIndex=...):
        return 1

    def columnCount(self, parent: QtCore.QModelIndex=...):
        return len(self.issues)

    def data(self, index: QtCore.QModelIndex, role: int=...):
        pass

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int=...):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.issues[section].name

    @property
    def issues(self) -> List[Issue]:
        return self.__issues
