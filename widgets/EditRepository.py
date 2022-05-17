from PySide6.QtWidgets import QWidget
from github import GithubException

from ui.widgets import Ui_RepositoryEdit
from utils import delete_repository_dialog, message


class EditRepository(QWidget):
    def __init__(self, repo, repo_widget):
        super(EditRepository, self).__init__()

        self.ui = Ui_RepositoryEdit()
        self.ui.setupUi(self)

        self.repo = repo
        self.repo_widget = repo_widget

        self.fill()
        self.config()

    def fill(self):
        self.ui.nameLineEdit.setText(self.repo.name)
        self.ui.descriptionLineEdit.setText(self.repo.description)
        self.ui.homePageLineEdit.setText(self.repo.homepage)
        self.ui.privateCheckBox.setChecked(self.repo.private)
        for branch in self.repo.get_branches():
            self.ui.defaultBranchComboBox.addItem(branch.name)
        self.ui.defaultBranchComboBox.setCurrentText(self.repo.default_branch)

    def config(self):
        self.ui.acceptButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        self.ui.deleteButton.clicked.connect(self.delete)

    def accept(self):
        self.repo.edit(
            name=self.ui.nameLineEdit.text(),
            description=self.ui.descriptionLineEdit.text(),
            homepage=self.ui.homePageLineEdit.text(),
            private=self.ui.privateCheckBox.isChecked(),
            default_branch=self.ui.defaultBranchComboBox.currentText(),
        )
        self.close()

    def delete(self):
        if delete_repository_dialog('remote'):
            try:
                self.repo.delete()
                message('success', 'Repository deleted')
                self.repo_widget.close()
                self.close()
            except GithubException as e:
                message('error', e.data['message'])
