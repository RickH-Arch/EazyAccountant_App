# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Processer.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_Processer(object):
    def setupUi(self, Processer):
        if not Processer.objectName():
            Processer.setObjectName(u"Processer")
        Processer.resize(424, 421)
        self.horizontalLayout = QHBoxLayout(Processer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Processer_mainWindow = QFrame(Processer)
        self.Processer_mainWindow.setObjectName(u"Processer_mainWindow")
        self.Processer_mainWindow.setMinimumSize(QSize(400, 0))
        self.Processer_mainWindow.setMaximumSize(QSize(400, 16777215))
        self.Processer_mainWindow.setFrameShape(QFrame.StyledPanel)
        self.Processer_mainWindow.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Processer_mainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.Processer_mainWindow)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setStyleSheet(u"*{background-color:rgb(110, 92, 194);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label)

        self.btn_close = QPushButton(self.header)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(110, 92, 194);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(94, 80, 168);\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color:rgb(84, 71, 148);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.btn_close, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header)

        self.main_context = QFrame(self.Processer_mainWindow)
        self.main_context.setObjectName(u"main_context")
        self.main_context.setMaximumSize(QSize(16777215, 16777215))
        self.main_context.setStyleSheet(u"background-color:rgb(243, 243, 243);")
        self.main_context.setFrameShape(QFrame.StyledPanel)
        self.main_context.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_context)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.keyHeader = QFrame(self.main_context)
        self.keyHeader.setObjectName(u"keyHeader")
        self.keyHeader.setMinimumSize(QSize(0, 0))
        self.keyHeader.setMaximumSize(QSize(10000, 35))
        self.keyHeader.setFrameShape(QFrame.StyledPanel)
        self.keyHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.keyHeader)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.keyHeader)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.keyHeader)

        self.key_frame = QFrame(self.main_context)
        self.key_frame.setObjectName(u"key_frame")
        self.key_frame.setFrameShape(QFrame.StyledPanel)
        self.key_frame.setFrameShadow(QFrame.Raised)
        self.key_grid = QVBoxLayout(self.key_frame)
        self.key_grid.setSpacing(0)
        self.key_grid.setObjectName(u"key_grid")
        self.key_grid.setContentsMargins(0, 0, 0, -1)
        self.key1 = QFrame(self.key_frame)
        self.key1.setObjectName(u"key1")
        self.key1.setMaximumSize(QSize(16777215, 50))
        self.key1.setFrameShape(QFrame.StyledPanel)
        self.key1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.key1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.label_4 = QLabel(self.key1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.key1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(295, 31))
        self.lineEdit.setMaximumSize(QSize(295, 16777215))
        self.lineEdit.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121)}")

        self.horizontalLayout_5.addWidget(self.lineEdit, 0, Qt.AlignRight)


        self.key_grid.addWidget(self.key1)

        self.key2 = QFrame(self.key_frame)
        self.key2.setObjectName(u"key2")
        self.key2.setMaximumSize(QSize(16777215, 50))
        self.key2.setFrameShape(QFrame.StyledPanel)
        self.key2.setFrameShadow(QFrame.Raised)

        self.key_grid.addWidget(self.key2)


        self.verticalLayout_2.addWidget(self.key_frame)

        self.valueHeader = QFrame(self.main_context)
        self.valueHeader.setObjectName(u"valueHeader")
        self.valueHeader.setMaximumSize(QSize(16777215, 35))
        self.valueHeader.setFrameShape(QFrame.StyledPanel)
        self.valueHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.valueHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.valueHeader)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.valueHeader)

        self.value_frame = QFrame(self.main_context)
        self.value_frame.setObjectName(u"value_frame")
        self.value_frame.setFrameShape(QFrame.StyledPanel)
        self.value_frame.setFrameShadow(QFrame.Raised)
        self.value_grid = QVBoxLayout(self.value_frame)
        self.value_grid.setSpacing(0)
        self.value_grid.setObjectName(u"value_grid")
        self.value_grid.setContentsMargins(0, 0, 0, 0)
        self.key1_2 = QFrame(self.value_frame)
        self.key1_2.setObjectName(u"key1_2")
        self.key1_2.setMaximumSize(QSize(16777215, 50))
        self.key1_2.setFrameShape(QFrame.StyledPanel)
        self.key1_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.key1_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.label_5 = QLabel(self.key1_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(self.key1_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 31))
        self.lineEdit_2.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121)}")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.value_grid.addWidget(self.key1_2)


        self.verticalLayout_2.addWidget(self.value_frame)


        self.verticalLayout.addWidget(self.main_context)

        self.buttons = QFrame(self.Processer_mainWindow)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMaximumSize(QSize(16777215, 40))
        self.buttons.setStyleSheet(u"*{background-color:rgb(243, 243, 243);\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;}")
        self.buttons.setFrameShape(QFrame.StyledPanel)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.buttons)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.buttons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 25))
        self.pushButton.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(81, 66, 147) ;\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.buttons)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 25))
        self.pushButton_2.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(217, 217, 217) ;\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.buttons)


        self.horizontalLayout.addWidget(self.Processer_mainWindow)


        self.retranslateUi(Processer)

        QMetaObject.connectSlotsByName(Processer)
    # setupUi

    def retranslateUi(self, Processer):
        Processer.setWindowTitle(QCoreApplication.translate("Processer", u"Form", None))
        self.label.setText(QCoreApplication.translate("Processer", u"Processer", None))
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("Processer", u"\u68c0\u7d22\u53d8\u91cf\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Processer", u"key1\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Processer", u"\u5199\u5165\u53d8\u91cf\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Processer", u"value1\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Processer", u"\u8fd0\u884c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Processer", u"\u5173\u95ed", None))
    # retranslateUi

