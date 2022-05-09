import os

from PySide6.QtWidgets import QWidget, QFileDialog

from modules.local_repository import LocalRepository
from ui.widgets import Ui_LocalRepositories
from utils import USER_HOME_PATH
from widgets import LocalRepositoryListWidgetItem
from widgets.LocalRepositoryTemplate import LocalRepositoryTemplate


class LocalRepositories(QWidget):
    def __init__(self, user):
        super(LocalRepositories, self).__init__()
        self.ui = Ui_LocalRepositories()
        self.ui.setupUi(self)

        self.user = user
        self.open_repo = None

        self.config()
        self.load_items()

    def load_items(self, route=USER_HOME_PATH):
        """
        Loads the repositories of the user in the listWidget
        """
        self.ui.searchButton.setDisabled(True)
        self.ui.listWidget.clear()
        for root, subdirs, files in os.walk(str(route)):
            for d in subdirs:
                if os.access(root, os.R_OK):
                    if d == ".git":
                        folder_name = root.split(os.sep)[-1]
                        item = LocalRepositoryListWidgetItem(folder_name, root)
                        widget = LocalRepositoryTemplate(root, self.user)
                        item.setSizeHint(widget.sizeHint())
                        self.ui.listWidget.addItem(item)
                        self.ui.listWidget.setItemWidget(item, widget)
                else:
                    print(d + " No permission")
        self.ui.searchButton.setEnabled(True)

    def config(self):
        """
        Configures the signals of the widget
        """
        self.ui.listWidget.itemClicked.connect(self.open_repository)
        self.ui.searchPathButton.clicked.connect(self.save_path)
        self.ui.searchButton.clicked.connect(lambda: self.load_items(self.ui.lineEdit_2.text()))
        self.ui.lineEdit_2.setText(str(USER_HOME_PATH))

    def save_path(self):
        """
        Repository save path
        """
        new_route = QFileDialog.getExistingDirectory(self, "Select folder", str(USER_HOME_PATH))
        if new_route:
            self.ui.lineEdit_2.setText(new_route)

    def open_repository(self, item):
        """
        Opens the repository selected in a new window
        """
        repo_name = item.path
        self.open_repo = LocalRepository(repo_name, self.user)
        self.open_repo.show()
