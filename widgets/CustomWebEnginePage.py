from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView


class CustomWebEnginePage(QWebEnginePage):
    external_windows = []

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            w = QWebEngineView()
            w.setUrl(url)
            w.show()

            self.external_windows.append(w)
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)
