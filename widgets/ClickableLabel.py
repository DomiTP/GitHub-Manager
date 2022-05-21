from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def mouseReleaseEvent(self, ev):
        self.clicked.emit()
