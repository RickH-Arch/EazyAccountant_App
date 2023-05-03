import sys
import os 
import platform


from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget,QTextBrowser)
from PySide6.QtWidgets import *

from EasyAccountantApp_UI_ui import Ui_MainWindow
from WriterEditor_ui import Ui_Form as WriterEditor

from ExtractFunc.Extract_main import *
from WriteFunc.Write_main import *
from utils.DoubleClickChecker import DoubleClickChecker
from utils.DataManager import DataMgr


WINDOW_SIZE = 0

extractMain = ExtractMain()
writerMain = WriteMain()

class MainWindow(QMainWindow):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.OnDrag = False
        self.setAcceptDrops(True)
        self.globalDataPath = "Cache\\globalData.json"
        self.glbData = DataMgr.LoadData(self.globalDataPath)
        if self.glbData is None:
            self.glbData = GlobalData()

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
        
        self.setFixedHeight(500)
        self.setFixedWidth(820)

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
        self.ui.btn_menu_check.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_check),
                                                self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_check),
                                               self.glbData.selectPage(3),
                                                self.MenuButtonClickedFinished()))
        self.ui.btn_menu_check.clicked.connect(self.SetStatus)
        self.ui.btn_menu_extract.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract),
                                                        self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_extract),
                                                        self.glbData.selectPage(0),
                                                        self.MenuButtonClickedFinished()))
        self.ui.btn_menu_extract.clicked.connect(self.SetStatus)
        self.ui.btn_menu_transfer.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_transfer),
                                                            self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_transfer),
                                                            self.glbData.selectPage(2),
                                                            self.MenuButtonClickedFinished()))
        self.ui.btn_menu_transfer.clicked.connect(self.SetStatus)
        self.ui.btn_menu_write.clicked.connect(lambda: (self.ui.stackedWidget.setCurrentWidget(self.ui.page_write),
                                                        self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_write),
                                                        self.glbData.selectPage(1),
                                                        self.MenuButtonClickedFinished()))
        self.ui.btn_menu_write.clicked.connect(self.SetStatus)
        self.ui.btn_menu_setting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_menu_setting.clicked.connect(lambda: self.ui.stackedWidget_side.setCurrentWidget(self.ui.sidePage_settings))
        self.ui.btn_menu_setting.clicked.connect(self.SetStatus)


        #Menu Button Styling
        #default button style set
        defaultStyle = self.ui.btn_menu_extract.styleSheet()+("background-color:rgb(125,108,202);")
        self.ui.btn_menu_extract.setStyleSheet(defaultStyle)
        #button style click event
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

#--------------------------------------------------------------------------------------
        #############Extract page Setting##################
        #folder Path
        extractMain.LoadFolderPath(self.ui.list_folderPath)
        self.ui.btn_browseFolder.clicked.connect(lambda:extractMain.AddFolderPath(self.ui.list_folderPath))
        self.ui.btn_deletFolder.clicked.connect(lambda:extractMain.DeleteFolderPath(self.ui.list_folderPath))
        #file keyword
        extractMain.LoadFileKeyword(self.ui.list_fileKeyword)
        self.ui.btn_addFileKeyword.clicked.connect(lambda:extractMain.AddKeyword(self.ui.list_fileKeyword))
        self.ui.btn_deletFileKeyWord.clicked.connect(lambda:extractMain.DeleteKeyword(self.ui.list_fileKeyword))
        self.ui.list_fileKeyword.itemDoubleClicked.connect(lambda item:extractMain.ListDoubleClickedEdit(item))
        self.ui.list_fileKeyword.itemChanged.connect(lambda item: extractMain.OnListChange(self.ui.list_fileKeyword,item))
        #sheet keyword
        #extractMain.LoadKeyWord(self.ui.list_keyword)
        #self.ui.btn_addKeyword.clicked.connect(lambda:extractMain.AddKeyword(self.ui.list_keyword))
        #self.ui.btn_deletKeyword.clicked.connect(lambda: extractMain.DeleteKeyword(self.ui.list_keyword))
        #self.ui.list_keyword.itemDoubleClicked.connect(lambda item: extractMain.ListDoubleClickedEdit(item))
        #self.ui.list_keyword.itemChanged.connect(lambda item: extractMain.OnListChange(self.ui.list_keyword,item))
        #tag group
        extractMain.LoadTagGroup(self.ui.tag_group)
        self.ui.btn_addTagGroup.clicked.connect(lambda:extractMain.AddTagGroup(self.ui.tag_group))
        self.doubleChecker_delTagGrp = DoubleClickChecker(lambda:extractMain.DeleteTagGroup(self.ui.tag_group))
        self.ui.btn_delTagGroup.clicked.connect(lambda : self.doubleChecker_delTagGrp.DoubleClick())
        self.ui.btn_addTag.clicked.connect(lambda: extractMain.AddTag(self.ui.tag_group))
        self.ui.btn_delTag.clicked.connect(lambda:extractMain.DeleteTag(self.ui.tag_group))
        self.ui.tag_group.tabBarDoubleClicked.connect(lambda:extractMain.RenameTagGroup(self.ui.tag_group))
        extractMain.LoadRowFollow(self.ui.check_asRow,self.ui.check_asColumn)
        self.ui.check_asRow.clicked.connect(lambda : extractMain.SetRowFollow(self.ui.check_asRow,self.ui.check_asColumn))
        self.ui.check_asColumn.clicked.connect(lambda : extractMain.SetColumnFollow(self.ui.check_asColumn,self.ui.check_asRow))
        extractMain.LoadAutoArrange(self.ui.check_autoArrange)
        self.ui.check_autoArrange.stateChanged.connect(lambda state:extractMain.SetAutoArrange(state))
        #process
        self.ui.btn_ExtractionStart.clicked.connect(lambda: extractMain.ExtractStart(self.ui.btn_ExtractionStart,self.ui.list_programStep))
        self.ui.btn_processDelete.clicked.connect(lambda: extractMain.DeleteOnProcess(self.ui.list_programStep))
        self.ui.btn_ExtractionReset.clicked.connect(lambda:extractMain.ResetProcess(self.ui.list_programStep,self.ui.btn_ExtractionStart))
        ####################################################
