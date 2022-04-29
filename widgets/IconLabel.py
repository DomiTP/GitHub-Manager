import qtawesome as qta
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class IconLabel(QWidget):
    IconSize = QSize(16, 16)
    HorizontalSpacing = 2

    def __init__(self, text, qta_id=None, final_stretch=True):
        super(IconLabel, self).__init__()

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.icon = QLabel()
        if qta_id:
            self.icon.setPixmap(qta.icon(qta_id).pixmap(self.IconSize))

        layout.addWidget(self.icon)
        layout.addSpacing(self.HorizontalSpacing)
        self.label = QLabel(text)
        layout.addWidget(self.label)

        if final_stretch:
            layout.addStretch()

    def set_icon(self, qta_id):
        self.icon.setPixmap(qta.icon(qta_id).pixmap(self.IconSize))

    def setText(self, text):
        self.label.setText(text)
