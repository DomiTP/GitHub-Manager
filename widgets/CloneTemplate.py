import qtawesome as qta
from PySide6.QtWidgets import QWidget, QApplication
from github.Repository import Repository

from ui.widgets import Ui_Clone


class CloneTemplate(QWidget):
    def __init__(self, repository: Repository):
        super(CloneTemplate, self).__init__()
        self.ui = Ui_Clone()
        self.ui.setupUi(self)

        self.repo: Repository = repository

        self.config_ui()

        self.config()

        self.fill()

    def fill(self):
        self.ui.cloneWidget.setText("Clone")
        self.ui.httpsUrlLineEdit.setText(self.repo.clone_url)
        self.ui.sshUrlLineEdit.setText(self.repo.ssh_url)

    def config_ui(self):
        self.ui.cloneWidget.set_icon("fa5s.terminal")
        self.ui.httpsCopyButton.setIcon(qta.icon("fa5s.copy"))
        self.ui.sshCopyButton.setIcon(qta.icon("fa5s.copy"))

    def config(self):
        self.ui.httpsCopyButton.clicked.connect(
            lambda: QApplication.clipboard().setText(self.ui.httpsUrlLineEdit.text()))
        self.ui.sshCopyButton.clicked.connect(lambda: QApplication.clipboard().setText(self.ui.sshUrlLineEdit.text()))
