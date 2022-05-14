from PySide6.QtWidgets import QListWidgetItem


class RepositoryListWidgetItem(QListWidgetItem):
    def __init__(self, name, is_directory, url, path="", contents=None):
        super().__init__()
        self.name = name
        self.isDirectory = is_directory
        self.url = url
        self.contents = contents
        self.path = path
