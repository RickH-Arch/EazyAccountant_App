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

class WriteMain:
    def __init__(self) -> None:
        self.dataMgr = WriteDataManager()

    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

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
        
        