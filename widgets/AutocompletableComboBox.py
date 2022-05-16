from PySide6.QtCore import Qt
from PySide6.QtWidgets import QCompleter, QComboBox


def completion(word_list, widget, i=True):
    """
    Autocompletion of sender and subject
    """
    word_set = set(word_list)
    completer = QCompleter(word_set)
    if i:
        completer.setCaseSensitivity(Qt.CaseInsensitive)
    else:
        completer.setCaseSensitivity(Qt.CaseSensitive)
    widget.setCompleter(completer)


class Autocomplete(QComboBox):
    def __init__(self, i=False, allow_duplicates=True):
        super(Autocomplete, self).__init__()
        self.insensitivity = i
        self.allowDuplicates = allow_duplicates
        self.init()

    def init(self):
        self.setEditable(True)
        self.setDuplicatesEnabled(self.allowDuplicates)

    def set_autocompletion(self, items, i):
        completion(items, self, i)

    def remove_item(self, item):
        self.removeItem(item)

    def clear_items(self):
        self.clear()

    def add_items(self, items):
        self.addItems(items)
        self.set_autocompletion(items, i=self.insensitivity)
