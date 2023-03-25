# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EazyAccountantApp_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(855, 505)
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
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
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
"}")
        self.searchLable = QLabel(self.page_extract)
        self.searchLable.setObjectName(u"searchLable")
        self.searchLable.setGeometry(QRect(30, 140, 91, 16))
        self.searchLable.setFont(font1)
        self.searchLable.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.list_keyword = QListWidget(self.page_extract)
        self.list_keyword.setObjectName(u"list_keyword")
        self.list_keyword.setGeometry(QRect(30, 160, 211, 51))
        self.list_keyword.setStyleSheet(u"*{border-radius:10px;\n"
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
        self.btn_addKeyword = QPushButton(self.page_extract)
        self.btn_addKeyword.setObjectName(u"btn_addKeyword")
        self.btn_addKeyword.setGeometry(QRect(350, 160, 51, 51))
        self.btn_addKeyword.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(81, 66, 147) ;\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}")
        self.textInput_keyword = QPlainTextEdit(self.page_extract)
        self.textInput_keyword.setObjectName(u"textInput_keyword")
        self.textInput_keyword.setGeometry(QRect(250, 160, 91, 51))
        self.textInput_keyword.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(232, 232, 232);\n"
"color: rgb(121, 121, 121)")
        self.btn_deletKeyword = QPushButton(self.page_extract)
        self.btn_deletKeyword.setObjectName(u"btn_deletKeyword")
        self.btn_deletKeyword.setGeometry(QRect(409, 160, 31, 50))
        self.btn_deletKeyword.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
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
        self.tag_group.setMovable(True)
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
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u52a0\u51cf\u7ec4\u4ef6\u52a0\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addTag.setIcon(icon3)
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
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/\u51cf\u53f7.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delTag.setIcon(icon4)
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
        self.side_assist_window.setStyleSheet(u"background-color: rgb(227, 227, 235);\n"
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
        self.folderPathLable_2 = QLabel(self.sidePage_extract)
        self.folderPathLable_2.setObjectName(u"folderPathLable_2")
        self.folderPathLable_2.setGeometry(QRect(30, 20, 91, 16))
        self.folderPathLable_2.setFont(font1)
        self.folderPathLable_2.setStyleSheet(u"color: rgb(127, 127, 127);")
        self.btn_ExtractionStart = QPushButton(self.sidePage_extract)
        self.btn_ExtractionStart.setObjectName(u"btn_ExtractionStart")
        self.btn_ExtractionStart.setGeometry(QRect(30, 390, 81, 41))
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
"}")
        self.btn_ExtractionExport = QPushButton(self.sidePage_extract)
        self.btn_ExtractionExport.setObjectName(u"btn_ExtractionExport")
        self.btn_ExtractionExport.setGeometry(QRect(160, 390, 61, 41))
        self.btn_ExtractionExport.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(217, 217, 217) ;\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
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
        self.btn_ExtractionStop = QPushButton(self.sidePage_extract)
        self.btn_ExtractionStop.setObjectName(u"btn_ExtractionStop")
        self.btn_ExtractionStop.setGeometry(QRect(116, 390, 39, 41))
        self.btn_ExtractionStop.setStyleSheet(u"*{border-radius:5px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color:rgb(217, 217, 217) ;\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}")
        self.stackedWidget_side.addWidget(self.sidePage_extract)
        self.sidePage_settings = QWidget()
        self.sidePage_settings.setObjectName(u"sidePage_settings")
        self.stackedWidget_side.addWidget(self.sidePage_settings)
        self.sidePage_write = QWidget()
        self.sidePage_write.setObjectName(u"sidePage_write")
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

        self.stackedWidget.setCurrentIndex(3)
        self.tag_group.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Eazy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"accountant", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"V1.0", None))
        self.minimizeButton.setText("")
        self.closeButton.setText("")
        self.btn_menu_extract.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6", None))
        self.btn_menu_write.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165", None))
        self.btn_menu_transfer.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.btn_menu_check.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5bf9", None))
        self.btn_menu_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.folderPathLable.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6\u8def\u5f84", None))
        self.btn_browseFolder.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u6587\u4ef6\u5939", None))
        self.btn_deletFolder.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6587\u4ef6\u5939", None))
        self.searchLable.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u68c0\u7d22\u5173\u952e\u8bcd", None))
        self.btn_addKeyword.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.btn_deletKeyword.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.searchLable_2.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u7ec4", None))
        self.btn_addTagGroup.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\n"
"\u6807\u7b7e\u7ec4", None))
        self.btn_delTagGroup.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\n"
"\u6807\u7b7e\u7ec4", None))
        self.btn_addTag.setText("")
        self.btn_delTag.setText("")
        self.folderPathLable_2.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b", None))
        self.btn_ExtractionStart.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.btn_ExtractionExport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.check_asRow.setText(QCoreApplication.translate("MainWindow", u"\u6309\u884c\u6392\u5217", None))
        self.check_asColumn.setText(QCoreApplication.translate("MainWindow", u"\u6309\u5217\u6392\u5217", None))
        self.check_autoArrange.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u6392\u5e8f", None))
        self.btn_ExtractionStop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
    # retranslateUi