#--------------------------------------------------------------------------------------------------------------
        #################write page setting#################
        #folderPath
        writerMain.LoadFolderPath(self.ui.list_write_folderPath)
        self.ui.btn_write_readFolder.clicked.connect(lambda:writerMain.AddFolderPath(self.ui.list_write_folderPath))
        self.ui.btn_write_deleteFolder.clicked.connect(lambda:writerMain.DeleteFolderPath(self.ui.list_write_folderPath))

        #writer group checkbox
        writerMain.LoadWriterGroup(self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout,self.ui.btn_renameWriterGroup)
        self.ui.comboBox_selectWriterGroup.currentIndexChanged.connect(lambda:writerMain.SwitchWriterGroup(self.ui.comboBox_selectWriterGroup,self.ui.btn_renameWriterGroup,self.ui.writerGridLayout,self.ui.filter_input))
        self.ui.btn_renameWriterGroup.clicked.connect(lambda:writerMain.RenameWriterGroup(self.ui.comboBox_selectWriterGroup))
        self.ui.btn_addWriterGroup.clicked.connect(lambda:writerMain.AddWriterGroup(self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout))
        self.doubleChecker_delWriterGroup = DoubleClickChecker(lambda:writerMain.DeleteWriterGroup(self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout))
        self.ui.btn_deleteWriterGroup.clicked.connect(lambda:self.doubleChecker_delWriterGroup.DoubleClick())
        self.ui.btn_writer_forward.clicked.connect(lambda:writerMain.RearrangeWriter(self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout,forward = True))
        self.ui.btn_writer_backward.clicked.connect(lambda:writerMain.RearrangeWriter(self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout,forward = False))
        self.ui.filter_input.textChanged.connect(lambda:writerMain.FilterTextChange(self.ui.filter_input,self.ui.comboBox_selectWriterGroup,self.ui.writerGridLayout))
        ####################################################

        if self.glbData.pageNow == 0:
            self.ui.btn_menu_extract.click()
        elif self.glbData.pageNow == 1:
            self.ui.btn_menu_write.click()
        elif self.glbData.pageNow == 2:
            self.ui.btn_menu_transfer.click()
        elif self.glbData.pageNow == 3:
            self.ui.btn_menu_check.click()


#####################################################################################
#####################################################################################
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

        #write page
        width2 = self.ui.write_frame.width()
        if width2 == 510:
            newWidth2 = 450
        else:
            newWidth2 = 510

        self.animation2 = QPropertyAnimation(self.ui.write_frame,b"size")
        self.animation2.setDuration(250)
        self.animation2.setStartValue(QSize(width2,430))
        self.animation2.setEndValue(QSize(newWidth2,430))
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation2.start()

        

        
        
#------------------------------------------------------------------------------------

#----------------------------menu button trigger-------------------------------------
    def MenuButtonClickedFinished(self):
        
        DataMgr.WriteData(self.glbData,self.globalDataPath)
    
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
        elif(self.sender().objectName() == "btn_menu_write"):
            self.ui.side_assist_window.setMinimumWidth(250)
        else:
            self.ui.side_assist_window.setMinimumWidth(100) 

            

#------------------------------------------------------------------------------------

#----------------------------menu button styling--------------------------------------
    def applyButtonStyle(self):
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                defaultStyle = w.styleSheet().replace("background-color:rgb(125,108,202);","")
                w.setStyleSheet(defaultStyle)

        newStyle = self.sender().styleSheet()+("background-color:rgb(125,108,202);")
        self.sender().setStyleSheet(newStyle)
        return

#-------------------------------------------------------------------------------------

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            QMainWindow.keyPressEvent(self, event)
            self.ui.filter_input.clearFocus()
        else:
            QMainWindow.keyPressEvent(self, event)
        
#######################################extract page###############################################
    def dragEnterEvent(self,event):
        path = event.mimeData().urls()[0].toLocalFile()
        if extractMain.AddDragFolderPath(path):
            self.ui.list_folderPath.addItem(QListWidgetItem(path))
        event.accept()

   

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

class GlobalData:
    def __init__(self) -> None:
        self.pageNow = 0
        

    def selectPage(self,idx):
        self.pageNow = idx
        
        

    

    
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec())

