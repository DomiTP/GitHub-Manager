# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'repository_template.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout)


class Ui_RepositoryTemplate(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 140)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.repoNameLabel = QLabel(Form)
        self.repoNameLabel.setObjectName(u"repoNameLabel")

        self.horizontalLayout.addWidget(self.repoNameLabel)

        self.visibilityLabel = QLabel(Form)
        self.visibilityLabel.setObjectName(u"visibilityLabel")

        self.horizontalLayout.addWidget(self.visibilityLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.starButton = QPushButton(Form)
        self.starButton.setObjectName(u"starButton")

        self.horizontalLayout.addWidget(self.starButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.repoDescLabel = QLabel(Form)
        self.repoDescLabel.setObjectName(u"repoDescLabel")

        self.verticalLayout_2.addWidget(self.repoDescLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.licenseIconLabel = QLabel(Form)
        self.licenseIconLabel.setObjectName(u"licenseIconLabel")

        self.horizontalLayout_2.addWidget(self.licenseIconLabel)

        self.licenseNameLabel = QLabel(Form)
        self.licenseNameLabel.setObjectName(u"licenseNameLabel")

        self.horizontalLayout_2.addWidget(self.licenseNameLabel)

        self.updatedLabel = QLabel(Form)
        self.updatedLabel.setObjectName(u"updatedLabel")

        self.horizontalLayout_2.addWidget(self.updatedLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.repoNameLabel.setText(QCoreApplication.translate("Form", u"repo-name", None))
        self.visibilityLabel.setText(QCoreApplication.translate("Form", u"public", None))
        self.starButton.setText(QCoreApplication.translate("Form", u"Star", None))
        self.repoDescLabel.setText(QCoreApplication.translate("Form", u"repo desc", None))
        self.licenseIconLabel.setText("")
        self.licenseNameLabel.setText(QCoreApplication.translate("Form", u"License Name", None))
        self.updatedLabel.setText(QCoreApplication.translate("Form", u"Updated", None))
    # retranslateUi
