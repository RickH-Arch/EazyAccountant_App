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

from ExtractFunc.ExtractDataManager import ExtractDataManager
from utils.ExcelManager import *
from utils.FolderPathManager import FolderPathMgr
import utils.styleSheets as styles

class ExtractMain():
    def __init__(self) -> None:
        self.dataMgr = ExtractDataManager()
        self.excelMgr = ExcelManager()
        
        self._getExcel_ = False
        self._getSheet_ = False
        self._getData_ = False
        self._exportData_ = False

        #记录读取到的excel文件以及各自用到的sheet,<MyWorkbook>
        self.myWorkbooks = []
        #记录每个tag读取到的信息,<MyTag>
        self.myTags = []

        self.sheetKeywordCache = ""
        
        

    #========Load info to ui=====================
    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadFileKeyword(self,list):
        keywords = self.dataMgr.data.file_keywords
        for w in keywords:
            list.addItem(QListWidgetItem(w))

    def LoadKeyWord(self,list):
        keywords = self.dataMgr.data.keywords
        for w in keywords:
            list.addItem(QListWidgetItem(w))

    def LoadTagGroup(self,tabs):
        
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
                        checkBox.setCheckState(QtCore.Qt.Unchecked)
                    table.setItem(rowPos,0,checkBox)
                    #add tag info
                    for i,value in enumerate( tag.tagInfo.values()):
                        table.setItem(rowPos,i+1,QTableWidgetItem(value))

                table.cellChanged.connect(lambda row,column : self.OnCellChanged(tabs,row,column))
                layout.addWidget(table)
                tabs.addTab(newTab,_g.groupName)
            tabs.setCurrentIndex(self.dataMgr.data.activeGroup)
        else:
            self.AddTagGroupFromName(tabs,"月报")
        tabs.currentChanged.connect(self.OnTabSelected)
            
    def LoadRowFollow(self,checkRow,checkCol):
        if self.dataMgr.data.followRow:
            checkRow.setChecked(True)
            checkCol.setChecked(False)
        else:
            checkRow.setChecked(False)
            checkCol.setChecked(True)

    def LoadAutoArrange(self,checkArr):
        if self.dataMgr.data.autoArrange:
            checkArr.setChecked(True)
        else:
            checkArr.setChecked(False)

    #=============================================

    #==========Data Change=========================
    def AddFolderPath(self,list):
        selectedDir = FolderPathMgr.AddFolderPath()
        if self.dataMgr.AddFolderPath(selectedDir):
            list.addItem(QListWidgetItem(selectedDir))
        
    def AddDragFolderPath(self,path):
        return self.dataMgr.AddFolderPath(path)
        
    def DeleteFolderPath(self,list):
        curItem_row = list.currentRow()
        item = list.item(curItem_row)
        if self.dataMgr.DelFolderPath(item.text()):
            list.takeItem(curItem_row)
            del item

    
    def AddKeyword(self,list):
        word = "新关键词"
        if list.objectName() == "list_keyword":
            if self.dataMgr.AddKeyword(word):
                list.addItem(QListWidgetItem(word))
        if list.objectName() == "list_fileKeyword":
            if self.dataMgr.AddFileKeyword(word):
                list.addItem(QListWidgetItem(word))
        
    def ListDoubleClickedEdit(self,item):
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        if not item.isSelected():
            item.setSelected(True)

    def OnListChange(self,list,item):
        index = list.row(item)
        target = item.text()
        if target != "":
            self.sheetKeywordCache = target
            if list.objectName() == "list_keyword":
                self.dataMgr.ChangeKeyword(index,target)
            if list.objectName() == "list_fileKeyword":
                self.dataMgr.ChangeFileKeyword(index,target)
        else:
            item.setText(self.sheetKeywordCache)

    
    def DeleteKeyword(self,list):
        item = list.item(list.currentRow())
        if list.objectName() == "list_keyword":
            if self.dataMgr.DelKeyword(item.text()):
                list.takeItem(list.currentRow())
                del item
        if list.objectName() == "list_fileKeyword":
            if self.dataMgr.DelFileKeyword(item.text()):
                list.takeItem(list.currentRow())
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

    def OnTabSelected(self,index):
        self.dataMgr.SetAvtiveGroup(index)

    def OnCellChanged(self,tabs,row,column):
        #is active check
        if column == 0:
            currentTab = tabs.currentWidget()
            table = currentTab.findChild(QTableWidget)
            item = table.item(row,column)
            status = item.checkState() == Qt.Checked
            groupName = table.objectName()
            tagName = table.item(row,1).text()
            self.dataMgr.ChangeTagActivation(groupName,tagName,status)
        #is info change
        else:
            currentTab = tabs.currentWidget()
            table = currentTab.findChild(QTableWidget)
            item = table.item(row,column)
            groupName = table.objectName()
            tagIndex = row
            infoName = table.horizontalHeaderItem(column).text()
            value = item.text()
            self.dataMgr.ChangeTagInfo(groupName,tagIndex,infoName,value)

    def SetRowFollow(self,checkBoxRow,checkBoxCol):
        if checkBoxRow.isChecked() and self.dataMgr.data.followRow == True:
            return
        elif checkBoxRow.isChecked() and self.dataMgr.data.followRow == False:
            self.dataMgr.SetRowFollow(True)
            checkBoxCol.setChecked(False)
        elif checkBoxRow.isChecked() == False:
            checkBoxRow.setChecked(True)
        
            
    def SetColumnFollow(self,checkBoxCol,checkBoxRow):
        if checkBoxCol.isChecked() and self.dataMgr.data.followRow == False:
            return
        elif checkBoxCol.isChecked() and self.dataMgr.data.followRow == True:
            self.dataMgr.SetRowFollow(False)
            checkBoxRow.setChecked(False)
        elif checkBoxCol.isChecked() == False:
            checkBoxCol.setChecked(True)

    def SetAutoArrange(self,status):
        if status == 2:
            self.dataMgr.SetAutoArrange(True)
        elif status == 0:
            self.dataMgr.SetAutoArrange(False)

    #==================================================================

    #=============================process===============================
    def ExtractStart(self,button,list):
        if self._getExcel_ == False:
            button.setStyleSheet(styles.buttonDisable)
            button.setEnabled(False)
            _workbooks,_workbookNames = self.excelMgr.GetExcelWorkBook(self.dataMgr.data.folderPaths,self.dataMgr.data.file_keywords)
            if self.dataMgr.data.autoArrange:
                _workbooks,_workbookNames = self.excelMgr.SortWorkbookByName(_workbooks,_workbookNames)
            list.addItem(QListWidgetItem("==================="))
            item = QListWidgetItem("检索到以下excel文件：")
            item.setForeground(QColor(255,0,0))
            list.addItem(item)
            list.addItem(QListWidgetItem("==================="))
            for i, n in enumerate(_workbookNames):
                list.addItem(QListWidgetItem(n))
                self.myWorkbooks.append(MyWorkBook(_workbooks[i],n))
            
            button.setStyleSheet(styles.buttonOnProcess)
            button.setEnabled(True)
            button.setText("继续")
            self._getExcel_ = True
            return
        
        if self._getSheet_ == False:
            list.clear()
            list.addItem(QListWidgetItem("==================="))
            item = QListWidgetItem("检索到以下工作表：")
            item.setForeground(QColor(255,0,0))
            list.addItem(item)
            list.addItem(QListWidgetItem("==================="))
            tagGroup = self.dataMgr.data.tagGroups[self.dataMgr.data.activeGroup]
            sheetKeywords = []
            for tag in tagGroup.tagList:
                if tag.isActive and tag.IsValid():
                    sheetKeywords.append(tag.tagInfo["工作表"])
            for i, mwb in enumerate(self.myWorkbooks) :
                sheets,sheetNames = self.excelMgr.GetSheetsFromWorkbook(mwb.workbook,sheetKeywords)
                mwb.sheets = sheets
                mwb.sheetNames = sheetNames
                item = QListWidgetItem(self.myWorkbooks[i].workbookName)
                item.setForeground(QColor(200,200,200))
                list.addItem(item)
                for sn in sheetNames:
                    output = "-->"+sn
                    list.addItem(QListWidgetItem(output))
                list.addItem(QListWidgetItem("---------------------------------------"))
                self._getSheet_ = True
            return
        
        if self._getData_ == False:
            list.clear()
            list.addItem(QListWidgetItem("==================="))
            item = QListWidgetItem("检索到以下数据：")
            item.setForeground(QColor(255,0,0))
            list.addItem(item)
            list.addItem(QListWidgetItem("==================="))
            tagGroup = self.dataMgr.data.tagGroups[self.dataMgr.data.activeGroup]
            for tag in tagGroup.tagList:
                if not tag.IsValid() or not tag.isActive:
                    continue
                myTag = MyTag(tag.tagInfo["名称"])
                if tag.tagInfo["单位"] != "":
                    myTag.tagName = tag.tagInfo["名称"]+"（"+tag.tagInfo["单位"]+"）"
                for i, mwb in enumerate(self.myWorkbooks) :
                    for i, s in enumerate(mwb.sheets) :
                        if self.excelMgr.AnalyzeFileName(s.title,tag.tagInfo["工作表"]):
                            value = self.excelMgr.GetValueFromSheet(s,tag.tagInfo["坐标"])
                            myTag.tagValues.append(value)
                            myTag.workbookNames.append(mwb.workbookName)
                self.myTags.append(myTag)
            for mytag in self.myTags:
                item = QListWidgetItem(mytag.tagName)
                item.setForeground(QColor(110,92,194))
                list.addItem(item)
                for i,wbname in enumerate(mytag.workbookNames):
                    item = QListWidgetItem(wbname)
                    item.setForeground(QColor(150,150,150))
                    list.addItem(item)
                    output = "-->"+str(mytag.tagValues[i])
                    list.addItem(QListWidgetItem(output))
                list.addItem(QListWidgetItem("---------------------------------------"))
            self._getData_ = True
            button.setText("导出")
            return
        
        if self._exportData_ == False:
            #get all tag name
            tagNames = []
            workbookNames = []
            for myTag in self.myTags:
                tagNames.append(myTag.tagName)
            for mwb in self.myWorkbooks:
                workbookNames.append(mwb.workbookShortName)

            
            if not self.dataMgr.data.followRow:
                #工作簿名称按照行进行排列
                self.wb = self.excelMgr.CreateExcel(tagNames,workbookNames)
                ws = self.wb.worksheets[0]
                #遍历工作簿名称
                rowCur = 2
                hasWbName = True
                while hasWbName:
                    if ws.cell(rowCur+1,1).value == None:
                        hasWbName = False
                    workbookNameNow = ws.cell(rowCur,1).value

                    colCur = 2
                    hasTagName = True
                    while hasTagName:
                        if ws.cell(1,colCur+1).value == None:
                            hasTagName = False
                        tagNameNow = ws.cell(1,colCur).value
                        value = self.GetValueFromMyTag(tagNameNow,workbookNameNow)
                        ws.cell(rowCur,colCur,value)
                        colCur+=1
                    rowCur+=1
            else:
                self.wb = self.excelMgr.CreateExcel(workbookNames,tagNames)
                ws = self.wb.worksheets[0]
                #遍历工作簿名称
                rowCur = 2
                hasTagName = True
                while hasTagName:
                    if ws.cell(rowCur+1,1).value == None:
                        hasTagName = False
                    tagNameNow = ws.cell(rowCur,1).value

                    colCur = 2
                    hasWbName = True
                    while hasWbName:
                        w = ws.cell(1,colCur+1).value
                        if ws.cell(1,colCur+1).value == None:
                            hasWbName = False
                        workbookNameNow = ws.cell(1,colCur).value
                        value = self.GetValueFromMyTag(tagNameNow,workbookNameNow)
                        ws.cell(rowCur,colCur,value)
                        colCur+=1
                    rowCur+=1

            selectedDir = FolderPathMgr.SelectExportFilePath()
            #print(selectedDir)
            self.wb.save(selectedDir[0])
            
        
                        
    def GetValueFromMyTag(self,tagName,workbookName):
        for myTag in self.myTags:
            if myTag.tagName == tagName:
                for i , wbName in enumerate(myTag.workbookNames):
                    if wbName.split(".")[0] == workbookName:
                        return myTag.tagValues[i]
        return "N/A"

    
    def DeleteOnProcess(self,list):
        if self._getExcel_ == True and self._getSheet_ == False:
            item = list.item(list.currentRow())
            n = item.text()
            for i, mwb in enumerate(self.myWorkbooks) :
                if mwb.workbookName == item.text():
                    self.myWorkbooks.pop(i)
                    list.takeItem(list.currentRow())
                    del item
                    return
            
        if self._getSheet_ == True and self._getData_ == False:
            curRow = list.currentRow()
            item = list.item(curRow)
            curText = item.text()[3:]
            #get parent workbook name
            getParent = False
            parentName = ""
            panRow = curRow-1
            while not getParent:
                if list.item(panRow).text()[:3] != "-->":
                    getParent = True
                    parentName = list.item(panRow).text()
                panRow -= 1

            for mwb in self.myWorkbooks:
                if mwb.workbookName == parentName:
                    for i, sn in enumerate(mwb.sheetNames):
                        if sn == curText:
                            mwb.sheets.pop(i)
                            mwb.sheetNames.pop(i)
                            list.takeItem(curRow)
                            return
        
    def ResetProcess(self,list,button):
        self._getExcel_ = False
        self._getSheet_ = False
        self._getData_ = False
        self._exportData_ = False
        self.myTags = []
        self.myWorkbooks = []
        self.wb = []
        list.clear()
        button.setStyleSheet(styles.buttonOnStart)
        button.setText("开始生成")




    #=========================================================================

    #=============================Helper Method=============================
    def GenerateTable(self,parent):
        table = QTableWidget(parent)
            
        #tagIns = _g.tagList[0]
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([""]+["名称","工作表","坐标","单位"])
            
        table.setStyleSheet(styles.TableStyleSheet)
        #table.setMinimumSize(QSize(364,123))
        #table.setMaximumSize(QSize(365,124))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        table.setColumnWidth(0,25)
        w = 75
        table.setColumnWidth(1,w+20)
        table.setColumnWidth(2,w+50)
        table.setColumnWidth(3,w-30)
        table.setColumnWidth(4,w-40)
        table.verticalHeader().setDefaultSectionSize(15)
        

        return table
    #===========================================================================
class MyWorkBook:
    def __init__(self,workbook,workbookName) -> None:
        self.workbook = workbook
        self.workbookName = workbookName
        self.workbookShortName = workbookName.split(".")[0]
        self.sheets = []
        self.sheetNames = []
class MyTag:
    def __init__(self,name) -> None:
        self.tagName = name
        self.tagValues = []
        self.workbookNames = []



