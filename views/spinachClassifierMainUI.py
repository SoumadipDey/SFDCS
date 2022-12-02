# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spinachClassifierMainUIanMKVW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 480)
        MainWindow.setFixedSize(940,480)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(940, 480))
        MainWindow.setMaximumSize(QSize(940, 480))
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.990000000000000)
        MainWindow.setIconSize(QSize(40, 40))
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalBaseFrame = QFrame(self.centralwidget)
        self.verticalBaseFrame.setObjectName(u"verticalBaseFrame")
        self.verticalBaseFrame.setGeometry(QRect(0, 0, 952, 480))
        sizePolicy.setHeightForWidth(self.verticalBaseFrame.sizePolicy().hasHeightForWidth())
        self.verticalBaseFrame.setSizePolicy(sizePolicy)
        self.verticalBaseFrame.setMinimumSize(QSize(952, 480))
        self.verticalBaseFrame.setMaximumSize(QSize(952, 480))
        self.verticalBaseFrame.setStyleSheet(u"background-color: rgb(205,214,219);\n"
"border: 1px solid rgb(205,214,219);")
        self.verticalBaseFrame.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout = QVBoxLayout(self.verticalBaseFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.headingLabel = QLabel(self.verticalBaseFrame)
        self.headingLabel.setObjectName(u"headingLabel")
        sizePolicy.setHeightForWidth(self.headingLabel.sizePolicy().hasHeightForWidth())
        self.headingLabel.setSizePolicy(sizePolicy)
        self.headingLabel.setMinimumSize(QSize(910, 30))
        self.headingLabel.setMaximumSize(QSize(910, 30))
        self.headingLabel.setSizeIncrement(QSize(0, 0))
        self.headingLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85,101,85);\n"
