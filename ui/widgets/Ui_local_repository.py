# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_repository.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFormLayout, QLabel, QLineEdit,
                               QSizePolicy, QVBoxLayout)


class Ui_localRepository(object):
    def setupUi(self, localRepository):
        if not localRepository.objectName():
            localRepository.setObjectName(u"localRepository")
        localRepository.resize(936, 640)
        self.verticalLayout = QVBoxLayout(localRepository)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.repoLabel = QLabel(localRepository)
        self.repoLabel.setObjectName(u"repoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repoLabel.sizePolicy().hasHeightForWidth())
        self.repoLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.repoLabel.setFont(font)

        self.verticalLayout.addWidget(self.repoLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.fullNameLabel = QLabel(localRepository)
        self.fullNameLabel.setObjectName(u"fullNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fullNameLabel)

        self.fullNameLineEdit = QLineEdit(localRepository)
        self.fullNameLineEdit.setObjectName(u"fullNameLineEdit")
        self.fullNameLineEdit.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fullNameLineEdit)

        self.ownerLabel = QLabel(localRepository)
        self.ownerLabel.setObjectName(u"ownerLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.ownerLabel)

        self.ownerLineEdit = QLineEdit(localRepository)
        self.ownerLineEdit.setObjectName(u"ownerLineEdit")
        self.ownerLineEdit.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ownerLineEdit)

        self.descriptionLabel = QLabel(localRepository)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.descriptionLabel)

        self.descriptionLineEdit = QLineEdit(localRepository)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")
        self.descriptionLineEdit.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.descriptionLineEdit)

        self.createdAtLabel = QLabel(localRepository)
        self.createdAtLabel.setObjectName(u"createdAtLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.createdAtLabel)

        self.createdAtLineEdit = QLineEdit(localRepository)
        self.createdAtLineEdit.setObjectName(u"createdAtLineEdit")
        self.createdAtLineEdit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.createdAtLineEdit)

        self.updatedLabel = QLabel(localRepository)
        self.updatedLabel.setObjectName(u"updatedLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.updatedLabel)

        self.updatedLineEdit = QLineEdit(localRepository)
        self.updatedLineEdit.setObjectName(u"updatedLineEdit")
        self.updatedLineEdit.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.updatedLineEdit)

        self.languageLabel = QLabel(localRepository)
        self.languageLabel.setObjectName(u"languageLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.languageLabel)

        self.languageLineEdit = QLineEdit(localRepository)
        self.languageLineEdit.setObjectName(u"languageLineEdit")
        self.languageLineEdit.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.languageLineEdit)

        self.forksLabel = QLabel(localRepository)
        self.forksLabel.setObjectName(u"forksLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.forksLabel)

        self.forksLineEdit = QLineEdit(localRepository)
        self.forksLineEdit.setObjectName(u"forksLineEdit")
        self.forksLineEdit.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.forksLineEdit)

        self.starsLabel = QLabel(localRepository)
        self.starsLabel.setObjectName(u"starsLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.starsLabel)

        self.starsLineEdit = QLineEdit(localRepository)
        self.starsLineEdit.setObjectName(u"starsLineEdit")
        self.starsLineEdit.setReadOnly(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.starsLineEdit)

        self.subscribersLabel = QLabel(localRepository)
        self.subscribersLabel.setObjectName(u"subscribersLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.subscribersLabel)

        self.subscribersLineEdit = QLineEdit(localRepository)
        self.subscribersLineEdit.setObjectName(u"subscribersLineEdit")
        self.subscribersLineEdit.setReadOnly(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.subscribersLineEdit)

        self.licenseLabel = QLabel(localRepository)
        self.licenseLabel.setObjectName(u"licenseLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.licenseLabel)

        self.licenseLineEdit = QLineEdit(localRepository)
        self.licenseLineEdit.setObjectName(u"licenseLineEdit")
        self.licenseLineEdit.setReadOnly(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.licenseLineEdit)

        self.verticalLayout.addLayout(self.formLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(localRepository)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.commitsImageLabel = QLabel(localRepository)
        self.commitsImageLabel.setObjectName(u"commitsImageLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.commitsImageLabel.sizePolicy().hasHeightForWidth())
        self.commitsImageLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.commitsImageLabel)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(localRepository)

        QMetaObject.connectSlotsByName(localRepository)

    # setupUi

    def retranslateUi(self, localRepository):
        localRepository.setWindowTitle(QCoreApplication.translate("localRepository", u"Form", None))
        self.repoLabel.setText(QCoreApplication.translate("localRepository", u"repo", None))
        self.fullNameLabel.setText(QCoreApplication.translate("localRepository", u"Full name", None))
        self.ownerLabel.setText(QCoreApplication.translate("localRepository", u"Owner", None))
        self.descriptionLabel.setText(QCoreApplication.translate("localRepository", u"Description", None))
        self.createdAtLabel.setText(QCoreApplication.translate("localRepository", u"Created at", None))
        self.updatedLabel.setText(QCoreApplication.translate("localRepository", u"Updated", None))
        self.languageLabel.setText(QCoreApplication.translate("localRepository", u"Language", None))
        self.forksLabel.setText(QCoreApplication.translate("localRepository", u"Forks", None))
        self.starsLabel.setText(QCoreApplication.translate("localRepository", u"Stars", None))
        self.subscribersLabel.setText(QCoreApplication.translate("localRepository", u"Subscribers", None))
        self.licenseLabel.setText(QCoreApplication.translate("localRepository", u"License", None))
        self.label.setText(QCoreApplication.translate("localRepository", u"Commits", None))
        self.commitsImageLabel.setText("")
    # retranslateUi
