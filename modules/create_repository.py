from PySide6.QtWidgets import QWidget, QMessageBox
from github import GithubException

from modules.repository import Repository
from ui.widgets import Ui_CreateRepo


class CreateRepository(QWidget):
    def __init__(self, user):
        super(CreateRepository, self).__init__()

        self.ui = Ui_CreateRepo()
        self.ui.setupUi(self)

        self.user = user

        self.new_repo = None

        self.config()
        self.fill()

    def fill(self):
        ignores = [""]
        repo = self.user.github.get_repo("github/gitignore")
        for file in repo.get_contents(""):
            if file.type == "file":
                ignores.append(file.name.split(".")[0])
        self.ui.gitignoreTemplateComboBox.add_items(ignores)

        licenses = ["", "MIT", "ISC", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "GPL-2.0", "GPL-3.0", "LGPL-2.1",
                    "LGPL-3.0", "Unlicense", "AGPL-3.0"]

        self.ui.licenseTemplateComboBox.add_items(licenses)

    def config(self):
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.createRepoButton.clicked.connect(self.create_repo)

    def create_repo(self):
        """
        Create a new repository.
        """
        if self.message('warning', 'Are you sure you want to create this repository?'):
            if self.ui.nameLineEdit.text() != '':
                try:
                    repo = self.user.get_data().create_repo(
                        name=self.ui.nameLineEdit.text(),
                        description=self.ui.descriptionLineEdit.text(),
                        homepage=self.ui.homepageLineEdit.text(),
                        private=self.ui.privateCheckBox.isChecked(),
                        has_issues=self.ui.hasIssuesCheckBox.isChecked(),
                        has_wiki=self.ui.hasWikiCheckBox.isChecked(),
                        has_downloads=self.ui.hasDownloadsCheckBox.isChecked(),
                        auto_init=self.ui.autoInitCheckBox.isChecked(),
                        allow_merge_commit=self.ui.allowMergeCommitCheckBox.isChecked(),
                        allow_rebase_merge=self.ui.allowRebaseMergeCheckBox.isChecked(),
                        license_template=self.ui.licenseTemplateComboBox.currentText(),
                        gitignore_template=self.ui.gitignoreTemplateComboBox.currentText())

                    self.new_repo = Repository(repo, self.user)
                    self.new_repo.show()

                    self.close()
                except GithubException as e:
                    print(e.status, e.data, e.headers)
                    self.message('error', e.data['message'], e.data['errors'][0]['message'])
            else:
                self.message('error', 'Repository name cannot be empty')

    def message(self, type_, message, additional_info=None):
        """
        Show a message box with the given type and message.
        :param type_:  Type of the message box.
        :param message:  Message to show.
        :param additional_info:  Additional information to show.
        :return:  True if the user clicked the Yes button, False if the user clicked the No button,
        or None if the user clicked the OK button.
        """
        messagebox = QMessageBox()
        if type_ == 'error':
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setWindowTitle('Error')
            messagebox.setStandardButtons(QMessageBox.Ok)
        elif type_ == 'warning':
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle('Warning')
            messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        elif type_ == 'success':
            messagebox.setIcon(QMessageBox.Information)
            messagebox.setWindowTitle('Success')
            messagebox.setStandardButtons(QMessageBox.Ok)

        messagebox.setText(message)
        if additional_info:
            messagebox.setDetailedText(additional_info)

        result = messagebox.exec()
        if result == QMessageBox.Yes:
            ret = True
        elif result == QMessageBox.No:
            ret = False
        else:
            ret = None

        return ret
