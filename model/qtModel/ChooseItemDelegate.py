from PySide2 import QtWidgets
from typing import List
from model import Issue


class ComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, column: int=0, **kwargs):
        super(ComboBox, self).__init__(*args, **kwargs)
        self.__column: int = column

    @property
    def column(self):
        return self.__column


class ChooseItemDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent, issues: List[Issue]=[]):
        QtWidgets.QItemDelegate.__init__(self, parent)
        self.__issues: List[Issue] = issues
        self.__refreshed_widgets: int = 0

    def paint(self, painter, option, index):
        combo_box = ComboBox(self.parent(), column=index.column())

        options = []
        for option in self.issues[index.column()].options:
            options.append(option.name)

        combo_box.addItems(options)
        combo_box.currentIndexChanged.connect(self.parent().currentIndexChanged)

        if not self.parent().indexWidget(index) or self.parent().updateWidgets:
            self.parent().setIndexWidget(index, combo_box)
            self.refreshed_widgets += 1
            if self.refreshed_widgets == len(self.issues):
                self.parent().updateWidgets = False
                self.__refreshed_widgets = 0

    @property
    def issues(self) -> List[Issue]:
        return self.__issues

    @property
    def refreshed_widgets(self) -> int:
        return self.__refreshed_widgets

    @refreshed_widgets.setter
    def refreshed_widgets(self, value):
        self.__refreshed_widgets = value
