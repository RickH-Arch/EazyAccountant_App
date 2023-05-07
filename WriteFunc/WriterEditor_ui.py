# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WriterEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_WriterEditor(object):
    def setupUi(self, WriterEditor):
        if not WriterEditor.objectName():
            WriterEditor.setObjectName(u"WriterEditor")
        WriterEditor.resize(688, 916)
        self.writerEditor_mainWindow = QWidget(WriterEditor)
        self.writerEditor_mainWindow.setObjectName(u"writerEditor_mainWindow")
        self.writerEditor_mainWindow.setGeometry(QRect(80, 10, 500, 850))
        self.writerEditor_mainWindow.setMinimumSize(QSize(500, 850))
        self.writerEditor_mainWindow.setMaximumSize(QSize(500, 850))
        self.writerEditor_mainWindow.setStyleSheet(u"*{\n"
"background-color :rgb(243, 243, 243);\n"
"border-radius : 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.writerEditor_mainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.writerEditor_mainWindow)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 40))
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setStyleSheet(u"*{background-color:rgb(110, 92, 194);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;}")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.header)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(463, 7, 28, 28))
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
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 14, 91, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.header)

        self.mainContext = QFrame(self.writerEditor_mainWindow)
        self.mainContext.setObjectName(u"mainContext")
        self.mainContext.setFrameShape(QFrame.StyledPanel)
        self.mainContext.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainContext)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, -1, 15, -1)
        self.basicInfo = QFrame(self.mainContext)
        self.basicInfo.setObjectName(u"basicInfo")
        self.basicInfo.setMinimumSize(QSize(0, 166))
        self.basicInfo.setMaximumSize(QSize(16777215, 183))
        self.basicInfo.setAutoFillBackground(False)
        self.basicInfo.setFrameShape(QFrame.StyledPanel)
        self.basicInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.basicInfo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.basicInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 36))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_writerName = QLineEdit(self.frame)
        self.line_writerName.setObjectName(u"line_writerName")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.line_writerName.setFont(font1)

        self.horizontalLayout.addWidget(self.line_writerName)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.basicInfo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label_writerParent = QLabel(self.frame_2)
        self.label_writerParent.setObjectName(u"label_writerParent")
        self.label_writerParent.setFocusPolicy(Qt.ClickFocus)
        self.label_writerParent.setStyleSheet(u"color: rgb(156, 156, 156);")
        self.label_writerParent.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_writerParent)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.checkBox_writerAsRow = QCheckBox(self.frame_2)
        self.checkBox_writerAsRow.setObjectName(u"checkBox_writerAsRow")
        self.checkBox_writerAsRow.setMaximumSize(QSize(60, 16777215))
        self.checkBox_writerAsRow.setStyleSheet(u"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.checkBox_writerAsRow)

        self.checkBox_writerAsColumn = QCheckBox(self.frame_2)
        self.checkBox_writerAsColumn.setObjectName(u"checkBox_writerAsColumn")
        self.checkBox_writerAsColumn.setMaximumSize(QSize(60, 16777215))
        self.checkBox_writerAsColumn.setStyleSheet(u"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.checkBox_writerAsColumn)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.basicInfo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(240, 0))
        self.label_2.setMaximumSize(QSize(16777215, 14))
        self.label_2.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 14))
        self.label_3.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 3, 0, 0)
        self.list_Writer_wbName = QListWidget(self.frame_4)
        self.list_Writer_wbName.setObjectName(u"list_Writer_wbName")
        self.list_Writer_wbName.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121)}\n"
