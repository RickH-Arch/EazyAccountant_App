from utils.DataManager import DataMgr
class WriteDataManager:
    def __init__(self) -> None:
        self.dataPath = "cache\\writeData.json"
        self.data = DataMgr.LoadData(self.dataPath)
        if self.data is None:
            self.data = StoreData()

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
        

    def RefreshJson(self):
        DataMgr.WriteData(self.data,self.dataPath)


class StoreData:
    def __init__(self) -> None:
        self.folderPaths = []
        self.writerGroups = []
        self.writerGroupNow = None
        self.writerGroups = []
        
class WriterGroup:
    def __init__(self,groupName) -> None:
        self.groupName = groupName
        self.writer = []

class Writer:
    def __init__(self,name) -> None:
        self.name = name
        self.chosen = False

        