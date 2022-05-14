import os
import shutil
from datetime import datetime

import requests
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
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
        self.url = None

        self.owner, self.repo_name, self.full_repo_name = get_repo_info(self.repo_path)

        self.config()
        self.load_data()

    def load_data(self):
        try:
            self.setWindowTitle(f'{self.repo_name} - {self.owner}')
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
            self.url = repo.html_url
            self.plot()
        except Exception:
            self.setWindowTitle(f'{self.repo_name}')
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
            self.ui.label.hide()
            self.ui.openBrowserButton.hide()
            self.ui.commitsImageWidget.hide()

    def plot(self):
        """
        Obtiene los datos de la api y los carga en la gráfica
        """
        response = requests.get(f'https://api.github.com/repos/{self.full_repo_name}/stats/commit_activity',
                                auth=(self.user.get_data().login, self.user.token))
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
            self.ui.commitsImageWidget.setLayout(QVBoxLayout(self.ui.commitsImageWidget).addWidget(canvas))

    def config(self):
        self.ui.deleteButton.clicked.connect(self.delete_repo)
        self.ui.openFolderButton.clicked.connect(self.open_folder)
        self.ui.openBrowserButton.clicked.connect(self.open_browser)

    def delete_repo(self):
        """
        Deletes the repo folder and all its contents
        """
        if self.warn():
            try:
                shutil.rmtree(self.repo_path, ignore_errors=True)
                print(f'{self.repo_path} deleted')
                self.close()
            except Exception as e:
                print(e)

    def warn(self):
        """
        Shows a warning message
        """
        res = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("You are about to delete the repository from the disk, this action cannot be undone.")
        msg.setInformativeText("Are you sure you want to continue?")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = msg.exec()
        if response == QMessageBox.Yes:
            double_check = QMessageBox()
            double_check.setIcon(QMessageBox.Warning)
            double_check.setText("Are you really sure you want to continue?")
            double_check.setInformativeText("This action cannot be undone.")
            double_check.setWindowTitle("Warning")
            double_check.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            response2 = double_check.exec()
            if response2 == QMessageBox.Yes:
                res = True
        return res

    def open_folder(self):
        """
        Opens the folder of the repo
        """
        os.startfile(self.repo_path)

    def open_browser(self):
        """
        Open the GitHub page of the repo
        """
        QDesktopServices.openUrl(QUrl(self.url))

