# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repositories.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QLineEdit, QListWidget, QVBoxLayout)


class Ui_Repositories(object):
    def setupUi(self, Repositories):
        if not Repositories.objectName():
            Repositories.setObjectName(u"Repositories")
        Repositories.resize(556, 357)
        self.verticalLayout = QVBoxLayout(Repositories)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Repositories)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(Repositories)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Repositories)

        QMetaObject.connectSlotsByName(Repositories)

    # setupUi

    def retranslateUi(self, Repositories):
        Repositories.setWindowTitle(QCoreApplication.translate("Repositories", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Repositories", u"Find a repository...", None))
    # retranslateUi
