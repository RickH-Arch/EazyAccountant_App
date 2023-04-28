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
        self.writer = []

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

        