"\n"
"QScrollBar {              \n"
"            border: none;\n"
"            background:white;\n"
"            width:3px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line{\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(3"
                        "2, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")

        self.horizontalLayout_4.addWidget(self.list_Writer_wbName)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(25, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_addWbName = QPushButton(self.frame_6)
        self.btn_writer_addWbName.setObjectName(u"btn_writer_addWbName")
        self.btn_writer_addWbName.setMinimumSize(QSize(25, 25))
        self.btn_writer_addWbName.setMaximumSize(QSize(25, 25))
        self.btn_writer_addWbName.setStyleSheet(u"*{border-radius:5px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/\u52a0\u51cf\u7ec4\u4ef6\u52a0\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_writer_addWbName.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_writer_addWbName)

        self.btn_Writer_deleteWbName = QPushButton(self.frame_6)
        self.btn_Writer_deleteWbName.setObjectName(u"btn_Writer_deleteWbName")
        self.btn_Writer_deleteWbName.setMinimumSize(QSize(25, 25))
        self.btn_Writer_deleteWbName.setMaximumSize(QSize(25, 25))
        self.btn_Writer_deleteWbName.setStyleSheet(u"*{border-radius:5px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/\u51cf\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Writer_deleteWbName.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.btn_Writer_deleteWbName)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.list_writer_sheetName = QListWidget(self.frame_4)
        self.list_writer_sheetName.setObjectName(u"list_writer_sheetName")
        self.list_writer_sheetName.setMinimumSize(QSize(0, 0))
        self.list_writer_sheetName.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121)}\n"
"\n"
"QScrollBar {              \n"
"            border: none;\n"
"            background:white;\n"
"            width:3px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line{\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"            stop: 0  rgb(3"
                        "2, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")

        self.horizontalLayout_4.addWidget(self.list_writer_sheetName)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(25, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_addSheetName = QPushButton(self.frame_7)
        self.btn_writer_addSheetName.setObjectName(u"btn_writer_addSheetName")
        self.btn_writer_addSheetName.setMinimumSize(QSize(25, 25))
        self.btn_writer_addSheetName.setMaximumSize(QSize(25, 25))
        self.btn_writer_addSheetName.setStyleSheet(u"*{border-radius:5px;\n"
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
        self.btn_writer_addSheetName.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.btn_writer_addSheetName, 0, Qt.AlignRight)

        self.btn_writer_deleteSheetName = QPushButton(self.frame_7)
        self.btn_writer_deleteSheetName.setObjectName(u"btn_writer_deleteSheetName")
        self.btn_writer_deleteSheetName.setMinimumSize(QSize(25, 25))
        self.btn_writer_deleteSheetName.setMaximumSize(QSize(25, 25))
        self.btn_writer_deleteSheetName.setStyleSheet(u"*{border-radius:5px;\n"
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
        self.btn_writer_deleteSheetName.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.btn_writer_deleteSheetName, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.basicInfo)

        self.keyInfo = QFrame(self.mainContext)
        self.keyInfo.setObjectName(u"keyInfo")
        self.keyInfo.setMaximumSize(QSize(16777215, 180))
        self.keyInfo.setCursor(QCursor(Qt.ArrowCursor))
        self.keyInfo.setFrameShape(QFrame.StyledPanel)
        self.keyInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.keyInfo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 5, 0, 5)
        self.label_4 = QLabel(self.keyInfo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.verticalLayout_7.addWidget(self.label_4)

        self.scrollArea_writerKey = QScrollArea(self.keyInfo)
        self.scrollArea_writerKey.setObjectName(u"scrollArea_writerKey")
        self.scrollArea_writerKey.setMinimumSize(QSize(0, 120))
        self.scrollArea_writerKey.setMaximumSize(QSize(16777215, 120))
        self.scrollArea_writerKey.setStyleSheet(u"*{\n"
"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid lightgray;\n"
"color: rgb(121, 121, 121);\n"
"font-size:11px;}\n"
"\n"
"QScrollBar:vertical {              \n"
"        border:none;\n"
"        background:white;\n"
"\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"		color:rgb(110, 92, 194)\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:vertical:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-orig"
                        "in: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar:horizontal{\n"
" border: none;\n"
"	background:white;\n"
"	height:10px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:horizontal:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1"
                        " rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QWidget{\n"
" border:none;\n"
"}")
        self.scrollArea_writerKey.setWidgetResizable(True)
        self.keyRepo = QWidget()
        self.keyRepo.setObjectName(u"keyRepo")
        self.keyRepo.setGeometry(QRect(0, 0, 470, 106))
        self.keyRepo.setMaximumSize(QSize(16777215, 106))
        self.keyRepo.setStyleSheet(u"border-radius:10px")
        self.keyGrid = QHBoxLayout(self.keyRepo)
        self.keyGrid.setSpacing(10)
        self.keyGrid.setObjectName(u"keyGrid")
        self.keyGrid.setContentsMargins(10, 0, 10, 0)
        self.keyName1 = QWidget(self.keyRepo)
        self.keyName1.setObjectName(u"keyName1")
        self.keyName1.setMinimumSize(QSize(90, 90))
        self.keyName1.setMaximumSize(QSize(75, 75))
        self.keyName1.setStyleSheet(u"*{\n"
"background-color: rgb(237, 234, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.keyName1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.keyName1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border:none")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.btn_writer_deleteKey = QPushButton(self.frame_9)
        self.btn_writer_deleteKey.setObjectName(u"btn_writer_deleteKey")
        self.btn_writer_deleteKey.setGeometry(QRect(64, 4, 20, 20))
        self.btn_writer_deleteKey.setMinimumSize(QSize(20, 20))
        self.btn_writer_deleteKey.setMaximumSize(QSize(20, 20))
        self.btn_writer_deleteKey.setStyleSheet(u"*{background-color:rgb(231, 210, 255);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_writer_deleteKey.setIcon(icon)

        self.verticalLayout_8.addWidget(self.frame_9)

        self.line_keyName = QLineEdit(self.keyName1)
        self.line_keyName.setObjectName(u"line_keyName")
        self.line_keyName.setMinimumSize(QSize(0, 55))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.line_keyName.setFont(font2)
        self.line_keyName.setStyleSheet(u"border:None;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        self.line_keyName.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.line_keyName)


        self.keyGrid.addWidget(self.keyName1)

        self.writer_add_key = QWidget(self.keyRepo)
        self.writer_add_key.setObjectName(u"writer_add_key")
        self.writer_add_key.setMinimumSize(QSize(90, 90))
        self.writer_add_key.setMaximumSize(QSize(75, 75))
        self.writer_add_key.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.writer_add_key)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_addKey = QPushButton(self.writer_add_key)
        self.btn_writer_addKey.setObjectName(u"btn_writer_addKey")
        self.btn_writer_addKey.setMinimumSize(QSize(90, 90))
        self.btn_writer_addKey.setMaximumSize(QSize(90, 90))
        self.btn_writer_addKey.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_writer_addKey.setIcon(icon3)
        self.btn_writer_addKey.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.btn_writer_addKey)


        self.keyGrid.addWidget(self.writer_add_key)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.keyGrid.addItem(self.horizontalSpacer_3)

        self.scrollArea_writerKey.setWidget(self.keyRepo)

        self.verticalLayout_7.addWidget(self.scrollArea_writerKey)

        self.frame_8 = QFrame(self.keyInfo)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, -1, 0)
        self.checkbox_key_and = QCheckBox(self.frame_8)
        self.checkbox_key_and.setObjectName(u"checkbox_key_and")
        self.checkbox_key_and.setStyleSheet(u"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.checkbox_key_and)

        self.checkbox_key_or = QCheckBox(self.frame_8)
        self.checkbox_key_or.setObjectName(u"checkbox_key_or")
        self.checkbox_key_or.setStyleSheet(u"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.checkbox_key_or)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.keyInfo)

        self.valueInfo = QFrame(self.mainContext)
        self.valueInfo.setObjectName(u"valueInfo")
        self.valueInfo.setMinimumSize(QSize(0, 106))
        self.valueInfo.setMaximumSize(QSize(16777215, 153))
        self.valueInfo.setFrameShape(QFrame.StyledPanel)
        self.valueInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.valueInfo)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.valueInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 5))
        self.label_5.setMaximumSize(QSize(16777215, 18))
        self.label_5.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.verticalLayout_10.addWidget(self.label_5)

        self.scrollArea_writerValue = QScrollArea(self.valueInfo)
        self.scrollArea_writerValue.setObjectName(u"scrollArea_writerValue")
        self.scrollArea_writerValue.setMinimumSize(QSize(0, 120))
        self.scrollArea_writerValue.setMaximumSize(QSize(16777215, 120))
        self.scrollArea_writerValue.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121);\n"
