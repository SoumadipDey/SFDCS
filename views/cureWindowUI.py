# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cureWindowKvGPuX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .resources_rc import *

class Ui_cureWindow(object):
    def setupUi(self, cureWindow):
        if not cureWindow.objectName():
            cureWindow.setObjectName(u"cureWindow")
        cureWindow.resize(550, 400)
        cureWindow.setFixedSize(550,400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(cureWindow.sizePolicy().hasHeightForWidth())
        cureWindow.setSizePolicy(sizePolicy)
        cureWindow.setMinimumSize(QSize(550, 400))
        cureWindow.setMaximumSize(QSize(550, 400))
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        cureWindow.setWindowIcon(icon)
        cureWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(cureWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticaBlFrame = QFrame(self.centralwidget)
        self.verticaBlFrame.setObjectName(u"verticaBlFrame")
        self.verticaBlFrame.setGeometry(QRect(0, 0, 550, 400))
        sizePolicy.setHeightForWidth(self.verticaBlFrame.sizePolicy().hasHeightForWidth())
        self.verticaBlFrame.setSizePolicy(sizePolicy)
        self.verticaBlFrame.setMinimumSize(QSize(550, 400))
        self.verticaBlFrame.setMaximumSize(QSize(550, 400))
        font = QFont()
        font.setFamily(u"Product Sans Medium")
        self.verticaBlFrame.setFont(font)
        self.verticaBlFrame.setStyleSheet(u"background-color: rgb(205,214,219);\n"
"border: 1px solid rgb(205,214,219);")
        self.verticalLayout = QVBoxLayout(self.verticaBlFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.horizontalFrame = QFrame(self.verticaBlFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy1)
        self.horizontalFrame.setMinimumSize(QSize(550, 200))
        self.horizontalFrame.setMaximumSize(QSize(550, 200))
        self.horizontalFrame.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.cureImageLabel = QLabel(self.horizontalFrame)
        self.cureImageLabel.setObjectName(u"cureImageLabel")
        sizePolicy.setHeightForWidth(self.cureImageLabel.sizePolicy().hasHeightForWidth())
        self.cureImageLabel.setSizePolicy(sizePolicy)
        self.cureImageLabel.setMinimumSize(QSize(150, 150))
        self.cureImageLabel.setMaximumSize(QSize(150, 150))
        self.cureImageLabel.setStyleSheet(u"")
        self.cureImageLabel.setPixmap(QPixmap(u":/assets/assets/007-fertilize.png"))
        self.cureImageLabel.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.cureImageLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.productFrame = QFrame(self.horizontalFrame)
        self.productFrame.setObjectName(u"productFrame")
        self.productFrame.setMinimumSize(QSize(350, 180))
        self.productFrame.setMaximumSize(QSize(350, 180))
        self.productFrame.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.productFrame.setFrameShape(QFrame.StyledPanel)
        self.productFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.productFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pr_Label = QLabel(self.productFrame)
        self.pr_Label.setObjectName(u"pr_Label")
        self.pr_Label.setMinimumSize(QSize(330, 30))
        self.pr_Label.setMaximumSize(QSize(330, 30))
        font1 = QFont()
        font1.setFamily(u"Product Sans Medium")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.pr_Label.setFont(font1)
        self.pr_Label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.pr_Label)

        self.productList = QListWidget(self.productFrame)
        self.productList.setObjectName(u"productList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.productList.sizePolicy().hasHeightForWidth())
        self.productList.setSizePolicy(sizePolicy2)
        self.productList.setMinimumSize(QSize(330, 120))
        self.productList.setMaximumSize(QSize(330, 120))
        font2 = QFont()
        font2.setFamily(u"Product Sans Medium")
        font2.setPointSize(12)
        self.productList.setFont(font2)
        self.productList.setStyleSheet(u"QListWidgetItem {\n"
"	margin-top: 10px;\n"
"	background-color:  rgb(126,153,120);\n"
"	border: 2px solid rgb(126,153,120);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QListWidget {\n"
"	border: 2px solid rgb(126,153,120);\n"
"	background-color:  rgb(126,153,120);\n"
"	color: rgb(255,255,255);\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.productList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.productList)


        self.horizontalLayout_7.addWidget(self.productFrame)


        self.verticalLayout.addWidget(self.horizontalFrame)

        self.horizontalFrame_2 = QFrame(self.verticaBlFrame)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy1)
        self.horizontalFrame_2.setMinimumSize(QSize(550, 200))
        self.horizontalFrame_2.setMaximumSize(QSize(550, 200))
        self.horizontalFrame_2.setStyleSheet(u"border-radius: 6px;")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 5)
        self.frame = QFrame(self.horizontalFrame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(530, 180))
        self.frame.setMaximumSize(QSize(530, 180))
        font3 = QFont()
        font3.setPointSize(9)
        self.frame.setFont(font3)
        self.frame.setStyleSheet(u"background-color: rgb(85,101,85);\n"
"border: 1px solid  rgb(85,101,85);\n"
"border-radius: 6px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.remedyHeaderLabel = QLabel(self.frame)
        self.remedyHeaderLabel.setObjectName(u"remedyHeaderLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.remedyHeaderLabel.sizePolicy().hasHeightForWidth())
        self.remedyHeaderLabel.setSizePolicy(sizePolicy3)
        self.remedyHeaderLabel.setMinimumSize(QSize(510, 30))
        self.remedyHeaderLabel.setMaximumSize(QSize(510, 30))
        self.remedyHeaderLabel.setFont(font1)
        self.remedyHeaderLabel.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.remedyHeaderLabel)

        self.remedyDetailsLabel = QLabel(self.frame)
        self.remedyDetailsLabel.setObjectName(u"remedyDetailsLabel")
        self.remedyDetailsLabel.setMinimumSize(QSize(510, 125))
        self.remedyDetailsLabel.setMaximumSize(QSize(510, 125))
        font4 = QFont()
        font4.setFamily(u"Product Sans Medium")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        font4.setKerning(True)
        self.remedyDetailsLabel.setFont(font4)
#if QT_CONFIG(tooltip)
        self.remedyDetailsLabel.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.remedyDetailsLabel.setStyleSheet(u"border: 2px solid rgb(126,153,120);\n"
"color: rgb(255,255,255);\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"")
        self.remedyDetailsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.remedyDetailsLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.remedyDetailsLabel)


        self.horizontalLayout_9.addWidget(self.frame)


        self.verticalLayout.addWidget(self.horizontalFrame_2)

        cureWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(cureWindow)

        QMetaObject.connectSlotsByName(cureWindow)
    # setupUi

    def retranslateUi(self, cureWindow):
        cureWindow.setWindowTitle(QCoreApplication.translate("cureWindow", u"Details", None))
        self.cureImageLabel.setText("")
        self.pr_Label.setText(QCoreApplication.translate("cureWindow", u"Products and Links:", None))
        self.remedyHeaderLabel.setText(QCoreApplication.translate("cureWindow", u"Remedy for <DiseaseName>:", None))
        self.remedyDetailsLabel.setText(QCoreApplication.translate("cureWindow", u"NULL", None))
    # retranslateUi

