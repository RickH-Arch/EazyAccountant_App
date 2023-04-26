# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EasyAccountantApp_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 500)
        MainWindow.setMinimumSize(QSize(820, 500))
        MainWindow.setMaximumSize(QSize(820, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 50))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color:rgb(81,68,140);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 50))
        self.left_menu_toggle.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background:rgb(125, 108, 202);\n"
"}")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.left_menu_toggle)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(40, 35))
        self.menuButton.setMaximumSize(QSize(50, 35))
        self.menuButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icon/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.menuButton)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.title_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 17, 54, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.title_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(47, 19, 81, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.title_bar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(119, 17, 54, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.title_bar)


        self.horizontalLayout_2.addWidget(self.title_bar_container)

        self.top_right_buttons = QFrame(self.main_header)
        self.top_right_buttons.setObjectName(u"top_right_buttons")
        self.top_right_buttons.setMinimumSize(QSize(80, 0))
        self.top_right_buttons.setMaximumSize(QSize(200, 16777215))
        self.top_right_buttons.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background:rgb(125, 108, 202);\n"
"}")
        self.top_right_buttons.setFrameShape(QFrame.StyledPanel)
        self.top_right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_buttons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_buttons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(30, 30))
        self.minimizeButton.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/\u7a97\u53e3\u6700\u5c0f\u5316line.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.closeButton = QPushButton(self.top_right_buttons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(30, 30))
        self.closeButton.setMaximumSize(QSize(30, 30))
        self.closeButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.top_right_buttons, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(52, 74, 108,0);\n"
