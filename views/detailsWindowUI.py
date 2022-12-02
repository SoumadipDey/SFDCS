# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailsWindowoaBaLJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .customWidgets.qscrolllabel import QScrollLabel

from .resources_rc import *

class Ui_detailsWindow(object):
    def setupUi(self, detailsWindow):
        if not detailsWindow.objectName():
            detailsWindow.setObjectName(u"detailsWindow")
        detailsWindow.resize(500, 500)
        detailsWindow.setFixedSize(500,500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(detailsWindow.sizePolicy().hasHeightForWidth())
        detailsWindow.setSizePolicy(sizePolicy)
        detailsWindow.setMinimumSize(QSize(500, 500))
        detailsWindow.setMaximumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        detailsWindow.setWindowIcon(icon)
        detailsWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(detailsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticaBlFrame = QFrame(self.centralwidget)
        self.verticaBlFrame.setObjectName(u"verticaBlFrame")
        self.verticaBlFrame.setGeometry(QRect(0, 0, 500, 500))
        sizePolicy.setHeightForWidth(self.verticaBlFrame.sizePolicy().hasHeightForWidth())
        self.verticaBlFrame.setSizePolicy(sizePolicy)
        self.verticaBlFrame.setMinimumSize(QSize(500, 500))
        self.verticaBlFrame.setMaximumSize(QSize(500, 500))
        self.verticaBlFrame.setStyleSheet(u"background-color: rgb(205,214,219);\n"
"border: 1px solid rgb(205,214,219);")
        self.verticalLayout = QVBoxLayout(self.verticaBlFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.referencelImageLabel = QLabel(self.verticaBlFrame)
        self.referencelImageLabel.setObjectName(u"referencelImageLabel")
        sizePolicy.setHeightForWidth(self.referencelImageLabel.sizePolicy().hasHeightForWidth())
        self.referencelImageLabel.setSizePolicy(sizePolicy)
        self.referencelImageLabel.setMinimumSize(QSize(100, 100))
        self.referencelImageLabel.setMaximumSize(QSize(100, 100))
        self.referencelImageLabel.setStyleSheet(u"border: 2px solid rgb(85,101,85);\n"
"border-radius: 10px;")
        self.referencelImageLabel.setPixmap(QPixmap(u":/assets/assets/006-virus.png"))
        self.referencelImageLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.referencelImageLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalFrame_2 = QFrame(self.verticaBlFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalFrame_2.setMinimumSize(QSize(490, 70))
        self.horizontalFrame_2.setMaximumSize(QSize(490, 70))
        self.horizontalFrame_2.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalFrame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(100, 50))
        self.label_2.setMaximumSize(QSize(100, 50))
        self.label_2.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(85,101,85);\n"
"font: 10pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 5px; \n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.diseaseNameLabel = QLabel(self.horizontalFrame_2)
        self.diseaseNameLabel.setObjectName(u"diseaseNameLabel")
        self.diseaseNameLabel.setMinimumSize(QSize(364, 50))
        self.diseaseNameLabel.setMaximumSize(QSize(364, 50))
        font = QFont()
        font.setFamily(u"Product Sans Medium")
        font.setPointSize(10)
        self.diseaseNameLabel.setFont(font)
        self.diseaseNameLabel.setStyleSheet(u"background-color: rgb(205,214,219);\n"
"border: 1px solid  rgb(85,101,85);\n"
"padding-left : 5px;")
        self.diseaseNameLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.diseaseNameLabel)


        self.verticalLayout.addWidget(self.horizontalFrame_2, 0, Qt.AlignHCenter)

        self.horizontalFrame_4 = QFrame(self.verticaBlFrame)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_4.setSizePolicy(sizePolicy1)
        self.horizontalFrame_4.setMinimumSize(QSize(490, 70))
        self.horizontalFrame_4.setMaximumSize(QSize(490, 70))
        self.horizontalFrame_4.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.horizontalFrame_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(100, 50))
        self.label_3.setMaximumSize(QSize(100, 50))
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(85,101,85);\n"
"font: 10pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 5px; \n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.pathogenLabel = QLabel(self.horizontalFrame_4)
        self.pathogenLabel.setObjectName(u"pathogenLabel")
        self.pathogenLabel.setMinimumSize(QSize(364, 50))
        self.pathogenLabel.setMaximumSize(QSize(364, 50))
        self.pathogenLabel.setFont(font)
        self.pathogenLabel.setStyleSheet(u"background-color: rgb(205,214,219);\n"
"border: 1px solid  rgb(85,101,85);\n"
"padding-left : 5px;")
        self.pathogenLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.pathogenLabel)


        self.verticalLayout.addWidget(self.horizontalFrame_4, 0, Qt.AlignHCenter)

        self.horizontalFrame_3 = QFrame(self.verticaBlFrame)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_3.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_3.setSizePolicy(sizePolicy1)
        self.horizontalFrame_3.setMinimumSize(QSize(490, 90))
        self.horizontalFrame_3.setMaximumSize(QSize(490, 90))
        self.horizontalFrame_3.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.horizontalFrame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(100, 80))
        self.label_4.setMaximumSize(QSize(100, 80))
        self.label_4.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(85,101,85);\n"
