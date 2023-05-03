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

writerRepoColNum = 4


class WriteMain:
    def __init__(self) -> None:
        self.dataMgr = WriteDataManager()

#-----------------------load function------------------------------

    def LoadFolderPath(self,list):
        paths = self.dataMgr.data.folderPaths
        for p in paths:
            list.addItem(QListWidgetItem(p))

    def LoadWriterGroup(self,cBox,grid,btn):
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


    def SwitchWriterGroup(self,cBox,renameBtn,grid):
        curText = cBox.currentText()
        if self.dataMgr.SwitchWriterGroup(curText):
            if curText == "全部写入组":
                renameBtn.setStyleSheet(styles.btn_Disable)
                self.GridShowAll(cBox,grid)
            else:
                renameBtn.setStyleSheet(styles.btn_Enable)
                renameBtn.setCheckable(True)
                self.RefreshGrid(cBox,grid)

    def AddWriterGroup(self,cBox,grid):
        name, ok = QInputDialog.getText(cBox, "添加写入组", "新写入组名称:")
        if ok:
            if self.dataMgr.AddWriterGroup(name):
                cBox.addItem(name)
                cBox.setCurrentText(name)
            else:
                QMessageBox.warning(self, "警告", "写入组名称已存在")
                return
        else:
            return
        
        self.RefreshGrid(cBox,grid)
        

    def RefreshGrid(self,cBox,grid):
        self.clearLayout(grid)
        groupNow = cBox.currentText()
        g = self.dataMgr.GetWriterGroup(groupNow)
        for i,w in enumerate(g.writers) :
            cord = divmod(i,writerRepoColNum)
            w,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid)
            grid.addWidget(w,cord[0],cord[1],1,1)
        addW,btns = self.GenerateAddWriterBox(grid.parent(),cBox,grid)
        cord = divmod(len(g.writers),writerRepoColNum)
        grid.addWidget(addW,cord[0],cord[1],1,1)
        if len(g.writers)+1<=4:
            vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
            grid.addItem(vSpacer,1,1,1,1)
        if len(g.writers)+1<4:
            hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
            grid.addItem(hSpacer,0,len(g.writers)+1,1,1)

    def GridShowAll(self,cBox,grid):
        self.clearLayout(grid)
        num = 0
        for g in self.dataMgr.data.writerGroups:
            for w in g.writers:
                cord = divmod(num,writerRepoColNum)
                w,btns = self.GenerateWriterBox(w.name,grid.parent(),cBox,grid)
                grid.addWidget(w,cord[0],cord[1],1,1)
                num+=1
        if num+1<=4:
            vSpacer = QSpacerItem(20,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
            grid.addItem(vSpacer,1,1,1,1)
        if num+1<4:
            hSpacer = QSpacerItem(40,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
            grid.addItem(hSpacer,0,len(g.writers)+1,1,1)




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
                QMessageBox.warning(self, "警告", "写入组名称已存在")
                return

    def AddWriter(self,cBox,repoGrid):
        
        groupNow = cBox.currentText()
        if groupNow == "全部写入组":
            return
        numNow,name = self.dataMgr.AddWriter(groupNow,"新写入")
        self.RefreshGrid(cBox,repoGrid)
        
            


    def DeleteWriter(self,cBox,name,grid):
        curGroup = cBox.currentText()
        if self.dataMgr.DeleteWriter(curGroup,name):
            self.RefreshGrid(cBox,grid)

    def CopyWriter(self,cBox,name,grid):
        curGroup = cBox.currentText()
        if self.dataMgr.CopyWriter(curGroup,name):
            self.RefreshGrid(cBox,grid)

    def EditWriter(self,name):
        print("edit writer:",name)
        #TODO:finish edit function

    
            

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

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
            

    def GenerateWriterBox(self,writerName,uiParent,cBox,grid):
        w = QWidget(uiParent)
        w.setObjectName(writerName)
        w.setMinimumSize(QSize(110, 110))
        w.setMaximumSize(QSize(110, 110))
        w.setStyleSheet(styles.write_writerBox)

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
        
        btn_writer_edit = QPushButton(frame1)
        btn_writer_edit.setObjectName(u"btn_writer_edit")
        btn_writer_edit.setMinimumSize(QSize(32, 20))
        btn_writer_edit.setMaximumSize(QSize(20, 20))
        btn_writer_edit.setStyleSheet(styles.write_btn_editWriter)
        btn_writer_edit.setText("编辑")

        hLayout1.addWidget(btn_writer_edit, 0, Qt.AlignLeft)

        btn_writer_copy = QPushButton(frame1)
        btn_writer_copy.setObjectName(u"btn_writer_copy")
        btn_writer_copy.setMinimumSize(QSize(20, 20))
        btn_writer_copy.setMaximumSize(QSize(20, 20))
        btn_writer_copy.setStyleSheet(styles.write_btn_editWriter)
        copyIcon = QIcon()
        copyIcon.addFile(u":/icons/icon/\u590d\u5236.ico", QSize(), QIcon.Normal, QIcon.Off)
        btn_writer_copy.setIcon(copyIcon)
        btn_writer_copy.clicked.connect(lambda:self.CopyWriter(cBox,btn_writer_delete.parent().parent().objectName(),grid))

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

        btn_writer_name = QPushButton(w)
        btn_writer_name.setObjectName(u"btn_writer_name")
        btn_writer_name.setMinimumSize(QSize(0, 39))
        font3 = QFont()
        font3.setBold(True)
        btn_writer_name.setFont(font3)
        btn_writer_name.setText(writerName)
        btn_writer_name.setStyleSheet(styles.write_btn_writerName)

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
    





    
    

        
        