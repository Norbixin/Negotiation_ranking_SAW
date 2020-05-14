# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, Qt, Slot)
from PySide2.QtWidgets import *
from model import *
from model.qtModel import *
from data import Parser
from .NewTemplateDialog import Ui_Dialog


class NewTemplateDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(NewTemplateDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)


class Delegate(QtWidgets.QItemDelegate):
    def __init__(self, owner, items):
        super(Delegate, self).__init__(owner)
        self.items = items

    def createEditor(self, parent, option, index):
        self.editor = QtGui.QComboBox(parent)
        self.editor.addItems(self.items)
        return self.editor

    def paint(self, painter, option, index):
        value = index.data(QtCore.Qt.DisplayRole).toString()
        style = QtGui.QApplication.style()
        opt = QtGui.QStyleOptionComboBox()
        opt.text = str(value)
        opt.rect = option.rect
        style.drawComplexControl(QtGui.QStyle.CC_ComboBox, opt, painter)
        QtGui.QItemDelegate.paint(self, painter, option, index)

    def setEditorData(self, editor, index):
        value = index.data(QtCore.Qt.DisplayRole).toString()
        num = self.items.index(value)
        editor.setCurrentIndex(num)

    def setModelData(self, editor, model, index):
        value = editor.currentText()
        model.setData(index, QtCore.Qt.DisplayRole, QtCore.QVariant(value))

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)

        app_icon = QtGui.QIcon()
        app_icon.addFile(':/assets/16.png', QtCore.QSize(16, 16))
        app_icon.addFile(':/assets/24.png', QtCore.QSize(24, 24))
        app_icon.addFile(':/assets/32.png', QtCore.QSize(32, 32))
        app_icon.addFile(':/assets/48.png', QtCore.QSize(48, 48))
        app_icon.addFile(':/assets/256.png', QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)

        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setIcon(QtGui.QIcon(QStyle.standardIcon(MainWindow.style(), QStyle.SP_FileDialogNewFolder)))
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setIcon(QtGui.QIcon(QStyle.standardIcon(MainWindow.style(), QStyle.SP_DialogSaveButton)))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setIcon(QtGui.QIcon(QStyle.standardIcon(MainWindow.style(), QStyle.SP_DirOpenIcon)))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.ratings = QWidget()
        self.ratings.setObjectName(u"ratings")
        self.gridLayout = QGridLayout(self.ratings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.deleteIssue = QPushButton(self.ratings)
        self.deleteIssue.setObjectName(u"deleteIssue")

        self.gridLayout.addWidget(self.deleteIssue, 1, 0, 1, 1)

        self.deleteOption = QPushButton(self.ratings)
        self.deleteOption.setObjectName(u"deleteOption")

        self.gridLayout.addWidget(self.deleteOption, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.issueName = QLineEdit(self.ratings)
        self.issueName.setObjectName(u"issueName")

        self.horizontalLayout.addWidget(self.issueName)

        self.addIssue = QPushButton(self.ratings)
        self.addIssue.setObjectName(u"addIssue")

        self.horizontalLayout.addWidget(self.addIssue)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.optionName = QLineEdit(self.ratings)
        self.optionName.setObjectName(u"optionName")

        self.horizontalLayout_2.addWidget(self.optionName)

        self.addOption = QPushButton(self.ratings)
        self.addOption.setObjectName(u"addOption")

        self.horizontalLayout_2.addWidget(self.addOption)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.issueModel = IssueModel(issues=self.issues)
        self.issueTable = QTableView(self.ratings)
        self.issueTable.setObjectName(u"issueTable")
        self.issueTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.issueTable.setModel(self.issueModel)
        self.issueTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.issueTable.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.issueTable.setSortingEnabled(True)

        self.gridLayout.addWidget(self.issueTable, 0, 0, 1, 1)

        self.optionModel = OptionModel(issues=self.issues)
        self.optionTable = QTableView(self.ratings)
        self.optionTable.setObjectName(u"optionTable")
        self.optionTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.optionTable.setModel(self.optionModel)
        self.optionTable.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.optionTable.setSortingEnabled(True)

        self.gridLayout.addWidget(self.optionTable, 0, 1, 1, 1)

        self.tabWidget.addTab(self.ratings, "")
        self.ranking = QWidget()
        self.ranking.setObjectName(u"ranking")
        self.gridLayout_3 = QGridLayout(self.ranking)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.rankingModel = RankingModel(issues=self.issues)
        self.rankingTable = QTableView(self.ranking)
        self.rankingTable.setObjectName(u"rankingTable")
        self.rankingTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.rankingTable.setModel(self.rankingModel)
        self.rankingTable.setSelectionMode(QAbstractItemView.NoSelection)
        self.rankingTable.setSortingEnabled(True)


        self.gridLayout_3.addWidget(self.rankingTable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.ranking, "")
        self.selectOffer = QWidget()
        self.selectOffer.setObjectName(u"selectOffer")
        self.gridLayout_4 = QGridLayout(self.selectOffer)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.offerScore = QLabel(self.selectOffer)
        self.offerScore.setObjectName(u"offerScore")
        self.offerScore.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.offerScore, 2, 0, 1, 1)

        self.chooseModel = ChooseModel(issues=self.issues)
        self.chooseTable = ChooseTableView(self.selectOffer, issues=self.issues)
        self.chooseTable.setObjectName(u"chooseTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseTable.sizePolicy().hasHeightForWidth())
        self.chooseTable.setSizePolicy(sizePolicy)
        self.chooseTable.setModel(self.chooseModel)
        self.chooseTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.chooseTable.updateScore.connect(self.update_score)
        self.chooseTable.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_4.addWidget(self.chooseTable, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.tabWidget.addTab(self.selectOffer, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuPlik = QMenu(self.menubar)
        self.menuPlik.setObjectName(u"menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPlik.menuAction())
        self.menuPlik.addAction(self.actionNew)
        self.menuPlik.addAction(self.actionSave)
        self.menuPlik.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def update_score(self, score):
        self.offerScore.setText("Ocena: " + str(score))

    def add_issue(self):
        name = self.issueName.text()
        if name == "":
            return
        self.issues.append(Issue(name))
        self.issueModel.layoutChanged.emit()
        self.issueName.setText("")
        self.issueName.repaint()
        self.chooseModel.layoutChanged.emit()

    def delete_issue(self):
        if len(self.issueTable.selectedIndexes()) == 0:
            return
        index = self.issueTable.selectedIndexes()[0].row()
        del self.issues[index]
        self.issueModel.layoutChanged.emit()
        self.issueTable.clearSelection()
        self.optionModel.issue_selected = -1
        self.optionModel.layoutChanged.emit()
        self.optionTable.clearSelection()
        self.chooseModel.layoutChanged.emit()
        self.rankingModel.layoutChanged.emit()

    def add_option(self):
        name = self.optionName.text()
        issue_selected = self.optionModel.issue_selected
        if name == "" or issue_selected == -1:
            return
        self.issues[issue_selected].add_option(Option(name))
        self.optionModel.layoutChanged.emit()
        self.optionName.setText("")
        self.optionName.repaint()
        self.chooseModel.layoutChanged.emit()

    def delete_option(self):
        if len(self.optionTable.selectedIndexes()) == 0:
            return
        indexes = list(set((map(lambda x: x.row(), self.optionTable.selectedIndexes()))))
        for removed, index in enumerate(indexes):
            del self.issues[self.optionModel.issue_selected].options[index - removed]
        self.optionModel.layoutChanged.emit()
        self.optionTable.clearSelection()
        self.chooseModel.layoutChanged.emit()

    @Slot()
    def on_issueName_returnPressed(self):
        self.add_issue()

    @Slot()
    def on_addIssue_clicked(self):
        self.add_issue()

    @Slot()
    def on_deleteIssue_clicked(self):
        self.delete_issue()

    @Slot()
    def on_optionName_returnPressed(self):
        self.add_option()

    @Slot()
    def on_addOption_clicked(self):
        self.add_option()

    @Slot()
    def on_deleteOption_clicked(self):
        self.delete_option()

    @Slot()
    def on_issueTable_clicked(self):
        if len(self.issueTable.selectedIndexes()) == 0:
            return
        index = self.issueTable.selectedIndexes()[0].row()
        self.optionModel.issue_selected = index
        self.optionModel.layoutChanged.emit()

    @Slot(int)
    def on_tabWidget_currentChanged(self, index: int):
        self.statusbar.showMessage("")
        if index == 1:
            self.rankingModel.update_offers()
            self.rankingModel.layoutChanged.emit()
        elif index == 2:
            self.chooseTable.updateWidgets = True
            self.chooseTable.update_offer()
            self.update_score(self.chooseTable.offer.rating)

    @Slot()
    def on_actionNew_triggered(self):
        newTemplateDialog = NewTemplateDialog(self)
        if newTemplateDialog.exec_():
            self.optionModel.issue_selected = -1
            self.issues.clear()
            self.issueModel.layoutChanged.emit()
            self.optionModel.layoutChanged.emit()
            self.rankingModel.layoutChanged.emit()
            self.chooseModel.layoutChanged.emit()
            self.statusbar.showMessage("Stworzono nowy szablon")

    @Slot()
    def on_actionSave_triggered(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("XML(*.xml)")
        file_dialog.setDefaultSuffix("xml")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            if file_path.endswith("xml"):
                file = open(file_path, "w+")
                file.write(Parser.parse_issues(self.issues))
                file.close()
                self.statusbar.showMessage("Dane zostały zapisane do pliku")

    @Slot()
    def on_actionOpen_triggered(self):
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("XML(*.xml)")
        file_dialog.setDefaultSuffix("xml")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            if file_path.endswith("xml"):
                self.optionModel.issue_selected = -1
                self.issues.clear()
                self.issues.extend(Parser.parse_file(file_path))
                self.issueModel.layoutChanged.emit()
                self.optionModel.layoutChanged.emit()
                self.rankingModel.layoutChanged.emit()
                self.chooseModel.layoutChanged.emit()
                self.statusbar.showMessage("Dane zostały wczytane z pliku")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Szablon negocjacyjny", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"Nowy szablon...", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Zapisz jako...", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Otwórz plik...", None))
        self.deleteIssue.setText(QCoreApplication.translate("MainWindow", u"Usuń kwestię", None))
        self.deleteOption.setText(QCoreApplication.translate("MainWindow", u"Usuń opcje", None))
        self.addIssue.setText(QCoreApplication.translate("MainWindow", u"Dodaj kwestię", None))
        self.addOption.setText(QCoreApplication.translate("MainWindow", u"Dodaj opcję", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ratings),
                                  QCoreApplication.translate("MainWindow", u"Ustalanie kwestii i ocen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ranking),
                                  QCoreApplication.translate("MainWindow", u"Ranking ofert", None))
        self.offerScore.setText(QCoreApplication.translate("MainWindow", u"Ocena: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectOffer),
                                  QCoreApplication.translate("MainWindow", u"Ocenianie wybranej oferty", None))
        self.menuPlik.setTitle(QCoreApplication.translate("MainWindow", u"Plik", None))
    # retranslateUi