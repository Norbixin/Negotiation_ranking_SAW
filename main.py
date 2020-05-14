# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QCoreApplication, Qt, QTranslator, QLibraryInfo
from view import Ui_MainWindow
from typing import List
from model import *
from assets import icons


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.issues: List[Issue] = []
        self.setupUi(self)


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)

    translator = QTranslator()
    translator.load("qt_pl", QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