"\n"
"")
        self.main_body.setFrameShape(QFrame.NoFrame)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(50, 0))
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setStyleSheet(u"*{background-color: rgb(110, 92, 194);\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border:none;\n"
"	border-left: 1px solid transparent;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(110, 92, 194);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:rgb(125, 108, 202);\n"
"}")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top = QFrame(self.left_side_menu)
        self.left_menu_top.setObjectName(u"left_menu_top")
        self.left_menu_top.setFrameShape(QFrame.StyledPanel)
        self.left_menu_top.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.left_menu_top)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_extract = QPushButton(self.left_menu_top)
        self.btn_menu_extract.setObjectName(u"btn_menu_extract")
        self.btn_menu_extract.setMinimumSize(QSize(80, 0))
        self.btn_menu_extract.setStyleSheet(u"background-image: url(:/png/icon/png/\u83b7\u53d6\u4fe1\u606f.png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"font-size: 12px;")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.btn_menu_extract)

        self.btn_menu_write = QPushButton(self.left_menu_top)
        self.btn_menu_write.setObjectName(u"btn_menu_write")
        self.btn_menu_write.setMinimumSize(QSize(80, 40))
        self.btn_menu_write.setStyleSheet(u"background-image: url(:/png/icon/png/\u5408\u540c7 (2).png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"font-size: 12px;")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.btn_menu_write)

        self.btn_menu_transfer = QPushButton(self.left_menu_top)
        self.btn_menu_transfer.setObjectName(u"btn_menu_transfer")
        self.btn_menu_transfer.setMinimumSize(QSize(80, 40))
        self.btn_menu_transfer.setStyleSheet(u"background-image: url(:/png/icon/png/\u8f6c\u6362.png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"font-size: 12px;")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.btn_menu_transfer)

        self.btn_menu_check = QPushButton(self.left_menu_top)
        self.btn_menu_check.setObjectName(u"btn_menu_check")
        self.btn_menu_check.setMinimumSize(QSize(80, 40))
        self.btn_menu_check.setStyleSheet(u"background-image: url(:/png/icon/png/\u6838\u5bf9.png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"font-size: 12px;")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.btn_menu_check)


        self.verticalLayout_2.addWidget(self.left_menu_top)

        self.btn_menu_setting = QPushButton(self.left_side_menu)
        self.btn_menu_setting.setObjectName(u"btn_menu_setting")
        self.btn_menu_setting.setMinimumSize(QSize(80, 0))
        self.btn_menu_setting.setStyleSheet(u"background-image: url(:/png/icon/png/\u8bbe\u7f6e.png);\n"
"background-repeat: none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"font-size: 12px;")

        self.verticalLayout_2.addWidget(self.btn_menu_setting)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.center_main_items.setFrameShape(QFrame.NoFrame)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_write = QWidget()
        self.page_write.setObjectName(u"page_write")
        self.page_write.setStyleSheet(u"")
        self.write_frame = QFrame(self.page_write)
        self.write_frame.setObjectName(u"write_frame")
        self.write_frame.setGeometry(QRect(0, 7, 510, 430))
        self.write_frame.setMinimumSize(QSize(0, 0))
        self.write_frame.setMaximumSize(QSize(510, 430))
        self.write_frame.setFrameShape(QFrame.StyledPanel)
        self.write_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.write_frame)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.write_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 86))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(34, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 13))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.verticalLayout_9.addWidget(self.label_4)

        self.list_write_folderPath = QListWidget(self.frame_5)
        self.list_write_folderPath.setObjectName(u"list_write_folderPath")
        self.list_write_folderPath.setMinimumSize(QSize(0, 54))
        self.list_write_folderPath.setMaximumSize(QSize(290, 44))
        self.list_write_folderPath.setStyleSheet(u"*{border-radius:10px;\n"
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

        self.verticalLayout_9.addWidget(self.list_write_folderPath)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(100, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.btn_write_readFolder = QPushButton(self.frame_2)
        self.btn_write_readFolder.setObjectName(u"btn_write_readFolder")
        self.btn_write_readFolder.setMinimumSize(QSize(80, 30))
        self.btn_write_readFolder.setMaximumSize(QSize(80, 30))
        self.btn_write_readFolder.setStyleSheet(u"*{border-radius:5px;\n"
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

        self.verticalLayout_5.addWidget(self.btn_write_readFolder, 0, Qt.AlignBottom)

        self.btn_write_deleteFolder = QPushButton(self.frame_2)
        self.btn_write_deleteFolder.setObjectName(u"btn_write_deleteFolder")
        self.btn_write_deleteFolder.setMinimumSize(QSize(80, 20))
        self.btn_write_deleteFolder.setMaximumSize(QSize(80, 16777215))
        self.btn_write_deleteFolder.setStyleSheet(u"*{border-radius:5px;\n"
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

        self.verticalLayout_5.addWidget(self.btn_write_deleteFolder)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.horizontalSpacer_3 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addWidget(self.frame)

        self.line = QFrame(self.write_frame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(500, 2))
        font2 = QFont()
        font2.setBold(False)
        self.line.setFont(font2)
        self.line.setStyleSheet(u"color:rgb(220, 220, 220)")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_6.addWidget(self.line)

        self.writer_editGroup = QFrame(self.write_frame)
        self.writer_editGroup.setObjectName(u"writer_editGroup")
        self.writer_editGroup.setMinimumSize(QSize(0, 40))
        self.writer_editGroup.setMaximumSize(QSize(16777215, 40))
        self.writer_editGroup.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(81, 66, 147) ;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")
        self.writer_editGroup.setFrameShape(QFrame.StyledPanel)
        self.writer_editGroup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.writer_editGroup)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBox_selectWriterGroup = QComboBox(self.writer_editGroup)
        self.comboBox_selectWriterGroup.addItem("")
        self.comboBox_selectWriterGroup.addItem("")
        self.comboBox_selectWriterGroup.setObjectName(u"comboBox_selectWriterGroup")
        self.comboBox_selectWriterGroup.setMinimumSize(QSize(180, 0))
        self.comboBox_selectWriterGroup.setMaximumSize(QSize(100, 32))
        self.comboBox_selectWriterGroup.setFont(font2)
        self.comboBox_selectWriterGroup.setStyleSheet(u"QComboBox{\n"
"border: 1px solid rgb(232, 232, 232);\n"
"    \n"
"    padding: 1px px 1px 10px; \n"
"     \n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px 10px 0px 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border:none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {image: url(:/png/icon/png/xiala.png);height:10px;width:20px;}\n"
"\n"
"\n"
"  QComboBox QAbstractItemView{\n"
"	background:rgba(255,255,255,1);\n"
"    border:1px solid rgba(228,228,228,1);\n"
"    border-radius:10px;\n"
"	font-size:14px;\n"
"    outline: 0px; \n"
"  }\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"	height:36px;\n"
"	color:#666666;\n"
"	padding-left:9px;\n"
"	background-color:#FFFFFF;\n"
"}\n"
"QComboBox QAbstractItemView::item:hover{ \n"
"  background-color:rgb(227, 227, 235);\n"
"  color:#ffffff;\n"
"}\n"
"QComboBox QAbstractItemView::item:selected{\n"
"  background-color:rgb(138, 116, 245);\n"
"  color:#ffffff;\n"
"}")
        self.comboBox_selectWriterGroup.setEditable(False)
        self.comboBox_selectWriterGroup.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.comboBox_selectWriterGroup)

        self.btn_renameWriterGroup = QPushButton(self.writer_editGroup)
        self.btn_renameWriterGroup.setObjectName(u"btn_renameWriterGroup")
        self.btn_renameWriterGroup.setMinimumSize(QSize(58, 30))
        self.btn_renameWriterGroup.setStyleSheet(u"*{border-radius:5px;\n"
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

        self.horizontalLayout_6.addWidget(self.btn_renameWriterGroup)

        self.btn_addWriterGroup = QPushButton(self.writer_editGroup)
        self.btn_addWriterGroup.setObjectName(u"btn_addWriterGroup")
        self.btn_addWriterGroup.setMinimumSize(QSize(80, 30))

        self.horizontalLayout_6.addWidget(self.btn_addWriterGroup)

        self.btn_deleteWriterGroup = QPushButton(self.writer_editGroup)
        self.btn_deleteWriterGroup.setObjectName(u"btn_deleteWriterGroup")
        self.btn_deleteWriterGroup.setMinimumSize(QSize(40, 30))
        self.btn_deleteWriterGroup.setStyleSheet(u"*{border-radius:5px;\n"
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

        self.horizontalLayout_6.addWidget(self.btn_deleteWriterGroup)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.writer_editGroup)

        self.writer_ctrlMenu = QFrame(self.write_frame)
        self.writer_ctrlMenu.setObjectName(u"writer_ctrlMenu")
        self.writer_ctrlMenu.setMinimumSize(QSize(0, 29))
        self.writer_ctrlMenu.setMaximumSize(QSize(16777215, 30))
        self.writer_ctrlMenu.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.writer_ctrlMenu.setFrameShape(QFrame.StyledPanel)
        self.writer_ctrlMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.writer_ctrlMenu)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.writer_ctrlMenu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(127, 127, 127);")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.filter_input = QTextEdit(self.writer_ctrlMenu)
        self.filter_input.setObjectName(u"filter_input")
        self.filter_input.setMinimumSize(QSize(264, 0))
        self.filter_input.setMaximumSize(QSize(100, 26))
        self.filter_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1px solid rgb(232, 232, 232);\n"
"")

        self.horizontalLayout_7.addWidget(self.filter_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addWidget(self.writer_ctrlMenu)

        self.scrollArea = QScrollArea(self.write_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 350))
        self.scrollArea.setStyleSheet(u"*{\n"
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
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 490, 245))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(110, 110))
        self.widget_5.setMaximumSize(QSize(110, 110))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(110, 110))
        self.widget_6.setMaximumSize(QSize(110, 110))
        self.widget_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(110, 110))
        self.widget_7.setMaximumSize(QSize(110, 110))
        self.widget_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_7, 1, 1, 1, 1)

        self.writer0 = QWidget(self.scrollAreaWidgetContents)
        self.writer0.setObjectName(u"writer0")
        self.writer0.setMinimumSize(QSize(110, 110))
        self.writer0.setMaximumSize(QSize(110, 110))
        self.writer0.setStyleSheet(u"*{\n"
"background-color: rgb(249, 246, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(227, 216, 255);\n"
"border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.writer0)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.frame_4 = QFrame(self.writer0)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 26))
        self.frame_4.setStyleSheet(u"border:none")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(4, 0, 4, 0)
        self.btn_writer_edit = QPushButton(self.frame_4)
        self.btn_writer_edit.setObjectName(u"btn_writer_edit")
        self.btn_writer_edit.setMinimumSize(QSize(32, 20))
        self.btn_writer_edit.setMaximumSize(QSize(20, 16777215))
        self.btn_writer_edit.setStyleSheet(u"*{background-color:rgb(230, 230, 230);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_writer_edit, 0, Qt.AlignLeft)

        self.btn_writer_copy = QPushButton(self.frame_4)
        self.btn_writer_copy.setObjectName(u"btn_writer_copy")
        self.btn_writer_copy.setMinimumSize(QSize(20, 20))
        self.btn_writer_copy.setMaximumSize(QSize(20, 20))
        self.btn_writer_copy.setStyleSheet(u"*{background-color:rgb(230, 230, 230);\n"
"color:rgb(227, 216, 255);}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u590d\u5236.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_writer_copy.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.btn_writer_copy)

        self.btn_writer_delete = QPushButton(self.frame_4)
        self.btn_writer_delete.setObjectName(u"btn_writer_delete")
        self.btn_writer_delete.setMinimumSize(QSize(20, 20))
        self.btn_writer_delete.setMaximumSize(QSize(20, 20))
        self.btn_writer_delete.setStyleSheet(u"*{background-color:rgb(243, 165, 166);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_writer_delete.setIcon(icon2)

        self.horizontalLayout_10.addWidget(self.btn_writer_delete, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.btn_writer_name = QPushButton(self.writer0)
        self.btn_writer_name.setObjectName(u"btn_writer_name")
        self.btn_writer_name.setMinimumSize(QSize(0, 39))
        font3 = QFont()
        font3.setBold(True)
        self.btn_writer_name.setFont(font3)
        self.btn_writer_name.setStyleSheet(u"color:rgb(72, 72, 72);\n"
"background-color:rgb(249, 246, 255);\n"
"border:none;")

        self.verticalLayout_7.addWidget(self.btn_writer_name)

        self.frame_3 = QFrame(self.writer0)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 37))
        self.frame_3.setStyleSheet(u"border:none")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_batchOpr = QPushButton(self.frame_3)
        self.btn_writer_batchOpr.setObjectName(u"btn_writer_batchOpr")
        self.btn_writer_batchOpr.setMinimumSize(QSize(61, 29))
        self.btn_writer_batchOpr.setMaximumSize(QSize(30, 29))

        self.horizontalLayout_9.addWidget(self.btn_writer_batchOpr)

        self.btn_writer_opr = QPushButton(self.frame_3)
        self.btn_writer_opr.setObjectName(u"btn_writer_opr")
        self.btn_writer_opr.setMinimumSize(QSize(35, 29))
        self.btn_writer_opr.setMaximumSize(QSize(30, 29))

        self.horizontalLayout_9.addWidget(self.btn_writer_opr)


        self.verticalLayout_7.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.writer0, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(110, 110))
        self.widget_8.setMaximumSize(QSize(110, 110))
        self.widget_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_8, 1, 3, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(110, 110))
        self.widget_2.setMaximumSize(QSize(110, 110))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_2, 0, 3, 1, 1)

        self.frame_addWriter = QWidget(self.scrollAreaWidgetContents)
        self.frame_addWriter.setObjectName(u"frame_addWriter")
        self.frame_addWriter.setMinimumSize(QSize(110, 110))
        self.frame_addWriter.setMaximumSize(QSize(110, 110))
        self.frame_addWriter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.frame_addWriter)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_writer_add = QPushButton(self.frame_addWriter)
        self.btn_writer_add.setObjectName(u"btn_writer_add")
        self.btn_writer_add.setMinimumSize(QSize(110, 110))
        self.btn_writer_add.setStyleSheet(u"*:hover{\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_writer_add.setIcon(icon4)
        self.btn_writer_add.setIconSize(QSize(40, 40))

        self.verticalLayout_8.addWidget(self.btn_writer_add)


        self.gridLayout.addWidget(self.frame_addWriter, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(110, 110))
        self.widget_3.setMaximumSize(QSize(110, 110))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_write)
        self.page_check = QWidget()
        self.page_check.setObjectName(u"page_check")
        self.page_check.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_check)
        self.page_transfer = QWidget()
        self.page_transfer.setObjectName(u"page_transfer")
        self.page_transfer.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_transfer)
        self.page_extract = QWidget()
        self.page_extract.setObjectName(u"page_extract")
        self.page_extract.setStyleSheet(u"")
        self.folderPathLable = QLabel(self.page_extract)
        self.folderPathLable.setObjectName(u"folderPathLable")
        self.folderPathLable.setGeometry(QRect(30, 20, 91, 16))
        self.folderPathLable.setFont(font1)
        self.folderPathLable.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.btn_browseFolder = QPushButton(self.page_extract)
        self.btn_browseFolder.setObjectName(u"btn_browseFolder")
        self.btn_browseFolder.setGeometry(QRect(350, 40, 91, 41))
        self.btn_browseFolder.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")
        self.list_folderPath = QListWidget(self.page_extract)
        self.list_folderPath.setObjectName(u"list_folderPath")
        self.list_folderPath.setGeometry(QRect(30, 40, 311, 81))
        self.list_folderPath.setStyleSheet(u"*{border-radius:10px;\n"
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
        self.btn_deletFolder = QPushButton(self.page_extract)
        self.btn_deletFolder.setObjectName(u"btn_deletFolder")
        self.btn_deletFolder.setGeometry(QRect(350, 90, 91, 31))
        self.btn_deletFolder.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.searchLable_2 = QLabel(self.page_extract)
        self.searchLable_2.setObjectName(u"searchLable_2")
        self.searchLable_2.setGeometry(QRect(30, 230, 91, 16))
        self.searchLable_2.setFont(font1)
        self.searchLable_2.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.btn_addTagGroup = QPushButton(self.page_extract)
        self.btn_addTagGroup.setObjectName(u"btn_addTagGroup")
        self.btn_addTagGroup.setGeometry(QRect(390, 270, 51, 41))
        self.btn_addTagGroup.setStyleSheet(u"*{border-radius:5px;\n"
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
        self.btn_delTagGroup = QPushButton(self.page_extract)
        self.btn_delTagGroup.setObjectName(u"btn_delTagGroup")
        self.btn_delTagGroup.setGeometry(QRect(390, 320, 51, 37))
        self.btn_delTagGroup.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.tag_group = QTabWidget(self.page_extract)
        self.tag_group.setObjectName(u"tag_group")
        self.tag_group.setGeometry(QRect(30, 250, 351, 181))
        self.tag_group.setMinimumSize(QSize(0, 0))
        self.tag_group.setMaximumSize(QSize(1000, 1000))
        self.tag_group.setStyleSheet(u"QTabWidget::Pane{\n"
"background-color: white;\n"
"border-radius:10px;\n"
"border: 1px solid lightgray;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"	background: rgb(255,255,255);\n"
"   \n"
"  padding: 3px;\n"
"	color: rgb(221, 221, 221);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"	background-color: rgb(168, 156, 225);\n"
"}\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: rgb(110, 92, 194);\n"
" }")
        self.tag_group.setTabShape(QTabWidget.Rounded)
        self.tag_group.setTabsClosable(False)
        self.tag_group.setMovable(False)
        self.tag_group.setTabBarAutoHide(False)
        self.btn_addTag = QPushButton(self.page_extract)
        self.btn_addTag.setObjectName(u"btn_addTag")
        self.btn_addTag.setGeometry(QRect(390, 375, 25, 25))
        self.btn_addTag.setMinimumSize(QSize(25, 25))
        self.btn_addTag.setMaximumSize(QSize(25, 25))
        self.btn_addTag.setStyleSheet(u"*{border-radius:5px;\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/\u52a0\u51cf\u7ec4\u4ef6\u52a0\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addTag.setIcon(icon5)
        self.btn_delTag = QPushButton(self.page_extract)
        self.btn_delTag.setObjectName(u"btn_delTag")
        self.btn_delTag.setGeometry(QRect(390, 405, 25, 25))
        self.btn_delTag.setMinimumSize(QSize(25, 25))
        self.btn_delTag.setMaximumSize(QSize(25, 25))
        self.btn_delTag.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/\u51cf\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delTag.setIcon(icon6)
        self.list_fileKeyword = QListWidget(self.page_extract)
        self.list_fileKeyword.setObjectName(u"list_fileKeyword")
        self.list_fileKeyword.setGeometry(QRect(30, 160, 311, 55))
        self.list_fileKeyword.setStyleSheet(u"*{border-radius:10px;\n"
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
        self.btn_addFileKeyword = QPushButton(self.page_extract)
        self.btn_addFileKeyword.setObjectName(u"btn_addFileKeyword")
        self.btn_addFileKeyword.setGeometry(QRect(350, 160, 25, 25))
        self.btn_addFileKeyword.setMinimumSize(QSize(25, 25))
        self.btn_addFileKeyword.setMaximumSize(QSize(25, 25))
        self.btn_addFileKeyword.setStyleSheet(u"*{border-radius:5px;\n"
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
        self.btn_addFileKeyword.setIcon(icon5)
        self.btn_deletFileKeyWord = QPushButton(self.page_extract)
        self.btn_deletFileKeyWord.setObjectName(u"btn_deletFileKeyWord")
        self.btn_deletFileKeyWord.setGeometry(QRect(350, 190, 25, 25))
        self.btn_deletFileKeyWord.setMinimumSize(QSize(25, 25))
        self.btn_deletFileKeyWord.setMaximumSize(QSize(25, 25))
        self.btn_deletFileKeyWord.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_deletFileKeyWord.setIcon(icon6)
        self.searchLable_3 = QLabel(self.page_extract)
        self.searchLable_3.setObjectName(u"searchLable_3")
        self.searchLable_3.setGeometry(QRect(30, 140, 111, 16))
        self.searchLable_3.setFont(font1)
        self.searchLable_3.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.stackedWidget.addWidget(self.page_extract)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.side_assist_window = QFrame(self.main_body)
        self.side_assist_window.setObjectName(u"side_assist_window")
        self.side_assist_window.setMinimumSize(QSize(250, 0))
        self.side_assist_window.setMaximumSize(QSize(60, 16777215))
        self.side_assist_window.setStyleSheet(u"background-color: rgb(244, 241, 250);\n"
"border-bottom-right-radius:10px;")
        self.side_assist_window.setFrameShape(QFrame.NoFrame)
        self.side_assist_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.side_assist_window)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_side = QStackedWidget(self.side_assist_window)
        self.stackedWidget_side.setObjectName(u"stackedWidget_side")
        self.sidePage_extract = QWidget()
        self.sidePage_extract.setObjectName(u"sidePage_extract")
        self.list_programStep = QListWidget(self.sidePage_extract)
        self.list_programStep.setObjectName(u"list_programStep")
        self.list_programStep.setGeometry(QRect(30, 39, 191, 291))
        self.list_programStep.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121);\n"
"font-size:11px;}\n"
"\n"
"QScrollBar:vertical {              \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"        width:4px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"      background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130"
                        "), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar:horizontal{\n"
" border: 1px solid #999999;\n"
"	background:white;\n"
"	height:6px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizonta {\n"
"      background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:horizonta {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizonta {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130)"
                        ",  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }")
        self.folderPathLable_2 = QLabel(self.sidePage_extract)
        self.folderPathLable_2.setObjectName(u"folderPathLable_2")
        self.folderPathLable_2.setGeometry(QRect(30, 20, 91, 16))
        self.folderPathLable_2.setFont(font1)
        self.folderPathLable_2.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.btn_ExtractionStart = QPushButton(self.sidePage_extract)
        self.btn_ExtractionStart.setObjectName(u"btn_ExtractionStart")
        self.btn_ExtractionStart.setGeometry(QRect(30, 390, 141, 41))
        self.btn_ExtractionStart.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(235, 159, 34);\n"
"}")
        self.check_asRow = QCheckBox(self.sidePage_extract)
        self.check_asRow.setObjectName(u"check_asRow")
        self.check_asRow.setGeometry(QRect(31, 340, 81, 20))
        self.check_asRow.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.check_asColumn = QCheckBox(self.sidePage_extract)
        self.check_asColumn.setObjectName(u"check_asColumn")
        self.check_asColumn.setGeometry(QRect(31, 362, 81, 20))
        self.check_asColumn.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.check_autoArrange = QCheckBox(self.sidePage_extract)
        self.check_autoArrange.setObjectName(u"check_autoArrange")
        self.check_autoArrange.setGeometry(QRect(150, 340, 81, 20))
        self.check_autoArrange.setStyleSheet(u"QCheckBox::indicator {\n"
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
        self.btn_ExtractionReset = QPushButton(self.sidePage_extract)
        self.btn_ExtractionReset.setObjectName(u"btn_ExtractionReset")
        self.btn_ExtractionReset.setGeometry(QRect(181, 390, 39, 41))
        self.btn_ExtractionReset.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_processDelete = QPushButton(self.sidePage_extract)
        self.btn_processDelete.setObjectName(u"btn_processDelete")
        self.btn_processDelete.setGeometry(QRect(189, 303, 25, 20))
        self.btn_processDelete.setMinimumSize(QSize(0, 0))
        self.btn_processDelete.setMaximumSize(QSize(25, 25))
        self.btn_processDelete.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.btn_processDelete.setIcon(icon6)
        self.stackedWidget_side.addWidget(self.sidePage_extract)
        self.sidePage_settings = QWidget()
        self.sidePage_settings.setObjectName(u"sidePage_settings")
        self.stackedWidget_side.addWidget(self.sidePage_settings)
        self.sidePage_write = QWidget()
        self.sidePage_write.setObjectName(u"sidePage_write")
        self.list_programStep_2 = QListWidget(self.sidePage_write)
        self.list_programStep_2.setObjectName(u"list_programStep_2")
        self.list_programStep_2.setGeometry(QRect(30, 30, 191, 399))
        self.list_programStep_2.setStyleSheet(u"*{border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121);\n"
"font-size:11px;}\n"
"\n"
"QScrollBar:vertical {              \n"
"        border: 1px solid #999999;\n"
"        background:white;\n"
"        width:4px;    \n"
"        margin: 0px 0px 0px 0px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"      background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130"
                        "), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"QScrollBar:horizontal{\n"
" border: 1px solid #999999;\n"
"	background:white;\n"
"	height:6px;\n"
"	margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"      background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"        min-height: 0px;\n"
"    }\n"
"    QScrollBar::add-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"       subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:horizontal {\n"
"       background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 1"
                        "30),  stop:1 rgb(32, 47, 130));\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }")
        self.folderPathLable_3 = QLabel(self.sidePage_write)
        self.folderPathLable_3.setObjectName(u"folderPathLable_3")
        self.folderPathLable_3.setGeometry(QRect(30, 11, 91, 16))
        self.folderPathLable_3.setFont(font1)
        self.folderPathLable_3.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.btn_writer_processClear = QPushButton(self.sidePage_write)
        self.btn_writer_processClear.setObjectName(u"btn_writer_processClear")
        self.btn_writer_processClear.setGeometry(QRect(174, 381, 39, 39))
        self.btn_writer_processClear.setStyleSheet(u"*{border-radius:5px;\n"
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
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(203, 125, 126);\n"
"}")
        self.stackedWidget_side.addWidget(self.sidePage_write)
        self.sidePage_check = QWidget()
        self.sidePage_check.setObjectName(u"sidePage_check")
        self.stackedWidget_side.addWidget(self.sidePage_check)
        self.sidePage_transfer = QWidget()
        self.sidePage_transfer.setObjectName(u"sidePage_transfer")
        self.stackedWidget_side.addWidget(self.sidePage_transfer)

        self.verticalLayout_4.addWidget(self.stackedWidget_side)


        self.horizontalLayout.addWidget(self.side_assist_window)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tag_group.setCurrentIndex(-1)
        self.stackedWidget_side.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Eazy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"accountant", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"V0.2", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.btn_menu_extract.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6", None))
        self.btn_menu_write.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165", None))
        self.btn_menu_transfer.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btn_menu_check.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5bf9", None))
        self.btn_menu_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6\u8def\u5f84", None))
        self.btn_write_readFolder.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939", None))
        self.btn_write_deleteFolder.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6587\u4ef6\u5939", None))
        self.comboBox_selectWriterGroup.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5199\u5165\u7ec4", None))
        self.comboBox_selectWriterGroup.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65b0\u5199\u5165\u7ec4", None))

        self.btn_renameWriterGroup.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540d", None))
        self.btn_addWriterGroup.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5199\u5165\u7ec4", None))
        self.btn_deleteWriterGroup.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4\u5668", None))
        self.btn_writer_edit.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.btn_writer_copy.setText("")
        self.btn_writer_delete.setText("")
        self.btn_writer_name.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5ea6\u786e\u8ba4", None))
        self.btn_writer_batchOpr.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u8fd0\u884c", None))
        self.btn_writer_opr.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.btn_writer_add.setText("")
        self.folderPathLable.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6\u8def\u5f84", None))
        self.btn_browseFolder.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939", None))
        self.btn_deletFolder.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6587\u4ef6\u5939", None))
        self.searchLable_2.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u7ec4", None))
        self.btn_addTagGroup.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\n"
"\u6807\u7b7e\u7ec4", None))
        self.btn_delTagGroup.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\n"
"\u6807\u7b7e\u7ec4", None))
        self.btn_addTag.setText("")
        self.btn_delTag.setText("")
        self.btn_addFileKeyword.setText("")
        self.btn_deletFileKeyWord.setText("")
        self.searchLable_3.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u68c0\u7d22\u5173\u952e\u8bcd", None))
        self.folderPathLable_2.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b", None))
        self.btn_ExtractionStart.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210", None))
        self.check_asRow.setText(QCoreApplication.translate("MainWindow", u"\u6309\u884c\u6392\u5217", None))
        self.check_asColumn.setText(QCoreApplication.translate("MainWindow", u"\u6309\u5217\u6392\u5217", None))
        self.check_autoArrange.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6392\u5e8f", None))
        self.btn_ExtractionReset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.btn_processDelete.setText("")
        self.folderPathLable_3.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b", None))
        self.btn_writer_processClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
    # retranslateUi

