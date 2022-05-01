import qtawesome as qta
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QPixmap, QDesktopServices, QIcon
from PySide6.QtWidgets import QWidget, QListWidgetItem
from github.Commit import Commit

from ui.widgets import Ui_repository
from utils import get_icon, time
from widgets import CloneTemplate, FileTemplate


class Repository(QWidget):
    def __init__(self, repo):
        super(Repository, self).__init__()
        self.ui = Ui_repository()
        self.ui.setupUi(self)

        self.repository = repo

        self.code = CloneTemplate(self.repository)

        self.config_ui()
        self.load_data()
        self.load_code_data()
        self.load_files()

    def load_data(self):
        self.ui.repoLabel.setText(self.repository.full_name)
        self.ui.watchButton.setText(
            "Watch " if self.repository in self.repository.owner.get_watched() else "Unwatch " + str(
                self.repository.subscribers_count))
        self.ui.watchButton.setIcon(QPixmap(qta.icon("fa5s.eye").pixmap(10, 10)))
        self.ui.forkButton.setText("Fork " + str(self.repository.forks_count))
        self.ui.forkButton.setIcon(QPixmap(qta.icon("fa5s.code-branch").pixmap(10, 10)))
        self.ui.forkButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(self.repository.forks_url)))
        self.ui.starButton.setText("Star " + str(self.repository.stargazers_count))
        self.ui.starButton.setIcon(
            QIcon(get_icon("dark_star.png" if self.repository.stargazers_count == 0 else "yellow_star.png")))

    def config_ui(self):
        self.setWindowTitle(self.repository.name)
        self.ui.tabWidget.setTabIcon(0, QIcon(qta.icon("fa5s.code").pixmap(10, 10)))
        self.ui.tabWidget.setTabIcon(1, QIcon(qta.icon("fa5s.dot-circle").pixmap(10, 10)))

    def load_code_data(self):
        for branch in self.repository.get_branches():
            self.ui.branchComboBox.addItem(QPixmap(qta.icon("fa5s.code-branch").pixmap(10, 10)), branch.name)

        self.ui.codeButton.clicked.connect(lambda: self.code.show())
        self.ui.profileImageLabel.setPixmap(QPixmap(self.repository.owner.avatar_url).scaled(QSize(50, 50)))
        self.ui.usernameLabel.setText(self.repository.owner.login)
        commits = self.repository.get_commits()
        last_commit: Commit = commits[0]
        self.ui.commitLabel.setText(last_commit.commit.message)
        self.ui.numsLabel.setText(last_commit.commit.sha[:7])
        self.ui.timeLabel.setText(time("", last_commit.commit.author.date))
        self.ui.commitsWidget.setText(
            str(commits.totalCount) + " commit" if commits.totalCount == 1 else str(commits.totalCount) + " commits")
        self.ui.licenseWidget.setText(self.repository.get_license().license.name)
        self.ui.commitsWidget.set_icon("fa5s.history")
        self.ui.licenseWidget.set_icon("fa5s.balance-scale")
        self.ui.starWidget.setText(
            str(self.repository.stargazers_count) + " star" if self.repository.stargazers_count == 1 else str(
                self.repository.stargazers_count) + " stars")
        self.ui.starWidget.set_icon("fa5s.star")
        self.ui.watchingWidget.setText(str(self.repository.subscribers_count) + " watching")
        self.ui.watchingWidget.set_icon("fa5s.eye")
        self.ui.forksWidget.setText(
            str(self.repository.forks_count) + " fork" if self.repository.forks_count == 1 else
            str(self.repository.forks_count) + " forks")
        self.ui.forksWidget.set_icon("fa5s.code-branch")
        self.ui.descLabel.setText(self.repository.description)

    def load_files(self):
        content = self.repository.get_contents("")
        while content:
            file_content = content.pop(0)
            item = QListWidgetItem()
            widget = FileTemplate(file_content, self.repository)
            item.setSizeHint(widget.sizeHint())
            self.ui.filesListWidget.addItem(item)
            self.ui.filesListWidget.setItemWidget(item, widget)
