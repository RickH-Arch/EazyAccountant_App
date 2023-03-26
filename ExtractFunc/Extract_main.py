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

from ExtractFunc.ExtractData import *

class ExtractMain():
    def __init__(self) -> None:
        self.dataMgr = ExtractDataManager()
        

    #========Load info to ui=====================
    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadKeyWord(self,list):
        keywords = self.dataMgr.data.keywords
        for w in keywords:
            list.addItem(QListWidgetItem(w))

    def LoadTagGroup(self,tab):
        
        _tagGroups = self.dataMgr.data.tagGroups
        if len(_tagGroups) != 0:
            for _g in _tagGroups:
                
                #create new tab(hasnt add to tabWidget yet)
                newTab = QWidget()
                newTab.setObjectName(_g.groupName)
                layout = QVBoxLayout(newTab)
                layout.setSpacing(0)
                layout.setContentsMargins(2,2,2,2)
                
                #create table
                table = self.GenerateTable(newTab)
                table.setObjectName(_g.groupName)
                #print("==========>",_g.tagList)
                #add row for each tag
                for tag in _g.tagList:
                    
                    rowPos = table.rowCount()
                    table.insertRow(rowPos)
                    #add checkbox
                    checkBox = QTableWidgetItem()
                    checkBox.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    if tag.isActive:
                        checkBox.setCheckState(QtCore.Qt.Checked)
                    else:
                        checkBox.setCheckState(QtCore.Qt.UnChecked)
                    table.setItem(rowPos,0,checkBox)
                    #add tag info
                    for i,value in enumerate( tag.tagInfo.values()):
                        table.setItem(rowPos,i+1,QTableWidgetItem(value))

                layout.addWidget(table)
                tab.addTab(newTab,_g.groupName)
        else:
            self.AddTagGroupFromName(tab,"月报")
            
            

    #=============================================

    #==========Data Change=========================
    def AddFolderPath(self,list):
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getExistingDirectory(mainWindow,"选择文件夹")
        if self.dataMgr.AddFolderPath(selectedDir):
            list.addItem(QListWidgetItem(selectedDir))
        
    def AddDragFolderPath(self,path):
        return self.dataMgr.AddFolderPath(path)
        
    def DeleteFolderPath(self,list):
        curItem_row = list.currentRow()
        item = list.takeItem(curItem_row)
        if self.dataMgr.DelFolderPath(item.text()):
            del item
    
    def AddKeyword(self,list,textInput):
        word = textInput.toPlainText()
        if self.dataMgr.AddKeyword(word):
            list.addItem(QListWidgetItem(word))
        textInput.setPlainText(None)
    
    def DeleteKeyword(self,list):
        item = list.takeItem(list.currentRow())
        if self.dataMgr.DelKeyword(item.text()):
            del item
    
    def AddTagGroup(self,tabs):
        name, ok = QInputDialog.getText(None, "输入", "新标签组名称:" )
        if ok:
            self.AddTagGroupFromName(tabs,name)
    
    def AddTagGroupFromName(self,tabs,name):
        if self.dataMgr.AddTagGroup(name):
            newTab = QWidget()
            layout = QVBoxLayout(newTab)
            layout.setSpacing(0)
            layout.setContentsMargins(2,2,2,2)
            table = self.GenerateTable(newTab)
            table.setObjectName(name)
            #print("================>tablename:",table.objectName())
            self.AddTagFromRowIndex(table,0)
            layout.addWidget(table)
            tabs.addTab(newTab,name)

    def RenameTagGroup(self,tabs):
        index = tabs.currentIndex()
        rect = tabs.tabBar().tabRect(index)
        if rect.contains(tabs.tabBar().mapFromGlobal(QCursor.pos())):
            name = tabs.tabText(index)
            new_name, ok = QInputDialog.getText(tabs, "更换名称", "标签组名称:", text=name)
            if ok:
                if self.dataMgr.RenameTagGroup(index,new_name):
                    tabs.setTabText(index, new_name)

    def DeleteTagGroup(self,tabs):
        name = tabs.tabText(tabs.currentIndex())
        if self.dataMgr.DelTagGroup(name):
            tabs.removeTab(tabs.currentIndex())

    def AddTag(self,tabs):
        currentTab = tabs.currentWidget()
        table = currentTab.findChild(QTableWidget)
        rowPos = table.rowCount()
        self.AddTagFromRowIndex(table,rowPos)

    #add a new Tag to rowIndex
    def AddTagFromRowIndex(self,table,row):
        #print("==========>tableName:",table.objectName())
        if self.dataMgr.AddTag(table.objectName(),"标签{}".format(row+1)):
            table.insertRow(row)
            checkBox = QTableWidgetItem()
            checkBox.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            checkBox.setCheckState(QtCore.Qt.Checked)
            table.setItem(row,0,checkBox)
            table.setItem(row,1,QTableWidgetItem("标签{}".format(row+1)))

    def DeleteTag(self,tabs):
        groupName = tabs.tabText(tabs.currentIndex())
        currentTab = tabs.currentWidget()
        table = currentTab.findChild(QTableWidget)
        curRow = table.currentRow()
        tagName = table.item(curRow,1).text()
        if self.dataMgr.DelTag(groupName,tagName):
            table.removeRow(curRow)




    #==================================================================

    #=============================Generate=============================
    def GenerateTable(self,parent):
        table = QTableWidget(parent)
            
        #tagIns = _g.tagList[0]
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([""]+["名称","坐标","关键词","单位"])
            
        table.setStyleSheet(TableStyleSheet)
        #table.setMinimumSize(QSize(364,123))
        #table.setMaximumSize(QSize(365,124))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table.setColumnWidth(0,25)
        w = 75
        table.setColumnWidth(1,w)
        table.setColumnWidth(2,w)
        table.setColumnWidth(3,w)
        table.setColumnWidth(4,w)
        table.verticalHeader().setDefaultSectionSize(15)
        

        return table

TableStyleSheet = '''*{background-color: rgb(255, 255, 255);\n
border-radius:10px;}\n

QScrollBar {              \n
            border: none;\n
            background:white;\n
            width:3px;\n
            margin: 0px 0px 0px 0px;\n
        }\n
        QScrollBar::handle {\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n
            min-height: 0px;\n
        }\n
        QScrollBar::add-line{\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n
            height: 0px;\n
            subcontrol-position: bottom;\n
            subcontrol-origin: margin;\n
        }\n
        QScrollBar::sub-line {\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
         stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n
           height: 0 px;\n
            subcontrol-position: top;\n
          subcontrol-origin: margin;\n
        }\n'''
