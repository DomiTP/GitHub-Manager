from PySide6.QtWidgets import QWidget
from github.ContentFile import ContentFile

from ui.widgets import Ui_FileTemplate


class FileTemplate(QWidget):
    def __init__(self, content):
        super(FileTemplate, self).__init__()
        self.ui = Ui_FileTemplate()
        self.ui.setupUi(self)

        self.content: ContentFile = content
        # self.commit = repo.get_commit(self.content.sha)

        self.fill()

    def fill(self):
        """
        Fill the widget with the data from the content file
        """
        self.ui.nameWidget.setText(self.content.name)
        self.ui.nameWidget.set_icon("fa5s.file-alt" if self.content.type == "file" else "fa5s.folder")
        # self.ui.commitLabel.setText(self.commit.message)
        # self.ui.label.setText(time("", self.commit.author.date))
