from datetime import datetime

import requests
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from github.Repository import Repository

from ui.widgets import Ui_localRepository
from utils import get_repo_info, time_formatter
from widgets import MplCanvas


class LocalRepository(QWidget):
    def __init__(self, repo_path, user):
        super(LocalRepository, self).__init__()
        self.ui = Ui_localRepository()
        self.ui.setupUi(self)

        self.repo_path = repo_path
        self.user = user

        self.owner, self.repo_name, self.full_repo_name = get_repo_info(self.repo_path)

        self.load_data()

    def load_data(self):
        try:
            repo: Repository = self.user.github.get_repo(self.full_repo_name)
            self.ui.repoLabel.setText(repo.name.upper())
            self.ui.fullNameLineEdit.setText(repo.full_name)
            self.ui.ownerLineEdit.setText(repo.owner.login)
            self.ui.descriptionLineEdit.setText(repo.description)
            self.ui.createdAtLineEdit.setText(repo.created_at.strftime("%d/%m/%Y"))
            self.ui.updatedLineEdit.setText(time_formatter("", time2=repo.updated_at))
            self.ui.languageLineEdit.setText(repo.language)
            self.ui.forksLineEdit.setText(str(repo.forks_count))
            self.ui.starsLineEdit.setText(str(repo.stargazers_count))
            self.ui.subscribersLineEdit.setText(str(repo.subscribers_count))
            # self.ui.licenseLineEdit.setText(repo.get_license().license.name)
            self.plot()
        except Exception as e:
            print(e)
            self.ui.repoLabel.setText(self.repo_name.upper())
            self.ui.fullNameLineEdit.setText(self.full_repo_name)
            self.ui.ownerLineEdit.setText(self.owner)
            self.ui.descriptionLabel.hide()
            self.ui.descriptionLineEdit.hide()
            self.ui.createdAtLabel.hide()
            self.ui.createdAtLineEdit.hide()
            self.ui.updatedLabel.hide()
            self.ui.updatedLineEdit.hide()
            self.ui.languageLabel.hide()
            self.ui.languageLineEdit.hide()
            self.ui.forksLabel.hide()
            self.ui.forksLineEdit.hide()
            self.ui.starsLabel.hide()
            self.ui.starsLineEdit.hide()
            self.ui.subscribersLabel.hide()
            self.ui.subscribersLineEdit.hide()
            self.ui.licenseLabel.hide()
            self.ui.licenseLineEdit.hide()
            self.ui.label.hide()
            self.ui.commitsImageLabel.hide()

    def plot(self):
        """
        Obtiene los datos de la api y los carga en la gráfica
        """
        response = requests.get(f'https://api.github.com/repos/{self.full_repo_name}/stats/commit_activity')
        weeks = []
        total = []
        if response.status_code == 200:
            for x in response.json():
                weeks.append(datetime.fromtimestamp(x["week"]).strftime('%m/%d'))
                total.append(x["total"])
            weeks = weeks[36:]
            total = total[36:]
            canvas = MplCanvas(width=10, height=6, dpi=50)
            canvas.ax.bar(weeks, total)
            self.ui.commitsImageLabel.setPixmap(
                QPixmap(canvas.figure.canvas.to_image()))
