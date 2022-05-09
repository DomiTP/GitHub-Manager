import sys
from datetime import datetime

import qtawesome as qta
import requests
from PySide6.QtCore import QSize, QTimer
from PySide6.QtGui import QIcon, QPixmap, QImage, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QMessageBox

from modules import Login, About, Repositories, LocalRepositories
from ui import Ui_MainWindow
from utils import LOGO, time_formatter

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

        self.about = About()

        self.user = None

        self.timer = QTimer(self)

        self.config()

    def start(self, user):
        """
        Loads the user's information and repositories.
        :param user:
        """
        self.user = user

        self.load_user_info()
        self.load_repositories()
        self.load_local_repositories()

        self.show()

    def config(self):
        """
        Configures the main window.
        """
        self.setWindowIcon(QIcon(LOGO))

        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(lambda x: self.about.show())
        self.ui.actionReload.triggered.connect(self.reload)

        self.ui.infoButton.setIcon(QIcon(qta.icon("fa5s.info-circle").pixmap(QSize(20, 20))))

    def load_repositories(self):
        """
        Loads the user's repositories.
        """
        repositories_widget = Repositories(self.user)
        self.ui.repositoriesTab.setLayout(QVBoxLayout(self.ui.repositoriesTab).addWidget(repositories_widget))

    def load_local_repositories(self):
        """
        Loads the user's local repositories.
        """
        local_repositories_widget = LocalRepositories(self.user)
        self.ui.localTab.setLayout(QVBoxLayout(self.ui.localTab).addWidget(local_repositories_widget))

    def load_user_info(self):
        """
        Loads the user's information.
        """
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
            self.ui.joinedWidget.setText(time_formatter("Joined", time2=user_data.created_at))
            self.ui.joinedWidget.set_icon("fa5s.clock")
        else:
            self.ui.joinedWidget.hide()

        image = QImage()
        image.loadFromData(requests.get(user_data.avatar_url).content)
        self.ui.profileImageLabel.setPixmap(QPixmap(image).scaled(QSize(120, 120), Qt.KeepAspectRatio))

        self.timer.timeout.connect(self.update_requests)
        self.timer.start(1000)
        self.ui.infoButton.clicked.connect(self.requests_info)

    def reload(self):
        self.load_user_info()
        self.load_repositories()

    def update_requests(self):
        user_requests = self.user.github.rate_limiting[0]
        max_requests = self.user.github.rate_limiting[1]
        self.ui.infoButton.setToolTip("Requests: {}/{}".format(user_requests, max_requests))

    def requests_info(self):
        message = QMessageBox()
        message.setWindowTitle("Requests")
        message.setText("Requests: {}/{} \n{}".format(
            self.user.github.rate_limiting[0],
            self.user.github.rate_limiting[1],
            time_formatter("Reset:", time1=datetime.utcfromtimestamp(self.user.github.rate_limiting_resettime),
                           suffix="")
        ))
        message.setDefaultButton(QMessageBox.Ok)
        message.exec()

    def closeEvent(self, event):
        """
        Closes the application.
        :param event: Event
        """
        quit()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon(LOGO))
    widget = GitHubManager()
    sys.exit(app.exec())
