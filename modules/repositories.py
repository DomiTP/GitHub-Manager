import qtawesome as qta
from PySide6.QtCore import QRunnable, Signal, Slot, QThreadPool, QObject
from PySide6.QtWidgets import QWidget, QListWidgetItem
from github.Repository import Repository as GithubRepository

from modules.create_repository import CreateRepository
from modules.repository import Repository
from ui import Ui_Repositories
from widgets import RepositoryTemplate, RepositoriesListWidgetItem


class WorkerSignals(QObject):
    repo = Signal(GithubRepository)
    error = Signal(tuple)
    finished = Signal()


class Worker(QRunnable):
    def __init__(self, user, ui):
        super().__init__()
        self.user = user
        self.ui = ui
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        for repo in self.user.get_repos():
            self.signals.repo.emit(repo)
        self.signals.finished.emit()


class Repositories(QWidget):
    def __init__(self, user):
        super(Repositories, self).__init__()
        self.ui = Ui_Repositories()
        self.ui.setupUi(self)

        self.user = user
        self.open_repo = None
        self.worker = Worker(self.user, self.ui)

        self.threadpool = QThreadPool()

        self.config()
        self.async_load_items()

    def async_load_items(self):
        """
        Loads the repositories of the user in the listWidget asynchronously
        """
        self.worker.signals.repo.connect(self.add_repo)
        self.worker.signals.finished.connect(self.finished)
        self.ui.lineEdit.setDisabled(True)
        self.ui.newButton.setDisabled(True)
        self.threadpool.start(self.worker)

    @Slot(GithubRepository)
    def add_repo(self, repo):
        item = QListWidgetItem()
        item.setToolTip(repo.name)
        widget = RepositoryTemplate(repo, self.user.get_data())
        item.setSizeHint(widget.sizeHint())
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, widget)

    def finished(self):
        self.ui.lineEdit.setEnabled(True)
        self.ui.newButton.setEnabled(True)

    def config(self):
        """
        Configures the signals of the widget
        """
        self.ui.listWidget.clicked.connect(self.open_repository)
        self.ui.newButton.setIcon(qta.icon('ph.book-bookmark', color='black'))
        self.ui.newButton.clicked.connect(self.create_repository)
        self.ui.newButton.setToolTip("Create a new repository")
        self.ui.lineEdit.textChanged.connect(self.on_text_changed)

    def create_repository(self):
        """
        Opens a new window to create a new repository
        """
        create_repo = CreateRepository(self.user)
        create_repo.show()

    def open_repository(self):
        """
        Opens the repository selected in a new window
        """
        item = self.ui.listWidget.currentItem()
        repo_name = item.toolTip()
        self.open_repo = Repository(self.user.user.get_repo(repo_name), self.user)
        self.open_repo.show()

    def on_text_changed(self, text):
        """
        Filters the repositories with the text entered the lineEdit
        """
        for row in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(row)
            widget = self.ui.listWidget.itemWidget(item)
            if text:
                item.setHidden(not widget.repo.name.lower().startswith(text.lower()))
            else:
                item.setHidden(False)