"font-size:11px;}\n"
"\n"
"QScrollBar:vertical {              \n"
"        border:none;\n"
"        background:white;\n"
"\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"		color:rgb(110, 92, 194)\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:vertical:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
""
                        "    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar:horizontal{\n"
" border: none;\n"
"	background:white;\n"
"	height:10px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:horizontal:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130"
                        "));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QWidget{\n"
" border:none;\n"
"}")
        self.scrollArea_writerValue.setWidgetResizable(True)
        self.valueRepo = QWidget()
        self.valueRepo.setObjectName(u"valueRepo")
        self.valueRepo.setGeometry(QRect(0, 0, 470, 106))
        self.valueRepo.setMaximumSize(QSize(16777215, 106))
        self.valueGrid = QHBoxLayout(self.valueRepo)
        self.valueGrid.setSpacing(10)
        self.valueGrid.setObjectName(u"valueGrid")
        self.valueGrid.setContentsMargins(10, 0, 10, 0)
        self.ValueName1 = QWidget(self.valueRepo)
        self.ValueName1.setObjectName(u"ValueName1")
        self.ValueName1.setMinimumSize(QSize(90, 90))
        self.ValueName1.setMaximumSize(QSize(75, 75))
        self.ValueName1.setStyleSheet(u"*{\n"
"background-color: rgb(221, 194, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.verticalLayout_9 = QVBoxLayout(self.ValueName1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.ValueName1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:none")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.btn_writer_deleteValue = QPushButton(self.frame_10)
        self.btn_writer_deleteValue.setObjectName(u"btn_writer_deleteValue")
        self.btn_writer_deleteValue.setGeometry(QRect(64, 4, 20, 20))
        self.btn_writer_deleteValue.setMinimumSize(QSize(20, 20))
        self.btn_writer_deleteValue.setMaximumSize(QSize(20, 20))
        self.btn_writer_deleteValue.setStyleSheet(u"*{background-color:rgb(248, 248, 248);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_writer_deleteValue.setIcon(icon)

        self.verticalLayout_9.addWidget(self.frame_10)

        self.line_valueName = QLineEdit(self.ValueName1)
        self.line_valueName.setObjectName(u"line_valueName")
        self.line_valueName.setMinimumSize(QSize(85, 55))
        self.line_valueName.setMaximumSize(QSize(85, 16777215))
        self.line_valueName.setStyleSheet(u"border:None;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        self.line_valueName.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.line_valueName, 0, Qt.AlignHCenter)


        self.valueGrid.addWidget(self.ValueName1)

        self.writer_addvalue = QWidget(self.valueRepo)
        self.writer_addvalue.setObjectName(u"writer_addvalue")
        self.writer_addvalue.setMinimumSize(QSize(90, 90))
        self.writer_addvalue.setMaximumSize(QSize(75, 75))
        self.writer_addvalue.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.writer_addvalue)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_addValue = QPushButton(self.writer_addvalue)
        self.btn_writer_addValue.setObjectName(u"btn_writer_addValue")
        self.btn_writer_addValue.setMinimumSize(QSize(90, 90))
        self.btn_writer_addValue.setMaximumSize(QSize(90, 90))
        self.btn_writer_addValue.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        self.btn_writer_addValue.setIcon(icon3)
        self.btn_writer_addValue.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.btn_writer_addValue)


        self.valueGrid.addWidget(self.writer_addvalue)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.valueGrid.addItem(self.horizontalSpacer_5)

        self.scrollArea_writerValue.setWidget(self.valueRepo)

        self.verticalLayout_10.addWidget(self.scrollArea_writerValue)


        self.verticalLayout_2.addWidget(self.valueInfo)

        self.processInfo = QFrame(self.mainContext)
        self.processInfo.setObjectName(u"processInfo")
        self.processInfo.setFrameShape(QFrame.StyledPanel)
        self.processInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.processInfo)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.processInfo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 26))
        self.label_6.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.verticalLayout_12.addWidget(self.label_6)

        self.scrollArea_writerProcess = QScrollArea(self.processInfo)
        self.scrollArea_writerProcess.setObjectName(u"scrollArea_writerProcess")
        self.scrollArea_writerProcess.setMinimumSize(QSize(0, 205))
        self.scrollArea_writerProcess.setMaximumSize(QSize(16777215, 250))
        self.scrollArea_writerProcess.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121);\n"
