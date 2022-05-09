import qtawesome as qta
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QWidget

from ui.widgets import Ui_LocalRepositoryTemplate
from utils import get_repo_info


class LocalRepositoryTemplate(QWidget):
    def __init__(self, repo_path, user):
        super(LocalRepositoryTemplate, self).__init__()
        self.ui = Ui_LocalRepositoryTemplate()
        self.ui.setupUi(self)

        self.repo_path = repo_path
        self.user = user

        self.config_ui()

        self.fill()

    def fill(self):
        repo_user, repo_name, full_repo_name = get_repo_info(self.repo_path)
        self.ui.repoNameLabel.setText(repo_name)
        self.ui.pathLineEdit.setText(self.repo_path)

        try:
            repo = self.user.github.get_repo(full_repo_name)
            self.ui.githubButton.setIcon(QIcon(qta.icon('msc.github', color='green')))
            self.ui.githubButton.setToolTip('Open in Browser')
            self.ui.githubButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(repo.html_url)))
        except Exception:
            self.ui.githubButton.setIcon(QIcon(qta.icon('msc.github', color='red')))
            self.ui.githubButton.setToolTip('Repository not found in GitHub')

    def config_ui(self):
        self.ui.pathLineEdit.setDisabled(True)
