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
    QWidget,QTextBrowser)
from PySide6.QtWidgets import *

from ui_EazyAccountantApp_UI import Ui_MainWindow

WINDOW_SIZE = 0

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.OnDrag = False
        self.setAcceptDrops(True)

        self.folderPaths = []
        self.keywords = []
        self.status = {
            "btn_menu_check":False,
            "btn_menu_extract":False,
            "btn_menu_setting":False,
            "btn_menu_transfer":False,
            "btn_menu_write":False,
        }

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
        self.resize(820,500)

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
        self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_extract)
        self.ui.side_assist_window.setMinimumWidth(250)
        self.status["btn_menu_extract"] = True
        #stacked pages navigation
        self.ui.btn_menu_check.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_check))
        self.ui.btn_menu_check.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_check))
        self.ui.btn_menu_check.clicked.connect(self.SetStatus)
        self.ui.btn_menu_extract.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract))
        self.ui.btn_menu_extract.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_extract))
        self.ui.btn_menu_extract.clicked.connect(self.SetStatus)
        self.ui.btn_menu_transfer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_transfer))
        self.ui.btn_menu_transfer.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_transfer))
        self.ui.btn_menu_transfer.clicked.connect(self.SetStatus)
        self.ui.btn_menu_write.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_write))
        self.ui.btn_menu_write.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_write))
        self.ui.btn_menu_write.clicked.connect(self.SetStatus)
        self.ui.btn_menu_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_menu_setting.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_settings))
        self.ui.btn_menu_setting.clicked.connect(self.SetStatus)


        #Menu Button Styling
        #default button style set
        defaultStyle = self.ui.btn_menu_extract.styleSheet()+("border-left: 1px solid rgb(255,179,54);")
        self.ui.btn_menu_extract.setStyleSheet(defaultStyle)
        #button style click event
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        #############Extract page Setting##################
        self.ui.btn_browseFolder.clicked.connect(self.ChooseFolderPath)
        self.ui.btn_deletFolder.clicked.connect(self.DeleteFolderPath)
        self.ui.textInput_keyword.setPlaceholderText("在此输入\n关键词")
        self.ui.btn_addKeyword.clicked.connect(self.AddKeyword)
        self.ui.btn_deletKeyword.clicked.connect(self.DeleteKeyword)
        self.ui.list_keyword.itemDoubleClicked.connect(self.DoubleClicked_to_edit)



#####################################################################################
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

#----------------------------menu button trigger-------------------------------------
    def SetStatus(self):
        for key in self.status:
            if key == self.sender().objectName():
                self.status[key] = True
            else:
                self.status[key] = False
        #print(self.status)
        self.resizeAssistWindow()

    def resizeAssistWindow(self):
        if(self.sender().objectName() == "btn_menu_extract"):
            self.ui.side_assist_window.setMinimumWidth(250)
        else:
            self.ui.side_assist_window.setMinimumWidth(100) 

            

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

#######################################extract page###############################################
#----------------------------file path------------------------------------------------
    #browse folder
    def ChooseFolderPath(self):
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getExistingDirectory(mainWindow,"选择文件夹")
        if selectedDir not in self.folderPaths:
            self.ui.list_folderPath.addItem(QListWidgetItem(selectedDir))
            self.folderPaths.append(selectedDir)
        
    
    def DeleteFolderPath(self):
        curItem_row = self.ui.list_folderPath.currentRow()
        item = self.ui.list_folderPath.takeItem(curItem_row)
        
        index = 0
        for path in self.folderPaths:
            if path == item.text():
                self.folderPaths.pop(index)
            index += 1
    
        del item
   
   #drag folder path
    def dragEnterEvent(self,event):
        path = event.mimeData().urls()[0].toLocalFile()
        
        if path not in self.folderPaths and self.status["btn_menu_extract"]:
            self.folderPaths.append(path)
            self.ui.list_folderPath.addItem(QListWidgetItem(path))
        event.accept()


#------------------------------------------------------------------------------------

#-----------------------------keyword------------------------------------------------
    def AddKeyword(self):
        if not self.ui.textInput_keyword.toPlainText() == "" or self.ui.textInput_keyword.toPlainText() is None:
            if self.ui.textInput_keyword.toPlainText() not in self.keywords:
                text = self.ui.textInput_keyword.toPlainText()
                self.ui.list_keyword.addItem(QListWidgetItem(text))
                self.ui.textInput_keyword.setPlainText(None)
                self.keywords.append(text)
            else:
                self.ui.textInput_keyword.setPlainText(None)

    def DeleteKeyword(self):
        selected_row = self.ui.list_keyword.currentRow()
        item = self.ui.list_keyword.takeItem(selected_row)

        index = 0
        for w in self.keywords:
            if w == item.text():
                self.keywords.pop(index)
            index += 1

        del item

    def DoubleClicked_to_edit(self, item):
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        if not item.isSelected():
            item.setSelected(True)
#--------------------------------------------------------------------------------------


##############################################################################################
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

