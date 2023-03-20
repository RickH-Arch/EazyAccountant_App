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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 493)
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
        self.main_header.setStyleSheet(u"background-color:rgb(24, 34, 50);\n"
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
"	background:rgb(67, 98, 141);\n"
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
"	background:rgb(67, 98, 141);\n"
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
        self.left_side_menu.setStyleSheet(u"*{background-color: rgb(24, 34, 50);\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 20px 10px;\n"
"	border:none;\n"
"	border-left: 1px solid transparent;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(24, 34, 50);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background:rgb(42, 61, 89)\n"
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
        self.center_main_items.setStyleSheet(u"background-color: rgb(51, 74, 107);")
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
        self.folderPathLable.setGeometry(QRect(34, 20, 91, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.folderPathLable.setFont(font)
        self.folderPathLable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_browseFolder = QPushButton(self.page_extract)
        self.btn_browseFolder.setObjectName(u"btn_browseFolder")
        self.btn_browseFolder.setGeometry(QRect(350, 40, 91, 41))
        self.btn_browseFolder.setStyleSheet(u"*{border-radius:10px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(139, 176, 52);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}")
        self.list_folderPath = QListWidget(self.page_extract)
        self.list_folderPath.setObjectName(u"list_folderPath")
        self.list_folderPath.setGeometry(QRect(30, 40, 311, 81))
        self.list_folderPath.setStyleSheet(u"border-radius:10px;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.btn_deletFolder = QPushButton(self.page_extract)
        self.btn_deletFolder.setObjectName(u"btn_deletFolder")
        self.btn_deletFolder.setGeometry(QRect(350, 90, 91, 31))
        self.btn_deletFolder.setStyleSheet(u"*{border-radius:10px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(143, 56, 48);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}")
        self.searchLable = QLabel(self.page_extract)
        self.searchLable.setObjectName(u"searchLable")
        self.searchLable.setGeometry(QRect(30, 150, 91, 16))
        self.searchLable.setFont(font)
        self.searchLable.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.list_keyword = QListWidget(self.page_extract)
        self.list_keyword.setObjectName(u"list_keyword")
        self.list_keyword.setGeometry(QRect(30, 170, 211, 81))
        self.list_keyword.setStyleSheet(u"border-radius:10px;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.btn_addKeyword = QPushButton(self.page_extract)
        self.btn_addKeyword.setObjectName(u"btn_addKeyword")
        self.btn_addKeyword.setGeometry(QRect(350, 170, 91, 41))
        self.btn_addKeyword.setStyleSheet(u"*{border-radius:10px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(139, 176, 52);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}")
        self.textInput_keyword = QPlainTextEdit(self.page_extract)
        self.textInput_keyword.setObjectName(u"textInput_keyword")
        self.textInput_keyword.setGeometry(QRect(250, 170, 91, 81))
        self.textInput_keyword.setStyleSheet(u"border-radius:10px;\n"
"border:1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.btn_deletKeyword = QPushButton(self.page_extract)
        self.btn_deletKeyword.setObjectName(u"btn_deletKeyword")
        self.btn_deletKeyword.setGeometry(QRect(350, 220, 91, 31))
        self.btn_deletKeyword.setStyleSheet(u"*{border-radius:10px;\n"
"	font-size:12px;\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(143, 56, 48);\n"
"}\n"
"\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(255, 179, 54);\n"
"}")
        self.line = QFrame(self.page_extract)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(7, 130, 501, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
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
        self.side_assist_window.setStyleSheet(u"background-color: rgb(66, 96, 138);\n"
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


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
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
        self.btn_addKeyword.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5173\u952e\u8bcd", None))
        self.btn_deletKeyword.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5173\u952e\u8bcd", None))
    # retranslateUi

