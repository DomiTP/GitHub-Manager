from PySide6.QtWidgets import QListWidgetItem


class LocalRepositoryListWidgetItem(QListWidgetItem):
    def __init__(self, name, path):
        super().__init__()
        self.name = name
        self.path = path
