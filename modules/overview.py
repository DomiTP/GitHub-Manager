from datetime import date

import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout
from github.PaginatedList import PaginatedList

from ui.widgets import Ui_Overview
from widgets import PopularRepository, MplCanvas


class Overview(QWidget):
    def __init__(self, user):
        super(Overview, self).__init__()
        self.ui = Ui_Overview()
        self.ui.setupUi(self)

        self.user = user

        self.load_popular_repos()
        self.load_contributions()

    def load_popular_repos(self):
        popular_repos: PaginatedList = self.user.get_data().get_repos(visibility="public", sort="updated",
                                                                      direction="desc")
        positions = [(i, j) for i in range(2) for j in range(2)]
        for positions, popular_repo in zip(positions, popular_repos):
            self.ui.gridLayout.addWidget(PopularRepository(popular_repo, self.user), *positions)

    def load_contributions(self):
        response = requests.get(f'https://skyline.github.com/{self.user.user.login}/{date.today().year}.json',
                                auth=(self.user.get_data().login, self.user.token))
        weeks = []
        total = []
        if response.status_code == 200:
            for x in response.json()['contributions']:
                weeks.append(x['week'])  # TODO: make this a date
                acum = 0
                for y in x['days']:
                    acum += int(y['count'])
                total.append(acum)
            canvas = MplCanvas(width=10, height=6, dpi=50, xlabel='weeks', ylabel='total contributions',
                               title='Contributions')
            canvas.ax.bar(weeks, total)
            self.ui.contributionsWidget.setLayout(QVBoxLayout(self.ui.contributionsWidget).addWidget(canvas))
