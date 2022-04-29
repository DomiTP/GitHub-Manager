import sys

import requests
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QImage, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout

from modules import Login, About, User, Repositories
from ui import Ui_MainWindow
from utils import LOGO, time

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = 'xyz.domitp.githubmanager.1.0'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class GitHubManager(QMainWindow):
    def __init__(self):
        super(GitHubManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.login = Login(self)
        self.login.show()
        self.login_method = None

        self.about = About()

        self.user = None

        self.repositories_widget = None

        self.config()

    def start(self, token=None):
        """
        Start
        :param token: Token de usuario
        """
        self.login_method = 1 if token else 0

        if self.login_method == 1:
            self.token_login(token)
        else:
            self.no_token()

        self.load_user_info()
        self.load_repositories()

        self.show()

    def token_login(self, token):
        self.user = User(token)

    def no_token(self):
        pass  # TODO: Implementar login por token no existente

    def config(self):
        self.setWindowIcon(QIcon(LOGO))

        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(lambda x: self.about.show())

    def load_repositories(self):
        self.repositories_widget = Repositories(self.user)
        self.ui.repositoriesTab.setLayout(QVBoxLayout(self.ui.repositoriesTab).addWidget(self.repositories_widget))

    def load_user_info(self):
        user_data = self.user.get_named_user_data()
        if user_data.name:
            self.ui.nameLabel.setText(user_data.name)
        else:
            self.ui.nameLabel.hide()

        if user_data.login:
            self.ui.userNameLabel.setText(user_data.login)
        else:
            self.ui.userNameLabel.hide()

        if user_data.bio:
            self.ui.bioLabel.setText(user_data.bio)
        else:
            self.ui.bioLabel.hide()

        if user_data.location:
            self.ui.locationWidget.setText(user_data.location)
            self.ui.locationWidget.set_icon("fa5s.map-marker-alt")
        else:
            self.ui.locationWidget.hide()

        if user_data.company:
            self.ui.companyWidget.setText(user_data.company)
            self.ui.companyWidget.set_icon("fa5s.building")
        else:
            self.ui.companyWidget.hide()

        if user_data.twitter_username:
            self.ui.twitterWidget.setText(user_data.twitter_username)
            self.ui.twitterWidget.set_icon("fa5b.twitter")
        else:
            self.ui.twitterWidget.hide()

        if user_data.created_at:
            self.ui.joinedWidget.setText(time("Joined", user_data.created_at))
            self.ui.joinedWidget.set_icon("fa5s.clock")
        else:
            self.ui.joinedWidget.hide()

        image = QImage()
        image.loadFromData(requests.get(user_data.avatar_url).content)
        self.ui.profileImageLabel.setPixmap(QPixmap(image).scaled(QSize(120, 120), Qt.KeepAspectRatio))

    def closeEvent(self, event):
        """
        Cierra todas las ventanas
        :param event:
        """
        quit()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(LOGO))
    widget = GitHubManager()
    sys.exit(app.exec())
