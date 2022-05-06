from PySide6.QtWidgets import QWidget, QListWidgetItem

from modules.repository import Repository
from ui import Ui_Repositories
from widgets import RepositoryTemplate


class Repositories(QWidget):
    def __init__(self, user):
        super(Repositories, self).__init__()
        self.ui = Ui_Repositories()
        self.ui.setupUi(self)

        self.user = user
        self.open_repo = None

        self.load_items()
        self.config()

    def load_items(self):
        """
        Loads the repositories of the user in the listWidget
        """
        for repo in self.user.get_repos():
            item = QListWidgetItem()
            item.setToolTip(repo.name)
            widget = RepositoryTemplate(repo, self.user.get_data())
            item.setSizeHint(widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)

    def config(self):
        """
        Configures the signals of the widget
        """
        self.ui.listWidget.clicked.connect(self.open_repository)

    def open_repository(self):
        """
        Opens the repository selected in a new window
        """
        item = self.ui.listWidget.currentItem()
        repo_name = item.toolTip()
        self.open_repo = Repository(self.user.user.get_repo(repo_name), self.user.get_data())
        self.open_repo.show()
