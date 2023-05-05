from utils.DataManager import DataMgr
import copy
class WriteDataManager:
    def __init__(self) -> None:
        self.dataPath = "cache\\writeData.json"
        self.data = DataMgr.LoadData(self.dataPath)
        if self.data is None:
            self.data = StoreData()
            self.RefreshJson()

    #=======================data change=============
    def AddFolderPath(self,path):
        if path == "":
            return
        if path not in self.data.folderPaths:
            self.data.folderPaths.append(path)
            self.RefreshJson()
            return True
        else:
            return False
        
    def DeleteFolderPath(self,pathin):
        if pathin == "":
            return False
        for i,path in enumerate(self.data.folderPaths):
            if path == pathin:
                self.data.folderPaths.pop(i)
                self.RefreshJson()
                return True
        return False
    
    def SwitchWriterGroup(self,curText):
        for i,g in enumerate(self.data.writerGroups):
            if g.groupName == curText:
                self.data.writerGroupNow = curText
                self.RefreshJson()
                return True
        return False
    
    def RenameWriterGroup(self,oldName,newName):
        for i,g in enumerate(self.data.writerGroups):
            if g.groupName == oldName:
                g.groupName = newName
                for w in g.writers:
                    w.parent = newName
                self.data.writerGroupNow = newName
                self.RefreshJson()
                return True
        return False
    
    def AddWriterGroup(self,name):
        for g in self.data.writerGroups:
            if g.groupName == name:
                return False
            
        newGroup = WriterGroup(name)
        newGroup.writers.append(Writer("新写入",name))
        self.data.writerGroups.append(newGroup)
        
        self.data.writerGroupNow = name

        self.RefreshJson()
        return True
    
    def GetWriterGroup(self,name):
        for g in self.data.writerGroups:
            if g.groupName == name:
                return g
        return None
    
    def GetWriter(self,groupName,name):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                for w in g.writers:
                    if w.name == name:
                        return w
        return None
    
    def DeleteWriterGroup(self,name):
        groupNum = len(self.data.writerGroups)
        if groupNum<2:
            return
        if name == "全部写入组":
            return
        for i,g in enumerate(self.data.writerGroups):
            if g.groupName == name:
                self.data.writerGroups.pop(i)
                groupNum-=1
                ind = (groupNum + i-1)%groupNum
                self.data.writerGroupNow = self.data.writerGroups[ind]
                return True
        return False

            
    
    def AddWriter(self,groupName,name = "新写入"):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                num = 0
                ind = 0
                for w in g.writers:
                    if w.name[:len(name)] == name:
                        if len(w.name)>len(name):
                            try:
                                curInd = int(w.name[len(name)])
                            except:
                                curInd = 0
                            if curInd>ind:
                                ind = curInd
                        num+=1
                if num >0 and num<ind+1:
                    name = name + str(ind+1)
                elif num>0:
                    name = name+str(num)
                
                    
                newWriter = Writer(name,groupName)
                g.writers.append(newWriter)
                self.RefreshJson()
                return len(g.writers),name+str(num)
        return 0,""
    
    def DeleteWriter(self,groupName,name):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                for i,w in enumerate(g.writers):
                    if w.name == name:
                        g.writers.pop(i)
                        self.RefreshJson()
                        return True
        return False
    
    def CopyWriter(self,groupName,name):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                for i,w in enumerate(g.writers):
                    if w.name == name:
                        g.writers.insert(i+1,copy.deepcopy(w))
                        g.writers[i+1].name = g.writers[i+1].name+"_拷贝"
                        self.RefreshJson()
                        return True
        return False
    
    def SelectWriter(self,groupName,name):
        for g in self.data.writerGroups:
            for w in g.writers:
                if w.name == name and g.groupName == groupName:
                    w.selected = True
                else:
                    w.selected = False
        self.RefreshJson()
        
    def WriterMoveForward(self,groupName):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                for i,w in enumerate(g.writers):
                    if w.selected == True:
                        if i ==0:
                            return False
                        g.writers.insert(i-1,g.writers.pop(i))
                        self.RefreshJson()
                        return True
        return False
    
    def WriterMoveBackward(self,groupName):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                for i,w in enumerate(g.writers):
                    if w.selected == True:
                        if i ==len(g.writers):
                            return False
                        g.writers.insert(i+1,g.writers.pop(i))
                        self.RefreshJson()
                        return True
        return False
    
    def RenameWriter(self,groupName,oldName,newName):
        g = self.GetWriterGroup(groupName)
        for w in g.writers:
            if w.name == newName:
                return False
        w = self.GetWriter(groupName,oldName)
        if w is None:
            return False
        w.name = newName
        self.RefreshJson()
        return True
    
    def SwitchWriterRowCol(self,groupName,writerName,state):
        w = self.GetWriter(groupName,writerName)
        w.isRowProcess = state
        self.RefreshJson()

        

    def RefreshJson(self):
        DataMgr.WriteData(self.data,self.dataPath)

    



class StoreData:
    def __init__(self) -> None:
        self.folderPaths = []
        self.writerGroups = []
        self.InitWriterGroup()
        self.writerGroupNow = "新写入组"

    def InitWriterGroup(self):
        self.writerGroups.append(WriterGroup("新写入组"))
        

        
class WriterGroup:
    def __init__(self,groupName) -> None:
        self.groupName = groupName
        self.writers = []

class Writer:
    def __init__(self,name,parent) -> None:
        self.name = name
        self.selected = False
        
        self.parent = parent
        self.isRowProcess = True
        self.key_and_mode = True
        self.workbookNames = []
        self.sheetNames = []
        self.keyNames = []
        self.valueNames = []
        self.processes = []

class Process:
    def __init__(self,name) -> None:
        self.name = name
        self.reWrite = True
        self.processStr = ""

        