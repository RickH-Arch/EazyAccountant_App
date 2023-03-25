import json
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
from ExtractFunc.Tags import *
from ExtractFunc.ExtractData import *

class ExtractMain():
    def __init__(self) -> None:
        self.dataMgr = ExtractDataManager()
        

    #========Load info to ui=====================
    def LoadFolderPath(self,list):
        paths = self.dataMgr.storeData["folderPaths"]
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadKeyWord(self,list):
        keywords = self.dataMgr.storeData["keywords"]
        for w in keywords:
            list.addItem(QListWidgetItem(w))
    #=============================================

    #==========Data Chage=========================
    def AddFolderPath(self):
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getExistingDirectory(mainWindow,"选择文件夹")
        if self.dataMgr.AddFolderPath(selectedDir):
            return selectedDir
        else:
            return ""
    def AddDragFolderPath(self,path):
        return self.dataMgr.AddFolderPath(path)
        
    def DeleteFolderPath(self,path):
        return self.dataMgr.DelFolderPath(path)
    
    def AddKeyword(self,word):
        return self.dataMgr.AddKeyword(word)
    
    def DeleteKeyword(self,word):
        return self.dataMgr.DelKeyword(word)