"font-size:11px;}\n"
"\n"
"QScrollBar:vertical {              \n"
"        border:none;\n"
"        background:white;\n"
"\n"
"        width:10px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"		color:rgb(110, 92, 194)\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:vertical:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
""
                        "    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar:horizontal{\n"
" border: none;\n"
"	background:white;\n"
"	height:10px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"      background-color:rgb(232, 232, 232);\n"
"        min-height: 30px;\n"
"border-radius:5px;\n"
"    }\n"
"QScrollBar::handle:horizontal:hover {\n"
"      background-color:rgb(227, 227, 235);\n"
"        \n"
"    }\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"      background-color:rgb(110, 92, 194);\n"
"        \n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130"
                        "));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QWidget{\n"
" border:none;\n"
"}")
        self.scrollArea_writerProcess.setWidgetResizable(True)
        self.processRepo = QWidget()
        self.processRepo.setObjectName(u"processRepo")
        self.processRepo.setGeometry(QRect(0, 0, 470, 242))
        self.processRepo.setMaximumSize(QSize(16777215, 242))
        self.processGrid = QHBoxLayout(self.processRepo)
        self.processGrid.setSpacing(10)
        self.processGrid.setObjectName(u"processGrid")
        self.processGrid.setContentsMargins(10, 0, 10, 0)
        self.process1 = QWidget(self.processRepo)
        self.process1.setObjectName(u"process1")
        self.process1.setMinimumSize(QSize(150, 210))
        self.process1.setMaximumSize(QSize(110, 210))
        self.process1.setStyleSheet(u"*{\n"
"background-color:rgb(110, 92, 194);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.process1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.frame_11 = QFrame(self.process1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setStyleSheet(u"border:none")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 10))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_7, 0, Qt.AlignBottom)

        self.btn_writer_deleteProcess = QPushButton(self.frame_11)
        self.btn_writer_deleteProcess.setObjectName(u"btn_writer_deleteProcess")
        self.btn_writer_deleteProcess.setMinimumSize(QSize(20, 20))
        self.btn_writer_deleteProcess.setMaximumSize(QSize(20, 20))
        self.btn_writer_deleteProcess.setStyleSheet(u"*{background-color:rgb(158, 132, 235);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_writer_deleteProcess.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_writer_deleteProcess, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.line_processName = QLineEdit(self.process1)
        self.line_processName.setObjectName(u"line_processName")
        self.line_processName.setMinimumSize(QSize(0, 31))
        self.line_processName.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        self.line_processName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.line_processName)

        self.checkBox_writer_rewrite = QCheckBox(self.process1)
        self.checkBox_writer_rewrite.setObjectName(u"checkBox_writer_rewrite")
        self.checkBox_writer_rewrite.setMinimumSize(QSize(0, 24))
        self.checkBox_writer_rewrite.setStyleSheet(u"QCheckBox{\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")

        self.verticalLayout_11.addWidget(self.checkBox_writer_rewrite, 0, Qt.AlignHCenter)

        self.text_writer_process = QTextEdit(self.process1)
        self.text_writer_process.setObjectName(u"text_writer_process")
        self.text_writer_process.setMinimumSize(QSize(0, 110))
        self.text_writer_process.setMaximumSize(QSize(16777215, 112))
        self.text_writer_process.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 9pt \"Microsoft YaHei UI\";")

        self.verticalLayout_11.addWidget(self.text_writer_process)


        self.processGrid.addWidget(self.process1)

        self.writer_addProcess = QWidget(self.processRepo)
        self.writer_addProcess.setObjectName(u"writer_addProcess")
        self.writer_addProcess.setMinimumSize(QSize(150, 210))
        self.writer_addProcess.setMaximumSize(QSize(150, 210))
        self.writer_addProcess.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.writer_addProcess)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_addProcess = QPushButton(self.writer_addProcess)
        self.btn_writer_addProcess.setObjectName(u"btn_writer_addProcess")
        self.btn_writer_addProcess.setMinimumSize(QSize(150, 210))
        self.btn_writer_addProcess.setMaximumSize(QSize(150, 210))
        self.btn_writer_addProcess.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        self.btn_writer_addProcess.setIcon(icon3)
        self.btn_writer_addProcess.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.btn_writer_addProcess)


        self.processGrid.addWidget(self.writer_addProcess)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.processGrid.addItem(self.horizontalSpacer_6)

        self.scrollArea_writerProcess.setWidget(self.processRepo)

        self.verticalLayout_12.addWidget(self.scrollArea_writerProcess)


        self.verticalLayout_2.addWidget(self.processInfo)


        self.verticalLayout.addWidget(self.mainContext)


        self.retranslateUi(WriterEditor)

        QMetaObject.connectSlotsByName(WriterEditor)
    # setupUi

    def retranslateUi(self, WriterEditor):
        WriterEditor.setWindowTitle(QCoreApplication.translate("WriterEditor", u"Form", None))
        self.btn_close.setText("")
        self.label.setText(QCoreApplication.translate("WriterEditor", u"Writer Editor", None))
        self.label_writerParent.setText(QCoreApplication.translate("WriterEditor", u"parent", None))
        self.checkBox_writerAsRow.setText(QCoreApplication.translate("WriterEditor", u"\u884c\u5199\u5165", None))
        self.checkBox_writerAsColumn.setText(QCoreApplication.translate("WriterEditor", u"\u5217\u5199\u5165", None))
        self.label_2.setText(QCoreApplication.translate("WriterEditor", u"\u4f5c\u7528\u4e8e\u5de5\u4f5c\u7c3f\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("WriterEditor", u"\u4f5c\u7528\u4e8e\u5de5\u4f5c\u8868\u540d\u79f0\uff08\u9009\u586b\uff09", None))
        self.btn_writer_addWbName.setText("")
        self.btn_Writer_deleteWbName.setText("")
#if QT_CONFIG(whatsthis)
        self.btn_writer_addSheetName.setWhatsThis(QCoreApplication.translate("WriterEditor", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_writer_addSheetName.setText("")
        self.btn_writer_deleteSheetName.setText("")
        self.label_4.setText(QCoreApplication.translate("WriterEditor", u"\u68c0\u7d22\u53d8\u91cf\u540d\u79f0", None))
        self.btn_writer_deleteKey.setText("")
        self.checkbox_key_and.setText(QCoreApplication.translate("WriterEditor", u"\u4e0e", None))
        self.checkbox_key_or.setText(QCoreApplication.translate("WriterEditor", u"\u6216", None))
        self.label_5.setText(QCoreApplication.translate("WriterEditor", u"\u5199\u5165\u53d8\u91cf\u540d\u79f0", None))
        self.btn_writer_deleteValue.setText("")
        self.line_valueName.setText(QCoreApplication.translate("WriterEditor", u"dsad", None))
        self.label_6.setText(QCoreApplication.translate("WriterEditor", u"\u64cd\u4f5c", None))
        self.label_7.setText(QCoreApplication.translate("WriterEditor", u"\u76ee\u6807\u5355\u5143\u683c\u540d\u79f0\uff1a", None))
        self.btn_writer_deleteProcess.setText("")
        self.checkBox_writer_rewrite.setText(QCoreApplication.translate("WriterEditor", u"\u8986\u76d6", None))
    # retranslateUi

