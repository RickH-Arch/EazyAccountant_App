import sys
import time

from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation,QEvent)
from PySide6.QtGui import *
    
from PySide6.QtWidgets import *
from .WriterEditor import WriterEditor

from utils.FolderPathManager import FolderPathMgr
from .WriteDataManager import WriteDataManager
import utils.styleSheets as styles



writerRepoColNum = 4




class WriteMain(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.dataMgr = WriteDataManager()
        self.cBox_cache = None
        self.grid_cache = None
        self.filter_cache = None

#-----------------------load function------------------------------

    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadWriterGroup(self,cBox,grid,btn):
        self.cBox_cache = cBox
        self.grid_cache = grid
        
        cBox.addItem("全部写入组")
        for g in self.dataMgr.data.writerGroups:
            cBox.addItem(g.groupName)
        cBox.setCurrentText(self.dataMgr.data.writerGroupNow)
        if self.dataMgr.data.writerGroupNow == "全部写入组":
            btn.setStyleSheet(styles.btn_Disable)
            btn.setCheckable(False)
            
        self.RefreshGrid(cBox,grid)


#-----------------------------------------------------
    def AddFolderPath(self,list):
        selectedDir = FolderPathMgr.AddFolderPath()
        if self.dataMgr.AddFolderPath(selectedDir):
            list.addItem(QListWidgetItem(selectedDir))

    def DeleteFolderPath(self,list):
        curItem_row = list.currentRow()
        item = list.item(curItem_row)
        if item is None:
            return
        if self.dataMgr.DeleteFolderPath(item.text()):
            list.takeItem(curItem_row)
            del item


    def SwitchWriterGroup(self,cBox,renameBtn,grid,textEdit):
        curText = cBox.currentText()
        msg = textEdit.toPlainText()
        
        if self.dataMgr.SwitchWriterGroup(curText):
            if curText == "全部写入组":
                renameBtn.setStyleSheet(styles.btn_Disable)
            
            else:
                renameBtn.setStyleSheet(styles.btn_Enable)
                renameBtn.setCheckable(True)
            if msg != "":
                self.GridShowFilted(cBox,grid,msg)
            else:
                self.RefreshGrid(cBox,grid)

    def AddWriterGroup(self,cBox,grid):
        name, ok = QInputDialog.getText(cBox, "添加写入组", "新写入组名称:")
        if ok:
            if self.dataMgr.AddWriterGroup(name):
                cBox.addItem(name)
                cBox.setCurrentText(name)
            else:
                QMessageBox.warning(cBox, "警告", "写入组名称已存在")
                return
        else:
            return
        
        self.RefreshGrid(cBox,grid)

    def DeleteWriterGroup(self,cBox,grid):
        curGroup = cBox.currentText()
        if self.dataMgr.DeleteWriterGroup(curGroup):
            index = cBox.findText(curGroup)
            if index >= 0:
                cBox.removeItem(index)
            cBox.setCurrentText(self.dataMgr.data.writerGroupNow)
            self.RefreshGrid(cBox,grid)
    
   



    def RenameWriterGroup(self,cBox):
        name = cBox.currentText()
        idx = cBox.currentIndex()
        if name == "全部写入组":
            return
        new_name, ok = QInputDialog.getText(cBox, "更换名称", "写入组名称:",text = name)
        if ok and new_name != "":
            if self.dataMgr.RenameWriterGroup(name,new_name):
                cBox.removeItem(idx)
                cBox.insertItem(idx,new_name)
                cBox.setCurrentText(new_name)
        elif new_name != "":
                QMessageBox.warning(cBox, "警告", "写入组名称已存在")
                return

    def AddWriter(self,cBox,repoGrid):
        
        groupNow = cBox.currentText()
        if groupNow == "全部写入组":
            return
        numNow,name = self.dataMgr.AddWriter(groupNow,"新写入")
        self.RefreshGrid(cBox,repoGrid)
        
            


    def DeleteWriter(self,cBox,name,grid):
        curGroup = cBox.currentText()
        if curGroup == "全部写入组":
            QMessageBox.warning(cBox, "警告", "请勿在全部写入组视图中进行删除操作")
        if self.dataMgr.DeleteWriter(curGroup,name):
            self.RefreshGrid(cBox,grid)

    def CopyWriter(self,cBox,name,grid):
        curGroup = cBox.currentText()
        if curGroup == "全部写入组":
            QMessageBox.warning(cBox, "警告", "请勿在全部写入组视图中进行复制操作")
        if self.dataMgr.CopyWriter(curGroup,name):
            self.RefreshGrid(cBox,grid)

    def RearrangeWriter(self,cBox,grid,forward = True):
        curGroup = cBox.currentText()
        if curGroup == "全部写入组":
            return
        if forward == True:
            if self.dataMgr.WriterMoveForward(curGroup):
                self.RefreshGrid(cBox,grid)
        else:
            if self.dataMgr.WriterMoveBackward(curGroup):
                self.RefreshGrid(cBox,grid)
            
    def FilterTextChange(self,textEdit,cBox,grid):
        if self.filter_cache is None:
            self.filter_cache = textEdit
        
        msg = textEdit.text()
        
        if "\n" in msg:
            msg = msg.replace('\n','')
            textEdit.setText(msg)
            cs = textEdit.textCursor()
            cs.movePosition(QTextCursor.End)
            textEdit.setTextCursor(cs)
        curGroup = cBox.currentText()
          
        if msg == "":
            self.RefreshGrid(cBox,grid)
        else:
            self.GridShowFilted(cBox,grid,msg)
        
    
    def SelectWriter(self,cBox,name,grid):
        #print(name," selected")
        curGroup = cBox.currentText()
        if curGroup == "全部写入组":
            return
        self.dataMgr.SelectWriter(curGroup,name)
        self.RefreshGrid(cBox,grid)
        


    def EditWriter(self,cBox,name):
        
        self.app = QApplication.instance()
        
        self.we = WriterEditor()
        curGroup = cBox.currentText()
        w = self.dataMgr.GetWriter(curGroup,name)
        self.writer_cache = w
        if w is None:
            return
        self.InitWriterEditor(w)
        
        self.we.show()
        

    def InitWriterEditor(self,writer):
        ui = self.we.ui
        ui.label_writerParent.setText(writer.parent)
        ui.line_writerName.setText(writer.name)
        ui.line_writerName.setObjectName(writer.name)
        self.we.ui.line_writerName.installEventFilter(self)
        

        ui.line_writerName.editingFinished.connect(lambda:self.RenameWriter(writer.parent,writer.name,ui.line_writerName.text()))
        
        if writer.isRowProcess == True:
            ui.checkBox_writerAsRow.setChecked(True)
        else:
            ui.checkBox_writerAsColumn.setChecked(True)

        ui.checkBox_writerAsRow.clicked.connect(lambda:self.SwitchRowColProcess(ui.checkBox_writerAsRow,ui.checkBox_writerAsColumn,True))
        ui.checkBox_writerAsColumn.clicked.connect(lambda:self.SwitchRowColProcess(ui.checkBox_writerAsRow,ui.checkBox_writerAsColumn,False))

        if writer.key_and_mode == True:
            ui.checkbox_key_and.setChecked(True)
        else:
            ui.checkbox_key_or.setChecked(True)

        for name in writer.workbookNames:
            ui.list_Writer_wbName.addItem(QListWidgetItem(name))

        for name in writer.sheetNames:
            ui.list_writer_sheetName.addItem(QListWidgetItem(name))

        self.RefreshKeyGrid(writer.keyNames,ui.label_writerParent.text(),ui.line_writerName.text(),ui.keyGrid)
        self.RefreshValueGrid(writer.valueNames,ui.label_writerParent.text(),ui.line_writerName.text(),ui.valueGrid)
        self.RefreshProcessGrid(writer.processes,ui.label_writerParent.text(),ui.line_writerName.text(),ui.processGrid)


    def eventFilter(self,obj,event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return:
                self.we.ui.line_writerName.clearFocus()
                return True
        return super().eventFilter(obj,event)
        
        
    def RenameWriter(self,groupName,oldWriterName,newWriterName):
        ui = self.we.ui
        writer = self.dataMgr.GetWriter(groupName,oldWriterName)
        if self.dataMgr.RenameWriter(groupName,oldWriterName,newWriterName):
            
            
            self.RefreshKeyGrid(writer.keyNames,ui.label_writerParent.text(),ui.line_writerName.text(),ui.keyGrid)
            self.RefreshValueGrid(writer.valueNames,ui.label_writerParent.text(),ui.line_writerName.text(),ui.valueGrid)
            self.RefreshProcessGrid(writer.processes,ui.label_writerParent.text(),ui.line_writerName.text(),ui.processGrid)

            
            try:
                filterStr = self.filter_cache.text()
            except:
                filterStr = ""
            if filterStr is None:
                self.RefreshGrid(self.cBox_cache,self.grid_cache)
            else:
                self.GridShowFilted(self.cBox_cache,self.grid_cache,filterStr)
        else:
            QMessageBox.warning(self, "警告", "该名称已在当前写入组中存在")
            ui.line_writerName.setText(writer.name)

    def SwitchRowColProcess(self,rowCheck,colCheck,state):
        self.dataMgr.SwitchWriterRowCol(self.cBox_cache.currentText(),self.writer_cache.name,state)
        if state == True:
            rowCheck.setChecked(True)
            colCheck.setChecked(False)
        else:
            rowCheck.setChecked(False)
            colCheck.setChecked(True)





        
    def RefreshKeyGrid(self,names,groupName,writerName,hGrid):
        self.clearLayout(hGrid)
        for name in names:
            box = self.GenerateKeyBox(name,groupName,writerName,hGrid)
            hGrid.addWidget(box)
        addBox = self.GenerateAddKeyBox(groupName,writerName,hGrid)
        hGrid.addWidget(addBox)
        if len(names)+1<5:
            hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            hGrid.addItem(hSpacer)

    def RefreshValueGrid(self,names,groupName,writerName,hGrid):
        self.clearLayout(hGrid)
        for name in names:
            box = self.GenerateValueBox(name,groupName,writerName,hGrid)
            hGrid.addWidget(box)
        addBox = self.GenerateAddValueBox(groupName,writerName,hGrid)
        hGrid.addWidget(addBox)
        if len(names)+1<5:
            hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            hGrid.addItem(hSpacer)

    def RefreshProcessGrid(self,processes,groupName,writerName,hGrid):
        self.clearLayout(hGrid)
        for process in processes:
            box = self.GenerateProcessBox(process,groupName,writerName,hGrid)
            hGrid.addWidget(box)
        addBox = self.GenerateAddProcessBox(groupName,writerName,hGrid)
        hGrid.addWidget(addBox)
        if len(processes)+1<5:
            hSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            hGrid.addItem(hSpacer)

        

        
        

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def GridShowFilted(self,cBox,grid,name):
        self.clearLayout(grid)

        if cBox.currentText() == "全部写入组" or cBox.currentIndex() == 0:
            
            num = 0
            for g in self.dataMgr.data.writerGroups:
                for w in g.writers:
                    if name not in w.name:
                        continue
                    cord = divmod(num,writerRepoColNum)
                    w,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid,parentName=w.parent)
                    
                    grid.addWidget(w,cord[0],cord[1],1,1)
                    num+=1
            if num<=writerRepoColNum:
                vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
                grid.addItem(vSpacer,1,1,1,1)
            if num<writerRepoColNum:
                hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
                grid.addItem(hSpacer,0,num+1,1,1)
        else:
            groupNow = cBox.currentText()
            g = self.dataMgr.GetWriterGroup(groupNow)
            num = 0
            for i,w in enumerate(g.writers) :
                if name not in w.name:
                    continue
                cord = divmod(num,writerRepoColNum)
                box,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid,w.selected)
                
                grid.addWidget(box,cord[0],cord[1],1,1)
                num+=1
            
            if num<=writerRepoColNum:
                vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
                grid.addItem(vSpacer,1,1,1,1)
            if num<writerRepoColNum:
                hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
                grid.addItem(hSpacer,0,len(g.writers)+1,1,1)

    def RefreshGrid(self,cBox,grid):
        if self.cBox_cache is None:
            self.cBox_cache = cBox
        if self.grid_cache is None:
            self.grid_cache = grid
        self.clearLayout(grid)

        if cBox.currentText() == "全部写入组" or cBox.currentIndex() == 0:
            
            num = 0
            for g in self.dataMgr.data.writerGroups:
                for w in g.writers:
                    cord = divmod(num,writerRepoColNum)
                    w,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid,parentName=w.parent)
                    
                    grid.addWidget(w,cord[0],cord[1],1,1)
                    num+=1
            if num<=writerRepoColNum:
                vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
                grid.addItem(vSpacer,1,1,1,1)
            if num<writerRepoColNum:
                hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
                grid.addItem(hSpacer,0,num+1,1,1)
        else:
            groupNow = cBox.currentText()
            g = self.dataMgr.GetWriterGroup(groupNow)
            for i,w in enumerate(g.writers) :
                cord = divmod(i,writerRepoColNum)
                box,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid,w.selected)
                
                grid.addWidget(box,cord[0],cord[1],1,1)
            addW,btns = self.GenerateAddWriterBox(grid.parent(),cBox,grid)
            cord = divmod(len(g.writers),writerRepoColNum)
            grid.addWidget(addW,cord[0],cord[1],1,1)
            if len(g.writers)+1<=writerRepoColNum:
                vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
                grid.addItem(vSpacer,1,1,1,1)
            if len(g.writers)+1<writerRepoColNum:
                hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
                grid.addItem(hSpacer,0,len(g.writers)+1,1,1)


    def GenerateAddWriterBox(self,uiParent,cBox,grid):
        frame_addWriter = QWidget(uiParent)
        frame_addWriter.setObjectName(u"frame_addWriter")
        frame_addWriter.setMinimumSize(QSize(110, 110))
        frame_addWriter.setMaximumSize(QSize(110, 110))
        frame_addWriter.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        verticalLayout_8 = QVBoxLayout(frame_addWriter)
        verticalLayout_8.setSpacing(0)
        verticalLayout_8.setObjectName(u"verticalLayout_8")
        verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        btn_writer_add = QPushButton(frame_addWriter)
        btn_writer_add.setObjectName(u"btn_writer_add")
        btn_writer_add.setMinimumSize(QSize(110, 110))
        btn_writer_add.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_add.setIcon(icon4)
        btn_writer_add.setIconSize(QSize(40, 40))
        btn_writer_add.clicked.connect(lambda:self.AddWriter(cBox,grid))

        verticalLayout_8.addWidget(btn_writer_add)
        return frame_addWriter,btn_writer_add
            

    def GenerateWriterBox(self,writerName,uiParent,cBox,grid,selected = False,parentName = None):
        w = QWidget(uiParent)
        w.setObjectName(writerName)
        w.setMinimumSize(QSize(110, 110))
        w.setMaximumSize(QSize(110, 110))
        if selected == False:
            w.setStyleSheet(styles.write_writerBox)
        else:
            w.setStyleSheet(styles.write_writerBox_selected)

        vLayout = QVBoxLayout(w)
        vLayout.setSpacing(3)
        vLayout.setObjectName(u"verticalLayout")
        vLayout.setContentsMargins(3, 3, 3, 3)

        frame1 = QFrame(w)
        frame1.setObjectName(u"frame")
        frame1.setMinimumSize(QSize(0, 26))
        frame1.setStyleSheet(u"border:none")
        frame1.setFrameShape(QFrame.StyledPanel)
        frame1.setFrameShadow(QFrame.Raised)

        hLayout1 = QHBoxLayout(frame1)
        hLayout1.setSpacing(0)
        hLayout1.setObjectName(u"horizontalLayout")
        hLayout1.setContentsMargins(4, 0, 4, 0)

        btn_writer_name = QPushButton(w)
        btn_writer_name.setObjectName(u"btn_writer_name")
        btn_writer_name.setMinimumSize(QSize(0, 39))
        font3 = QFont()
        font3.setBold(True)
        btn_writer_name.setFont(font3)
        if parentName is not None:
            btn_writer_name.setText("/"+parentName+"/"+"\n"+writerName)
        else:
            btn_writer_name.setText(writerName)
        btn_writer_name.setStyleSheet(styles.write_btn_writerName)
        btn_writer_name.clicked.connect(lambda:self.SelectWriter(cBox,btn_writer_delete.parent().parent().objectName(),grid))
        
        btn_writer_edit = QPushButton(frame1)
        btn_writer_edit.setObjectName(u"btn_writer_edit")
        btn_writer_edit.setMinimumSize(QSize(32, 20))
        btn_writer_edit.setMaximumSize(QSize(20, 20))
        btn_writer_edit.setStyleSheet(styles.write_btn_editWriter)
        btn_writer_edit.setText("编辑")
        btn_writer_edit.clicked.connect(lambda:(self.EditWriter(cBox,btn_writer_delete.parent().parent().objectName()),btn_writer_name.click()))

        hLayout1.addWidget(btn_writer_edit, 0, Qt.AlignLeft)

        btn_writer_copy = QPushButton(frame1)
        btn_writer_copy.setObjectName(u"btn_writer_copy")
        btn_writer_copy.setMinimumSize(QSize(20, 20))
        btn_writer_copy.setMaximumSize(QSize(20, 20))
        btn_writer_copy.setStyleSheet(styles.write_btn_editWriter)
        copyIcon = QIcon()
        copyIcon.addFile(u":/icons/icon/\u590d\u5236.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_copy.setIcon(copyIcon)
        btn_writer_copy.clicked.connect(lambda:(self.CopyWriter(cBox,btn_writer_delete.parent().parent().objectName(),grid),
                                                btn_writer_name.click()))

        hLayout1.addWidget(btn_writer_copy)

        btn_writer_delete = QPushButton(frame1)
        btn_writer_delete.setObjectName(u"btn_writer_delete")
        btn_writer_delete.setMinimumSize(QSize(20, 20))
        btn_writer_delete.setMaximumSize(QSize(20, 20))
        btn_writer_delete.setStyleSheet(styles.write_btn_deleteWriter)
        deleteIcon = QIcon()
        deleteIcon.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_delete.setIcon(deleteIcon)
        btn_writer_delete.clicked.connect(lambda:self.DeleteWriter(cBox,btn_writer_delete.parent().parent().objectName(),grid))

        hLayout1.addWidget(btn_writer_delete, 0, Qt.AlignRight)

        vLayout.addWidget(frame1)

        

        vLayout.addWidget(btn_writer_name)

        frame2 = QFrame(w)
        frame2.setObjectName(u"frame2")
        frame2.setMinimumSize(QSize(0, 37))
        frame2.setStyleSheet(u"border:none")
        frame2.setFrameShape(QFrame.StyledPanel)
        frame2.setFrameShadow(QFrame.Raised)

        hLayout2 = QHBoxLayout(frame2)
        hLayout2.setSpacing(0)
        hLayout2.setObjectName(u"horizontalLayout_9")
        hLayout2.setContentsMargins(0, 0, 0, 0)

        btn_writer_batchOpr = QPushButton(frame2)
        btn_writer_batchOpr.setObjectName(u"btn_writer_batchOpr")
        btn_writer_batchOpr.setMinimumSize(QSize(61, 29))
        btn_writer_batchOpr.setMaximumSize(QSize(30, 29))
        btn_writer_batchOpr.setText("批量运行")

        hLayout2.addWidget(btn_writer_batchOpr)

        btn_writer_opr = QPushButton(frame2)
        btn_writer_opr.setObjectName(u"btn_writer_opr")
        btn_writer_opr.setMinimumSize(QSize(35, 29))
        btn_writer_opr.setMaximumSize(QSize(30, 29))
        btn_writer_opr.setText("运行")

        hLayout2.addWidget(btn_writer_opr)

        vLayout.addWidget(frame2)

        return w,[btn_writer_name,btn_writer_edit,btn_writer_copy,btn_writer_delete,btn_writer_batchOpr,btn_writer_opr]
    

    def GenerateKeyBox(self,name,groupName,writerName,hGrid):
        keyBox = QWidget(hGrid.parent())
        keyBox.setObjectName(name)
        keyBox.setMinimumSize(QSize(90, 90))
        keyBox.setMaximumSize(QSize(75, 75))
        keyBox.setStyleSheet(u"*{\n"
"background-color: rgb(237, 234, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        vLayout = QVBoxLayout(keyBox)
        vLayout.setObjectName(u"verticalLayout_8")
        vLayout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame(keyBox)
        frame.setObjectName(u"frame_9")
        frame.setStyleSheet(u"border:none")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        btn_writer_deleteKey = QPushButton(keyBox)
        btn_writer_deleteKey.setObjectName(u"btn_writer_deleteKey")
        btn_writer_deleteKey.setGeometry(QRect(64, 4, 20, 20))
        btn_writer_deleteKey.setMinimumSize(QSize(20, 20))
        btn_writer_deleteKey.setMaximumSize(QSize(20, 20))
        btn_writer_deleteKey.setStyleSheet(u"*{background-color:rgb(231, 210, 255);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_deleteKey.setIcon(icon)

        vLayout.addWidget(frame)

        line_keyName = QLineEdit(keyBox)
        line_keyName.setObjectName(name)
        line_keyName.setMinimumSize(QSize(0, 55))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        line_keyName.setFont(font2)
        line_keyName.setStyleSheet(u"border:None;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        line_keyName.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        line_keyName.setText(name)

        vLayout.addWidget(line_keyName)

        return keyBox

    
    def GenerateAddKeyBox(self,groupName,writerName,hGrid):
        addKeyBox = QWidget(hGrid.parent())
        addKeyBox.setObjectName(u"writer_add_key")
        addKeyBox.setMinimumSize(QSize(90, 90))
        addKeyBox.setMaximumSize(QSize(75, 75))
        addKeyBox.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        horizontalLayout_7 = QHBoxLayout(addKeyBox)
        horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        btn_writer_addKey = QPushButton(addKeyBox)
        btn_writer_addKey.setObjectName(u"btn_writer_addKey")
        btn_writer_addKey.setMinimumSize(QSize(90, 90))
        btn_writer_addKey.setMaximumSize(QSize(90, 90))
        btn_writer_addKey.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_addKey.setIcon(icon3)
        btn_writer_addKey.setIconSize(QSize(30, 30))

        return addKeyBox


    def GenerateValueBox(self,name,groupName,writerName,hGrid):
        valueBox = QWidget(hGrid.parent())
        valueBox.setObjectName(name)
        valueBox.setMinimumSize(QSize(90, 90))
        valueBox.setMaximumSize(QSize(75, 75))
        valueBox.setStyleSheet(u"*{\n"
"background-color: rgb(221, 194, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        vLayout = QVBoxLayout(valueBox)
        vLayout.setObjectName(u"verticalLayout_9")
        vLayout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame(valueBox)
        frame.setObjectName(u"frame_9")
        frame.setStyleSheet(u"border:none")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        btn_writer_deleteValue = QPushButton(valueBox)
        btn_writer_deleteValue.setObjectName(u"btn_writer_deleteKey")
        btn_writer_deleteValue.setGeometry(QRect(64, 4, 20, 20))
        btn_writer_deleteValue.setMinimumSize(QSize(20, 20))
        btn_writer_deleteValue.setMaximumSize(QSize(20, 20))
        btn_writer_deleteValue.setStyleSheet(u"*{background-color:rgb(248, 248, 248);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_deleteValue.setIcon(icon)

        vLayout.addWidget(frame)

        line_valueName = QLineEdit(valueBox)
        line_valueName.setObjectName(name)
        line_valueName.setMinimumSize(QSize(0, 55))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        line_valueName.setFont(font2)
        line_valueName.setStyleSheet(u"border:None;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        line_valueName.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        line_valueName.setText(name)

        vLayout.addWidget(line_valueName)

        return valueBox


    def GenerateAddValueBox(self,groupName,writerName,hGrid):
        addValueBox = QWidget(hGrid.parent())
        addValueBox.setObjectName(u"writer_add_key")
        addValueBox.setMinimumSize(QSize(90, 90))
        addValueBox.setMaximumSize(QSize(75, 75))
        addValueBox.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        horizontalLayout_7 = QHBoxLayout(addValueBox)
        horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        btn_writer_addValue = QPushButton(addValueBox)
        btn_writer_addValue.setObjectName(u"btn_writer_addKey")
        btn_writer_addValue.setMinimumSize(QSize(90, 90))
        btn_writer_addValue.setMaximumSize(QSize(90, 90))
        btn_writer_addValue.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_addValue.setIcon(icon3)
        btn_writer_addValue.setIconSize(QSize(30, 30))

        return addValueBox

    
    def GenerateProcessBox(self,process,groupName,writerName,hGrid):
        processBox = QWidget(hGrid.parent())
        processBox.setObjectName(u"processBox")
        processBox.setMinimumSize(QSize(150, 210))
        processBox.setMaximumSize(QSize(110, 210))
        processBox.setStyleSheet(u"*{\n"
"background-color:rgb(110, 92, 194);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        vLayout = QVBoxLayout(processBox)
        vLayout.setSpacing(0)
        vLayout.setObjectName(u"verticalLayout_11")
        vLayout.setContentsMargins(5, 0, 5, 0)

        frame = QFrame(processBox)
        frame.setObjectName(u"frame_11")
        frame.setMinimumSize(QSize(0, 30))
        frame.setMaximumSize(QSize(16777215, 30))
        frame.setStyleSheet(u"border:none")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        horizontalLayout_5 = QHBoxLayout(frame)
        horizontalLayout_5.setSpacing(0)
        horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        btn_writer_deleteProcess = QPushButton(frame)
        btn_writer_deleteProcess.setObjectName(u"btn_writer_deleteProcess")
        btn_writer_deleteProcess.setMinimumSize(QSize(20, 20))
        btn_writer_deleteProcess.setMaximumSize(QSize(20, 20))
        btn_writer_deleteProcess.setStyleSheet(u"*{background-color:rgb(158, 132, 235);}\n"
"*:hover{\n"
"	\n"
"	background-color: rgb(223, 145, 146);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(203, 125, 126);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icon/\u5173\u95ed.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_deleteProcess.setIcon(icon)
    
        horizontalLayout_5.addWidget(btn_writer_deleteProcess, 0, Qt.AlignRight)
        
        vLayout.addWidget(frame)

        line_processName = QLineEdit(processBox)
        line_processName.setObjectName(u"line_processName")
        line_processName.setMinimumSize(QSize(0, 31))
        line_processName.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"font: 700 10pt \"Microsoft YaHei UI\";")
        line_processName.setAlignment(Qt.AlignCenter)
        line_processName.setText(process.name)

        vLayout.addWidget(line_processName)

        checkBox_writer_rewrite = QCheckBox(processBox)
        checkBox_writer_rewrite.setObjectName(u"checkBox_writer_rewrite")
        checkBox_writer_rewrite.setMinimumSize(QSize(0, 24))
        checkBox_writer_rewrite.setStyleSheet(u"QCheckBox{\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator {\n"
"    \n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: rgb(102, 86, 180)\n"
"}\n"
"\n"
"")
        checkBox_writer_rewrite.setChecked(process.reWrite)
        checkBox_writer_rewrite.setText("覆盖")

        vLayout.addWidget(checkBox_writer_rewrite,0,Qt.AlignHCenter)
        text_writer_process = QTextEdit(processBox)
        text_writer_process.setObjectName(u"text_writer_process")
        text_writer_process.setMinimumSize(QSize(0, 110))
        text_writer_process.setMaximumSize(QSize(16777215, 112))
        text_writer_process.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 9pt \"Microsoft YaHei UI\";")
        text_writer_process.setText(process.processStr)

        vLayout.addWidget(text_writer_process)

        return processBox
    

    def GenerateAddProcessBox(self,groupName,writerName,hGrid):
        addProcessBox = QWidget(hGrid.parent())
        addProcessBox.setObjectName(u"writer_addProcess")
        addProcessBox.setMinimumSize(QSize(150, 210))
        addProcessBox.setMaximumSize(QSize(150, 210))
        addProcessBox.setStyleSheet(u"*{\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid rgb(239, 239, 248);\n"
"border-radius:10px;\n"
"}\n"
"")
        hLayout = QHBoxLayout(addProcessBox)
        hLayout.setObjectName(u"horizontalLayout_11")
        hLayout.setContentsMargins(0, 0, 0, 0)
        btn_writer_addProcess = QPushButton(addProcessBox)
        btn_writer_addProcess.setObjectName(u"btn_writer_addProcess")
        btn_writer_addProcess.setMinimumSize(QSize(150, 210))
        btn_writer_addProcess.setMaximumSize(QSize(150, 210))
        btn_writer_addProcess.setStyleSheet(u"*:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"\n"
"*:pressed{\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"*{\n"
"border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_addProcess.setIcon(icon3)
        btn_writer_addProcess.setIconSize(QSize(30, 30))

        hLayout.addWidget(btn_writer_addProcess)

        return addProcessBox