"font: 10pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 5px; \n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.symptomsLabel = QScrollLabel(self.horizontalFrame_3)
        self.symptomsLabel.setObjectName(u"symptomsLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.symptomsLabel.sizePolicy().hasHeightForWidth())
        self.symptomsLabel.setSizePolicy(sizePolicy3)
        self.symptomsLabel.setMinimumSize(QSize(364, 80))
        self.symptomsLabel.setMaximumSize(QSize(364, 80))
        self.symptomsLabel.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Product Sans Medium")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.symptomsLabel.setFont(font1)
        self.symptomsLabel.setAutoFillBackground(False)
        self.symptomsLabel.setStyleSheet(u"QScrollArea{\n"
"	background-color: rgb(205,214,219);\n"
"	border: 1px solid  rgb(85,101,85);\n"
"	padding-left: 5px;\n"
"	font: 10pt \"Product Sans Medium\";\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.symptomsLabel.setWidgetResizable(True)
        '''self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 68))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: none;\n"
"border-radius: 0px;")
        self.symptomsLabel.setWidget(self.scrollAreaWidgetContents)'''

        self.horizontalLayout_4.addWidget(self.symptomsLabel)


        self.verticalLayout.addWidget(self.horizontalFrame_3, 0, Qt.AlignHCenter)

        self.horizontalFrame_5 = QFrame(self.verticaBlFrame)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_5.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_5.setSizePolicy(sizePolicy1)
        self.horizontalFrame_5.setMinimumSize(QSize(490, 90))
        self.horizontalFrame_5.setMaximumSize(QSize(490, 90))
        self.horizontalFrame_5.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.horizontalFrame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(100, 80))
        self.label_6.setMaximumSize(QSize(100, 80))
        self.label_6.setStyleSheet(u"color: rgb(255,255,255);\n"
"background-color: rgb(85,101,85);\n"
"font: 10pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 5px; \n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.favCondLabel = QScrollLabel(self.horizontalFrame_5)
        self.favCondLabel.setObjectName(u"favCondLabel")
        sizePolicy3.setHeightForWidth(self.favCondLabel.sizePolicy().hasHeightForWidth())
        self.favCondLabel.setSizePolicy(sizePolicy3)
        self.favCondLabel.setMinimumSize(QSize(364, 80))
        self.favCondLabel.setMaximumSize(QSize(364, 80))
        self.favCondLabel.setBaseSize(QSize(0, 0))
        self.favCondLabel.setFont(font1)
        self.favCondLabel.setAutoFillBackground(False)
        self.favCondLabel.setStyleSheet(u"QScrollArea{\n"
"	background-color: rgb(205,214,219);\n"
"	border: 1px solid  rgb(85,101,85);\n"
"	padding-left: 5px;\n"
"	font: 10pt \"Product Sans Medium\";\n"
"	padding-top: 2px;\n"
"}\n"
"\n"
"\n"
"")
        self.favCondLabel.setWidgetResizable(True)
        '''self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 352, 68))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"border: none;\n"
"border-radius: 0px;")
        self.favCondLabel.setWidget(self.scrollAreaWidgetContents_2)'''

        self.horizontalLayout_6.addWidget(self.favCondLabel)


        self.verticalLayout.addWidget(self.horizontalFrame_5, 0, Qt.AlignHCenter)

        detailsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(detailsWindow)

        QMetaObject.connectSlotsByName(detailsWindow)
    # setupUi

    def retranslateUi(self, detailsWindow):
        detailsWindow.setWindowTitle(QCoreApplication.translate("detailsWindow", u"Details", None))
        self.referencelImageLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("detailsWindow", u"Name", None))
        self.diseaseNameLabel.setText(QCoreApplication.translate("detailsWindow", u"NULL", None))
        self.label_3.setText(QCoreApplication.translate("detailsWindow", u"Pathogen", None))
        self.pathogenLabel.setText(QCoreApplication.translate("detailsWindow", u"NULL", None))
        self.label_4.setText(QCoreApplication.translate("detailsWindow", u"Symptoms", None))
        self.label_6.setText(QCoreApplication.translate("detailsWindow", u"Favourable Conditions", None))
    # retranslateUi

