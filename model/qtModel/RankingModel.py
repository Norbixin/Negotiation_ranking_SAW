from PySide2 import QtCore
from typing import List
from model import Issue, Offer


class RankingModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, issues: List[Issue]=[], **kwargs):
        super(RankingModel, self).__init__(*args, **kwargs)
        self.__issues: List[Issue] = issues
        self.__offers: List[Offer] = []

    def rowCount(self, parent: QtCore.QModelIndex=...):
        return len(self.offers)

    def columnCount(self, parent: QtCore.QModelIndex=...):
        return len(self.issues) + 1

    def data(self, index: QtCore.QModelIndex, role: int=...):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return self.offers[index.row()].rating
            return self.offers[index.row()].options[index.column() - 1].name

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section == 0:
                    return "Ocena"
                return self.issues[section - 1].name
            elif orientation == QtCore.Qt.Vertical:
                return section + 1

    def sort(self, column: int, order: QtCore.Qt.SortOrder=...):
        if column == 0:
            if order == QtCore.Qt.AscendingOrder:
                self.offers.sort(key=lambda offer: offer.rating)
            elif order == QtCore.Qt.DescendingOrder:
                self.offers.sort(key=lambda offer: offer.rating, reverse=True)
        else:
            if order == QtCore.Qt.AscendingOrder:
                self.offers.sort(key=lambda offer: offer.options[column - 1].name)
            elif order == QtCore.Qt.DescendingOrder:
                self.offers.sort(key=lambda offer: offer.options[column - 1].name, reverse=True)
        self.layoutChanged.emit()

    @property
    def issues(self) -> List[Issue]:
        return self.__issues

    @property
    def offers(self) -> List[Offer]:
        return self.__offers

    @offers.setter
    def offers(self, value):
        self.__offers = value

    def update_offers(self):
        self.offers.clear()
        issues_valid: bool = len(self.issues) > 0
        for issue in self.issues:
            if len(issue.options) == 0:
                issues_valid = False
        if not issues_valid:
            return
        if len(self.issues) > 0:
            self.__offers = self.create_offers(0, 0, Offer())
        for offer in self.offers:
            offer.calculate_rating()
        self.offers.sort(key=lambda _offer: _offer.rating, reverse=True)

    def create_offers(self, issue_index: int, option_index: int, offer: Offer):
        current_offer = offer.__copy__()
        current_offer.add_option(self.issues[issue_index].options[option_index])
        if issue_index == len(self.issues) - 1:
            if option_index == len(self.issues[issue_index].options) - 1:
                return [current_offer]
            offers = self.create_offers(issue_index, option_index + 1, offer)
            offers.append(current_offer)
            return offers
        offers = self.create_offers(issue_index + 1, 0, current_offer)
        if option_index < len(self.issues[issue_index].options) - 1:
            offers.extend(self.create_offers(issue_index, option_index + 1, offer))
        return offers