"font: 14pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 5px; ")

        self.verticalLayout.addWidget(self.headingLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.contentlFrame = QFrame(self.verticalBaseFrame)
        self.contentlFrame.setObjectName(u"contentlFrame")
        sizePolicy.setHeightForWidth(self.contentlFrame.sizePolicy().hasHeightForWidth())
        self.contentlFrame.setSizePolicy(sizePolicy)
        self.contentlFrame.setMinimumSize(QSize(930, 395))
        self.contentlFrame.setMaximumSize(QSize(930, 395))
        self.contentlFrame.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.contentlFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputDataVerticalFrame = QFrame(self.contentlFrame)
        self.inputDataVerticalFrame.setObjectName(u"inputDataVerticalFrame")
        sizePolicy.setHeightForWidth(self.inputDataVerticalFrame.sizePolicy().hasHeightForWidth())
        self.inputDataVerticalFrame.setSizePolicy(sizePolicy)
        self.inputDataVerticalFrame.setMinimumSize(QSize(460, 394))
        self.inputDataVerticalFrame.setMaximumSize(QSize(460, 394))
        self.inputDataVerticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.inputDataVerticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectedImageLabel = QLabel(self.inputDataVerticalFrame)
        self.selectedImageLabel.setObjectName(u"selectedImageLabel")
        sizePolicy.setHeightForWidth(self.selectedImageLabel.sizePolicy().hasHeightForWidth())
        self.selectedImageLabel.setSizePolicy(sizePolicy)
        self.selectedImageLabel.setMinimumSize(QSize(300, 300))
        self.selectedImageLabel.setMaximumSize(QSize(300, 300))
        self.selectedImageLabel.setStyleSheet(u"/*border: 1px solid rgb(85,101,85);*/\n"
"border-radius: 15px;")
        self.selectedImageLabel.setPixmap(QPixmap(u":/assets/assets/spinach.png"))
        self.selectedImageLabel.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.selectedImageLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.buttonFrame = QFrame(self.inputDataVerticalFrame)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.browseBtn = QPushButton(self.buttonFrame)
        self.browseBtn.setObjectName(u"browseBtn")
        sizePolicy.setHeightForWidth(self.browseBtn.sizePolicy().hasHeightForWidth())
        self.browseBtn.setSizePolicy(sizePolicy)
        self.browseBtn.setMinimumSize(QSize(200, 40))
        self.browseBtn.setMaximumSize(QSize(200, 40))
        self.browseBtn.setStyleSheet(u"QPushButton { color: rgb(255, 255, 255);\n"
"background-color: rgb(128,152,121);\n"
"font: 12pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 8px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed { background-color: rgb(128,152,121); }\n"
"QPushButton:hover { border-color: rgb(182,191,121);\n"
"color: rgb(0,0,0);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/002-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browseBtn.setIcon(icon1)
        self.browseBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.browseBtn)

        self.horizontalSpacer_2 = QSpacerItem(10, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.predictBtn = QPushButton(self.buttonFrame)
        self.predictBtn.setObjectName(u"predictBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.predictBtn.sizePolicy().hasHeightForWidth())
        self.predictBtn.setSizePolicy(sizePolicy1)
        self.predictBtn.setMinimumSize(QSize(200, 40))
        self.predictBtn.setMaximumSize(QSize(200, 40))
        self.predictBtn.setStyleSheet(u"QPushButton { color: rgb(255, 255, 255);\n"
"background-color: rgb(128,152,121);\n"
"font: 12pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 8px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed { background-color: rgb(128,152,121); }\n"
"QPushButton:hover { border-color: rgb(182,191,121);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/005-nature-product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.predictBtn.setIcon(icon2)
        self.predictBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.predictBtn)


        self.verticalLayout_2.addWidget(self.buttonFrame)


        self.horizontalLayout.addWidget(self.inputDataVerticalFrame)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dataViewGridlayout = QFrame(self.contentlFrame)
        self.dataViewGridlayout.setObjectName(u"dataViewGridlayout")
        sizePolicy.setHeightForWidth(self.dataViewGridlayout.sizePolicy().hasHeightForWidth())
        self.dataViewGridlayout.setSizePolicy(sizePolicy)
        self.dataViewGridlayout.setMinimumSize(QSize(420, 380))
        self.dataViewGridlayout.setMaximumSize(QSize(420, 380))
        self.dataViewGridlayout.setStyleSheet(u"/* border: 1px solid rgb(85,101,85);*/\n"
"border-radius: 15px;")
        self.formLayout = QFormLayout(self.dataViewGridlayout)
        self.formLayout.setObjectName(u"formLayout")
        self.diseaseNamelFrame = QFrame(self.dataViewGridlayout)
        self.diseaseNamelFrame.setObjectName(u"diseaseNamelFrame")
        sizePolicy.setHeightForWidth(self.diseaseNamelFrame.sizePolicy().hasHeightForWidth())
        self.diseaseNamelFrame.setSizePolicy(sizePolicy)
        self.diseaseNamelFrame.setMinimumSize(QSize(400, 40))
        self.diseaseNamelFrame.setMaximumSize(QSize(400, 40))
        self.diseaseNamelFrame.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.horizontalLayout_6 = QHBoxLayout(self.diseaseNamelFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.labelName = QLabel(self.diseaseNamelFrame)
        self.labelName.setObjectName(u"labelName")
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)
        self.labelName.setMinimumSize(QSize(100, 20))
        self.labelName.setMaximumSize(QSize(100, 20))
        font1 = QFont()
        font1.setFamily(u"Product Sans Medium")
        font1.setPointSize(10)
        self.labelName.setFont(font1)
        self.labelName.setStyleSheet(u"color: rgb(255,255,255);")
        self.labelName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.labelName)

        self.diseaseNameLabel = QLabel(self.diseaseNamelFrame)
        self.diseaseNameLabel.setObjectName(u"diseaseNameLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.diseaseNameLabel.sizePolicy().hasHeightForWidth())
        self.diseaseNameLabel.setSizePolicy(sizePolicy2)
        self.diseaseNameLabel.setMinimumSize(QSize(40, 20))
        self.diseaseNameLabel.setMaximumSize(QSize(165, 20))
        self.diseaseNameLabel.setFont(font1)
        self.diseaseNameLabel.setStyleSheet(u"color: rgb(255,255,255);")
        self.diseaseNameLabel.setAlignment(Qt.AlignCenter)
        self.diseaseNameLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.diseaseNameLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.diseaseNamelFrame)

        self.confidenceFrame = QFrame(self.dataViewGridlayout)
        self.confidenceFrame.setObjectName(u"confidenceFrame")
        sizePolicy.setHeightForWidth(self.confidenceFrame.sizePolicy().hasHeightForWidth())
        self.confidenceFrame.setSizePolicy(sizePolicy)
        self.confidenceFrame.setMinimumSize(QSize(400, 50))
        self.confidenceFrame.setMaximumSize(QSize(400, 50))
        self.confidenceFrame.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.horizontalLayout_3 = QHBoxLayout(self.confidenceFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.confidenceLabel = QLabel(self.confidenceFrame)
        self.confidenceLabel.setObjectName(u"confidenceLabel")
        self.confidenceLabel.setFont(font1)
        self.confidenceLabel.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.confidenceLabel)

        self.confidenceProgressBar = QProgressBar(self.confidenceFrame)
        self.confidenceProgressBar.setObjectName(u"confidenceProgressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.confidenceProgressBar.sizePolicy().hasHeightForWidth())
        self.confidenceProgressBar.setSizePolicy(sizePolicy3)
        self.confidenceProgressBar.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Product Sans Medium")
        self.confidenceProgressBar.setFont(font2)
        self.confidenceProgressBar.setStyleSheet(u"border: 2px solid rgb(126,153,120);\n"
"color: rgb(255,255,255);")
        self.confidenceProgressBar.setValue(0)
        self.confidenceProgressBar.setAlignment(Qt.AlignCenter)
        self.confidenceProgressBar.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.confidenceProgressBar)


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.confidenceFrame)

        self.DescriptionFrame = QFrame(self.dataViewGridlayout)
        self.DescriptionFrame.setObjectName(u"DescriptionFrame")
        sizePolicy.setHeightForWidth(self.DescriptionFrame.sizePolicy().hasHeightForWidth())
        self.DescriptionFrame.setSizePolicy(sizePolicy)
        self.DescriptionFrame.setMinimumSize(QSize(400, 255))
        self.DescriptionFrame.setMaximumSize(QSize(400, 255))
        self.DescriptionFrame.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.verticalLayout_3 = QVBoxLayout(self.DescriptionFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.descriptionLabel = QLabel(self.DescriptionFrame)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setMinimumSize(QSize(380, 150))
        self.descriptionLabel.setMaximumSize(QSize(380, 150))
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setStyleSheet(u"border: 2px solid rgb(126,153,120);\n"
"color: rgb(255,255,255);\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"")
        self.descriptionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.descriptionLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.descriptionLabel)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.confidenceFrame_2 = QFrame(self.DescriptionFrame)
        self.confidenceFrame_2.setObjectName(u"confidenceFrame_2")
        sizePolicy.setHeightForWidth(self.confidenceFrame_2.sizePolicy().hasHeightForWidth())
        self.confidenceFrame_2.setSizePolicy(sizePolicy)
        self.confidenceFrame_2.setMinimumSize(QSize(380, 75))
        self.confidenceFrame_2.setMaximumSize(QSize(380, 75))
        self.confidenceFrame_2.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.horizontalLayout_4 = QHBoxLayout(self.confidenceFrame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.detailsBtn = QPushButton(self.confidenceFrame_2)
        self.detailsBtn.setObjectName(u"detailsBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.detailsBtn.sizePolicy().hasHeightForWidth())
        self.detailsBtn.setSizePolicy(sizePolicy4)
        self.detailsBtn.setMinimumSize(QSize(175, 0))
        self.detailsBtn.setStyleSheet(u"QPushButton { color: rgb(255, 255, 255);\n"
"background-color: rgb(128,152,121);\n"
"font: 12pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 8px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed { background-color: rgb(128,152,121); }\n"
"QPushButton:hover { border-color: rgb(182,191,121);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/003-vision.png", QSize(), QIcon.Normal, QIcon.Off)
        self.detailsBtn.setIcon(icon3)
        self.detailsBtn.setIconSize(QSize(20, 20))
        self.detailsBtn.setFlat(False)

        self.horizontalLayout_4.addWidget(self.detailsBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.cureBtn = QPushButton(self.confidenceFrame_2)
        self.cureBtn.setObjectName(u"cureBtn")
        sizePolicy4.setHeightForWidth(self.cureBtn.sizePolicy().hasHeightForWidth())
        self.cureBtn.setSizePolicy(sizePolicy4)
        self.cureBtn.setMinimumSize(QSize(175, 0))
        self.cureBtn.setStyleSheet(u"QPushButton { color: rgb(255, 255, 255);\n"
"background-color: rgb(128,152,121);\n"
"font: 12pt \"Product Sans Medium\";\n"
"border: 4px solid rgb(85,101,85);\n"
"border-radius: 8px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:pressed { background-color: rgb(128,152,121); }\n"
"QPushButton:hover { border-color: rgb(182,191,121);\n"
"color: rgb(0,0,0);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/004-natural-product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cureBtn.setIcon(icon4)
        self.cureBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.cureBtn)


        self.verticalLayout_3.addWidget(self.confidenceFrame_2)


        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.DescriptionFrame)


        self.horizontalLayout.addWidget(self.dataViewGridlayout)


        self.verticalLayout.addWidget(self.contentlFrame, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Spinach Disease Classifier", None))
        self.headingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Spinach Disease Classifier</p></body></html>", None))
        self.selectedImageLabel.setText("")
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse for Picture", None))
        self.predictBtn.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Disease/State:", None))
        self.diseaseNameLabel.setText(QCoreApplication.translate("MainWindow", u"Unidentified", None))
        self.confidenceLabel.setText(QCoreApplication.translate("MainWindow", u"Confidence:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Unidentified", None))
        self.detailsBtn.setText(QCoreApplication.translate("MainWindow", u"See More ", None))
        self.cureBtn.setText(QCoreApplication.translate("MainWindow", u"Cure", None))
    # retranslateUi

