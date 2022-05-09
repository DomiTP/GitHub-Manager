import qtawesome as qta
import requests
from PySide6.QtCore import QUrl, QSize
from PySide6.QtGui import QPixmap, QDesktopServices, QIcon, QImage
from PySide6.QtWidgets import QWidget, QListWidgetItem
from github.AuthenticatedUser import AuthenticatedUser
from github.Commit import Commit

from modules import User
from ui.widgets import Ui_repository
from utils import time_formatter
from widgets import CloneTemplate, FileTemplate, RepositoryListWidgetItem, EditRepository, IssueTemplate


class Repository(QWidget):
    def __init__(self, repo, user):
        super(Repository, self).__init__()
        self.ui = Ui_repository()
        self.ui.setupUi(self)

        self.repository = repo

        self.user: User = user
        self.authenticated_user: AuthenticatedUser = user.get_data()

        self.clone = CloneTemplate(self.repository, self.user)
        self.edit_repo = QWidget()

        self.config_ui()
        self.load_data()
        self.load_code_data()
        self.load_issues()

    def load_data(self):
        """
        Load repo data to ui widgets
        """
        self.ui.repoLabel.setText(self.repository.full_name)
        self.watch()
        self.fork()
        self.star()

        self.ui.watchButton.clicked.connect(self.watch_button)
        self.ui.forkButton.clicked.connect(self.fork_button)
        self.ui.starButton.clicked.connect(self.star_button)

        try:
            self.ui.licenseWidget.setText(self.repository.get_license().license.name)
        except Exception:
            self.ui.licenseWidget.setText("No license")

    def config_ui(self):
        """
        Config ui widgets
        """
        self.setWindowTitle(self.repository.name)
        self.ui.tabWidget.setTabIcon(0, QIcon(qta.icon("fa5s.code").pixmap(10, 10)))
        self.ui.tabWidget.setTabIcon(1, QIcon(qta.icon("fa5s.dot-circle").pixmap(10, 10)))
        self.ui.commitsWidget.set_icon("fa5s.history")
        self.ui.licenseWidget.set_icon("fa5s.balance-scale")
        self.ui.configButton.setIcon(QIcon(qta.icon("ei.cog").pixmap(20, 20)))

        self.ui.descLabel.setText(self.repository.description)
        self.ui.codeButton.clicked.connect(lambda: self.clone.show())
        self.ui.branchComboBox.currentTextChanged.connect(self.branch_changed)
        self.ui.filesListWidget.itemClicked.connect(self.on_click)
        self.ui.configButton.clicked.connect(self.edit_repo_window)

    def load_code_data(self):
        """
        Load repo data to ui widgets
        """
        self.ui.branchComboBox.clear()
        for branch in self.repository.get_branches():
            self.ui.branchComboBox.addItem(QPixmap(qta.icon("fa5s.code-branch").pixmap(10, 10)), branch.name)

        self.ui.branchComboBox.setCurrentText(self.repository.default_branch)

        image = QImage()
        image.loadFromData(requests.get(self.repository.owner.avatar_url).content)
        self.ui.profileImageLabel.setPixmap(QPixmap(image).scaled(QSize(20, 20)))
        self.ui.usernameLabel.setText(self.repository.owner.login)
        commits = self.repository.get_commits()
        last_commit: Commit = commits[0]
        self.ui.commitLabel.setText(last_commit.commit.message)
        self.ui.numsLabel.setText(last_commit.commit.sha[:7])
        self.ui.timeLabel.setText(time_formatter("", time2=last_commit.commit.author.date))
        self.ui.commitsWidget.setText(
            str(commits.totalCount) + " commit" if commits.totalCount == 1 else str(commits.totalCount) + " commits")

    def load_issues(self):
        issues = self.repository.get_issues()
        for issue in issues:
            item = QListWidgetItem()
            widget = IssueTemplate(issue)
            item.setSizeHint(widget.sizeHint())
            self.ui.issuesListWidget.addItem(item)
            self.ui.issuesListWidget.setItemWidget(item, widget)

    def branch_changed(self, branch_name):
        """
        When branch changed, update files list
        :param branch_name: branch name
        """
        content = self.repository.get_contents("/", ref=branch_name)
        self.load_content(content, depth=0)

    def load_content(self, content, full_path="/", depth=0, dir_name=None):
        """
        Load repo files to the QListWidget
        :param dir_name:  dir name
        :param content:  content
        :param full_path:  last path
        :param depth:  depth
        """
        self.ui.filesListWidget.clear()
        if depth != 0:
            if dir_name == "..":
                cont = self.repository.get_contents("/".join(full_path.split("/")[:-1]),
                                                    ref=self.ui.branchComboBox.currentText())
                item = RepositoryListWidgetItem("..", True, "",
                                                full_path if depth < 1 else "/".join(full_path.split("/")[:-1]),
                                                depth=depth - 1, contents=cont)
            else:
                cont = self.repository.get_contents(full_path.split("/").pop(),
                                                    ref=self.ui.branchComboBox.currentText())
                item = RepositoryListWidgetItem("..", True, "", full_path if depth < 1 else full_path + dir_name + "/",
                                                depth=depth - 1, contents=cont)
            item.setText("..")
            item.setIcon(QIcon(qta.icon("fa5s.arrow-up").pixmap(10, 10)))
            self.ui.filesListWidget.addItem(item)

        while content:
            file_content = content.pop(0)
            if file_content.type == "dir":
                item = RepositoryListWidgetItem(file_content.name, True, file_content.html_url,
                                                full_path if depth < 1 else full_path + dir_name + "/", depth + 1,
                                                contents=self.repository.get_contents(
                                                    file_content.path, ref=self.ui.branchComboBox.currentText()))
            else:
                item = RepositoryListWidgetItem(file_content.name, False, file_content.html_url, full_path)
            widget = FileTemplate(file_content)
            item.setSizeHint(widget.sizeHint())
            self.ui.filesListWidget.addItem(item)
            self.ui.filesListWidget.setItemWidget(item, widget)

    def on_click(self, item):
        """
        When item clicked, update content
        :param item: RepositoryListWidgetItem
        """
        if item.isDirectory:
            self.load_content(item.contents, item.path, item.depth, item.name)
        else:
            QDesktopServices.openUrl(QUrl(item.url))

    def edit_repo_window(self):
        self.edit_repo = EditRepository(self.repository)
        self.edit_repo.show()

    def watch(self):
        """
        People subscribed to this repo
        """
        self.ui.watchButton.setText("Unwatch " + str(self.repository.subscribers_count)
                                    if self.repository in self.authenticated_user.get_watched()
                                    else "Watch " + str(self.repository.subscribers_count))
        self.ui.watchButton.setIcon(qta.icon("ei.eye-close") if self.repository in self.authenticated_user.get_watched()
                                    else qta.icon("ei.eye-open"))

        self.ui.watchingWidget.setText(str(self.repository.subscribers_count) + " watching")
        self.ui.watchingWidget.set_icon("fa5s.eye")

    def watch_button(self):
        """
        Watch/Unwatch repository
        """
        if self.repository in self.authenticated_user.get_watched():
            self.authenticated_user.remove_from_watched(self.repository)
        else:
            self.authenticated_user.add_to_watched(self.repository)
        self.watch()

    def fork(self):
        """
        Fork repository and forks count
        """
        if self.repository in self.authenticated_user.get_repos():
            self.ui.forkButton.setDisabled(True)
            self.ui.forkButton.setToolTip("You own this repository")

        self.ui.forkButton.setText("Fork " + str(self.repository.forks_count))
        self.ui.forkButton.setIcon(QPixmap(qta.icon("fa5s.code-branch").pixmap(15, 15)))

        self.ui.forksWidget.setText(
            str(self.repository.forks_count) + " fork" if self.repository.forks_count == 1 else
            str(self.repository.forks_count) + " forks")
        self.ui.forksWidget.set_icon("fa5s.code-branch")

    def fork_button(self):
        """
        Fork repository
        """
        self.authenticated_user.create_fork(self.repository)
        self.fork()

    def star(self):
        """
        Star repository and stars count
        """
        self.ui.starButton.setText("Starred " + str(self.repository.stargazers_count)
                                   if self.repository in self.authenticated_user.get_starred()
                                   else "Star " + str(self.repository.stargazers_count))
        self.ui.starButton.setIcon(QPixmap(
            qta.icon("fa5s.star", color='orange').pixmap(15, 15)
            if self.repository in self.authenticated_user.get_starred()
            else qta.icon("fa5s.star").pixmap(15, 15)))

        self.ui.starWidget.setText(
            str(self.repository.stargazers_count) + " star" if self.repository.stargazers_count == 1 else str(
                self.repository.stargazers_count) + " stars")
        self.ui.starWidget.set_icon("fa5s.star")

    def star_button(self):
        """
        Star repository
        """
        if self.repository in self.authenticated_user.get_starred():
            self.authenticated_user.remove_from_starred(self.repository)
        else:
            self.authenticated_user.add_to_starred(self.repository)
        self.star()
