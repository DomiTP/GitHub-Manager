from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget
from github.Repository import Repository

from ui.widgets import Ui_RepositoryTemplate
from utils import get_icon, time


class RepositoryTemplate(QWidget):
    def __init__(self, repository: Repository):
        super(RepositoryTemplate, self).__init__()
        self.ui = Ui_RepositoryTemplate()
        self.ui.setupUi(self)

        self.repo: Repository = repository

        self.config_ui()

        self.fill()

    def fill(self):
        """
        Fill the template with the data from the repository
        """
        self.ui.repoNameLabel.setText(self.repo.name)
        self.ui.visibilityLabel.setText('Private' if self.repo.private else 'Public')
        self.ui.repoDescLabel.setText(self.repo.description)
        try:
            self.ui.licenseNameLabel.setText(self.repo.get_license().license.name)
        except Exception:
            self.ui.licenseNameLabel.setText("None")
        self.ui.updatedLabel.setText(time("Updated", self.repo.updated_at))
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
