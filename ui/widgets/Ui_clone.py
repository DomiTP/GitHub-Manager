# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clone.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit, QPushButton,
                               QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from widgets.IconLabel import IconLabel


class Ui_Clone(object):
    def setupUi(self, Clone):
        if not Clone.objectName():
            Clone.setObjectName(u"Clone")
        Clone.resize(391, 113)
        self.verticalLayout = QVBoxLayout(Clone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cloneWidget = IconLabel(Clone)
        self.cloneWidget.setObjectName(u"cloneWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cloneWidget.sizePolicy().hasHeightForWidth())
        self.cloneWidget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.cloneWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(Clone)
        self.tabWidget.setObjectName(u"tabWidget")
        self.https = QWidget()
        self.https.setObjectName(u"https")
        self.horizontalLayout_3 = QHBoxLayout(self.https)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.httpsUrlLineEdit = QLineEdit(self.https)
        self.httpsUrlLineEdit.setObjectName(u"httpsUrlLineEdit")

        self.horizontalLayout_3.addWidget(self.httpsUrlLineEdit)

        self.httpsCopyButton = QPushButton(self.https)
        self.httpsCopyButton.setObjectName(u"httpsCopyButton")
        sizePolicy.setHeightForWidth(self.httpsCopyButton.sizePolicy().hasHeightForWidth())
        self.httpsCopyButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.httpsCopyButton)

        self.tabWidget.addTab(self.https, "")
        self.ssh = QWidget()
        self.ssh.setObjectName(u"ssh")
        self.horizontalLayout_2 = QHBoxLayout(self.ssh)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sshUrlLineEdit = QLineEdit(self.ssh)
        self.sshUrlLineEdit.setObjectName(u"sshUrlLineEdit")
        self.sshUrlLineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.sshUrlLineEdit)

        self.sshCopyButton = QPushButton(self.ssh)
        self.sshCopyButton.setObjectName(u"sshCopyButton")
        sizePolicy.setHeightForWidth(self.sshCopyButton.sizePolicy().hasHeightForWidth())
        self.sshCopyButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.sshCopyButton)

        self.tabWidget.addTab(self.ssh, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Clone)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Clone)

    # setupUi

    def retranslateUi(self, Clone):
        Clone.setWindowTitle(QCoreApplication.translate("Clone", u"Form", None))
        self.httpsCopyButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.https),
                                  QCoreApplication.translate("Clone", u"HTTPS", None))
        self.sshCopyButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ssh), QCoreApplication.translate("Clone", u"SSH", None))
    # retranslateUi
