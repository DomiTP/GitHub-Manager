from PySide6.QtWidgets import QWidget, QListWidgetItem

from ui import Ui_Repositories
from widgets import RepositoryTemplate


class Repositories(QWidget):
    def __init__(self, user):
        super(Repositories, self).__init__()
        self.ui = Ui_Repositories()
        self.ui.setupUi(self)

        self.user = user

        self.load_items()

    def load_items(self):
        for repo in self.user.get_repos():
            item = QListWidgetItem()
            widget = RepositoryTemplate(repo)
            item.setSizeHint(widget.sizeHint())
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, widget)
