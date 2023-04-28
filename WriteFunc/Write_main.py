import sys


from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

from utils.FolderPathManager import FolderPathMgr
from .WriteDataManager import WriteDataManager
import utils.styleSheets as styles

class WriteMain:
    def __init__(self) -> None:
        self.dataMgr = WriteDataManager()

#-----------------------load function------------------------------

    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadWriterGroup(self,cBox,btn):
        for g in self.dataMgr.data.writerGroups:
            cBox.addItem(g.groupName)
        cBox.setCurrentText(self.dataMgr.data.writerGroupNow)
        if self.dataMgr.data.writerGroupNow == "全部写入组":
            btn.setStyleSheet(styles.buttonDisable)
            btn.setCheckable(False)


#-----------------------------------------------------
    def AddFolderPath(self,list):
        selectedDir = FolderPathMgr.AddFolderPath()
        if self.dataMgr.AddFolderPath(selectedDir):
            list.addItem(QListWidgetItem(selectedDir))

    def DeleteFolderPath(self,list):
        curItem_row = list.currentRow()
        item = list.item(curItem_row)
        if self.dataMgr.DeleteFolderPath(item.text()):
            list.takeItem(curItem_row)
            del item

    def SwitchWriterGroup(self,cBox,renameBtn):
        curText = cBox.currentText()
        if self.dataMgr.SwitchWriterGroup(curText):
            if curText == "全部写入组":
                renameBtn.setStyleSheet(styles.buttonDisable)
            else:
                renameBtn.setStyleSheet(styles.buttonEnable)
                renameBtn.setCheckable(True)
    
    

        
        