# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_repositories.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit, QListWidget,
                               QPushButton, QSizePolicy, QVBoxLayout)


class Ui_LocalRepositories(object):
    def setupUi(self, LocalRepositories):
        if not LocalRepositories.objectName():
            LocalRepositories.setObjectName(u"LocalRepositories")
        LocalRepositories.resize(556, 357)
        self.verticalLayout = QVBoxLayout(LocalRepositories)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(LocalRepositories)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(LocalRepositories)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_2 = QLineEdit(LocalRepositories)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.searchPathButton = QPushButton(LocalRepositories)
        self.searchPathButton.setObjectName(u"searchPathButton")

        self.horizontalLayout.addWidget(self.searchPathButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.searchButton = QPushButton(LocalRepositories)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.searchButton)

        self.retranslateUi(LocalRepositories)

        QMetaObject.connectSlotsByName(LocalRepositories)

    # setupUi

    def retranslateUi(self, LocalRepositories):
        LocalRepositories.setWindowTitle(QCoreApplication.translate("LocalRepositories", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LocalRepositories", u"Find a repository...", None))
        self.searchPathButton.setText(QCoreApplication.translate("LocalRepositories", u"Select directory", None))
        self.searchButton.setText(QCoreApplication.translate("LocalRepositories", u"Search", None))
    # retranslateUi
