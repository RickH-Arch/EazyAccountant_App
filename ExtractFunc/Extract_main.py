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

class ExtractMain:
    def __init__(self):
        #self.folderPaths = []
        #self.keywords = []
        self.storeData = {
            "folderPaths":[],
            "keywords":[],
        }

        try:
            with open("extractData.json","r") as f:
                indata = json.load(f)
                self.storeData["folderPaths"] = indata["folderPaths"]
                self.storeData["keywords"] = indata["keywords"]
        except FileNotFoundError:
            pass


    
    def AddFolderPath(self,path):
        if path == "":
            return
        if path not in self.storeData["folderPaths"]:
            self.storeData["folderPaths"].append(path)
            self.RefreshJson()
            return True
            
        else:
            return False
        
    def DelFolderPath(self,pathin):
        if pathin == "":
            return
        index = 0
        for path in self.storeData["folderPaths"]:
            if path == pathin:
                self.storeData["folderPaths"].pop(index)
                self.RefreshJson()
            index += 1

    def AddKeyword(self,keyword):
        if keyword == "":
            return
        if keyword not in self.storeData["keywords"]:
            self.storeData["keywords"].append(keyword)
            self.RefreshJson()
            return True
        else:
            return False
        
    def DelKeyword(self,keyword):
        if keyword == "":
            return
        index = 0
        for w in self.storeData["keywords"]:
            if w == keyword:
                self.storeData["keywords"].pop(index)
                self.RefreshJson()
                return True
            index += 1
        return False
    
    def RefreshJson(self):
        
        with open('extractData.json','w') as f:
            json.dump(self.storeData,f,indent = 4)

    def LoadFolderPath(self,list):
        paths = self.storeData["folderPaths"]
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadKeyWord(self,list):
        keywords = self.storeData["keywords"]
        for w in keywords:
            list.addItem(QListWidgetItem(w))
            