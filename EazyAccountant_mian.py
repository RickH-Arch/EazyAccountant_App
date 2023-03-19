import sys
import os 
import platform


from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from PySide6.QtWidgets import *

from ui_EazyAccountantApp_UI import Ui_MainWindow

WINDOW_SIZE = 0

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.OnDrag = False

        #remove window title bar
        self.setWindowFlag(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)

        #Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        #apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.resize(800,500)

        #Button click events to top bar buttons
        #Minimize Window
        self.ui.minimizeButton.clicked.connect(lambda:self.showMinimized())

        #restore/Maximize window
        #self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        #Close Window
        self.ui.closeButton.clicked.connect(lambda: self.close())

        #Left menu toggle button
        self.ui.menuButton.clicked.connect(lambda: self.slideLeftMenu())

        #STACKED PAGES
        #set default page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract)
        #stacked pages navigation
        self.ui.btn_menu_check.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_check))
        self.ui.btn_menu_extract.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract))
        self.ui.btn_menu_transfer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_transfer))
        self.ui.btn_menu_write.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_write))
        self.ui.btn_menu_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))


        #Menu Button Styling
        #default button style set
        defaultStyle = self.ui.btn_menu_extract.styleSheet()+("border-left: 1px solid rgb(255,179,54);")
        self.ui.btn_menu_extract.setStyleSheet(defaultStyle)
        #button style click event
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)



#--------------------------------move----------------------------------------------
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            if(event.pos().y()<50 and event.pos().x()>100):
                self.OnDrag = True
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.OnDrag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.OnDrag = False


#-------------------------------------------------------------------------------------

#-----------------------------left menu slide-----------------------------------------
    def slideLeftMenu(self):
        #get current left menu width
        width = self.ui.left_side_menu.width()
        if width == 50:
            newWidth = 110
        else:
            newWidth = 50

        #animate transition
        self.animation = QPropertyAnimation(self.ui.left_side_menu,b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
#------------------------------------------------------------------------------------

#----------------------------menu button styling--------------------------------------
    def applyButtonStyle(self):
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                defaultStyle = w.styleSheet().replace("border-left: 1px solid rgb(255,179,54);","")
                w.setStyleSheet(defaultStyle)

        newStyle = self.sender().styleSheet()+("border-left: 1px solid rgb(255,179,54);")
        self.sender().setStyleSheet(newStyle)
        return

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
    def restore_or_maximize_window(self):
        #Global windows state
        win_status = WINDOW_SIZE

        if win_status == 0:
           WINDOW_SIZE = 1
           self.showMaximized()
        else:
            WINDOW_SIZE = 0
            self.showNormal()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())

