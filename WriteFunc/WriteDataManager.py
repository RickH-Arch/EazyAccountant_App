from utils.DataManager import DataMgr
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
                self.data.writerGroupNow = newName
                #self.RefreshJson()
                return True
        return False
    
    def AddWriterGroup(self,name):
        for g in self.data.writerGroups:
            if g.groupName == name:
                return False
            
        newGroup = WriterGroup(name)
        newGroup.writers.append(Writer("新写入"))
        self.data.writerGroups.append(newGroup)
        
        self.data.writerGroupNow = name

        self.RefreshJson()
        return True
    
    def GetWriterGroup(self,name):
        for g in self.data.writerGroups:
            if g.groupName == name:
                return g
        return None
    
    def AddWriter(self,groupName,name = "新写入"):
        for g in self.data.writerGroups:
            if g.groupName == groupName:
                num = 0
                for w in g.writers:
                    if w.name[:len(name)] == name:
                        num+=1
                if num >0:
                    newWriter = Writer(name+str(num))
                else:
                    newWriter = Writer(name)
                g.writers.append(newWriter)
                self.RefreshJson()
                return len(g.writers),name+str(num)
        return 0,""
                

        

    def RefreshJson(self):
        DataMgr.WriteData(self.data,self.dataPath)


class StoreData:
    def __init__(self) -> None:
        self.folderPaths = []

        self.writerGroups = []
        self.InitWriterGroup()
        self.writerGroupNow = "全部写入组"

    def InitWriterGroup(self):
        self.writerGroups.append(WriterGroup("全部写入组"))
        self.writerGroups.append(WriterGroup("新写入组"))
        

        
class WriterGroup:
    def __init__(self,groupName) -> None:
        self.groupName = groupName
        self.writers = []

class Writer:
    def __init__(self,name) -> None:
        self.name = name
        self.chosen = False
        self.isRowProcess = True
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

        