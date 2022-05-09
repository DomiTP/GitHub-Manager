from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget
from github.AuthenticatedUser import AuthenticatedUser
from github.Repository import Repository

from ui.widgets import Ui_RepositoryTemplate
from utils import get_icon, time_formatter


class RepositoryTemplate(QWidget):
    def __init__(self, repo: Repository, user: AuthenticatedUser):
        super(RepositoryTemplate, self).__init__()
        self.ui = Ui_RepositoryTemplate()
        self.ui.setupUi(self)

        self.repo: Repository = repo
        self.user: AuthenticatedUser = user

        self.config_ui()

        self.fill()

    def fill(self):
        """
        Fill the template with the data from the repo
        """
        self.ui.repoNameLabel.setText(self.repo.name)
        self.ui.visibilityLabel.setText('Private' if self.repo.private else 'Public')
        self.ui.repoDescLabel.setText(self.repo.description)
        try:
            self.ui.licenseNameLabel.setText(self.repo.get_license().license.name)
        except Exception:
            self.ui.licenseNameLabel.setText("None")
        self.ui.updatedLabel.setText(time_formatter("Updated", time2=self.repo.updated_at))
        self.ui.updatedLabel.setToolTip(self.repo.updated_at.strftime("%d-%m-%Y %H:%M:%S") + " UTC")
        self.ui.starButton.setText("Star" if self.repo.stargazers_count == 0 else "Starred")

    def config_ui(self):
        """
        Configure the UI
        """
        self.ui.licenseIconLabel.setPixmap(QPixmap(get_icon("dark_license.png")).scaled(QSize(15, 15)))
        self.ui.starButton.setIcon(
            QIcon(get_icon("dark_star.png" if self.repo.stargazers_count == 0 else "yellow_star.png")))
        self.ui.visibilityLabel.setStyleSheet("border: 1px solid black; border-radius: 10px; padding: 1px;")
        self.ui.starButton.clicked.connect(self.star_button)

    def star(self):
        """
        Star the repo
        """
        self.ui.starButton.setText("Starred" if self.repo in self.user.get_starred() else "Star")
        self.ui.starButton.setIcon(
            QIcon(get_icon("yellow_star.png" if self.repo in self.user.get_starred() else "dark_star.png")))

    def star_button(self):
        """
        Star the repo
        """
        if self.repo in self.user.get_starred():
            self.user.remove_from_starred(self.repo)
        else:
            self.user.add_to_starred(self.repo)
        self.star()
