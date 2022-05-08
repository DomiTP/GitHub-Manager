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

    def set_icon(self, qta_id, color="black", size=IconSize):
        """
        Set the icon to the label with the given qta_id.
        :param qta_id: The qta_id of the icon.
        :param color:  The color of the icon.
        :param size:  The size of the icon.
        """
        self.icon.setPixmap(qta.icon(qta_id, color=color).pixmap(size))

    def setText(self, text):
        """
        Set the text of the label.
        :param text:  The text to set.
        """
        self.label.setText(text)

    def set_text_style(self, color=None, font_size=None, bold=False, italic=False, underline=False, font_family=None):
        """
        Set the style of the label.
        :param color:  The color of the text.
        :param font_size:  The size of the font.
        :param bold:  Whether the text is bold.
        :param italic:  Whether the text is italic.
        :param underline:  Whether the text is underlined.
        :param font_family:  The font family of the text.
        """
        style = ""
        if color:
            style += "color: %s;" % color
        if font_size:
            style += "font-size: %spx;" % font_size
        if bold:
            style += "font-weight: bold;"
        if italic:
            style += "font-style: italic;"
        if underline:
            style += "text-decoration: underline;"
        if font_family:
            style += "font-family: %s;" % font_family
        self.label.setStyleSheet(style)
