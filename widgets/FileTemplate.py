from PySide6.QtWidgets import QWidget
from github.ContentFile import ContentFile

from ui.widgets import Ui_FileTemplate
from utils import format_file_size


class FileTemplate(QWidget):
    def __init__(self, content):
        super(FileTemplate, self).__init__()
        self.ui = Ui_FileTemplate()
        self.ui.setupUi(self)

        self.content: ContentFile = content

        self.fill()

    def fill(self):
        """
        Fill the widget with the data from the content file
        """
        self.ui.nameWidget.setText(self.content.name)
        self.ui.nameWidget.set_icon("fa5s.file-alt" if self.content.type == "file" else "fa5s.folder")
        self.ui.sizeLabel.setText(str(format_file_size(self.content.size, "B", "KB")) + " KB")
        if self.content.type == "dir":
            self.ui.sizeLabel.setText("")
