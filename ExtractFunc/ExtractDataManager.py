from utils.DataManager import DataMgr

class ExtractDataManager:
    def __init__(self):
        self.dataPath = "cache\\extractData.json"
        
        self.data = DataMgr.LoadData(self.dataPath)
        if self.data is None:
            self.data = StoreData()
            self.RefreshJson()


    #=================Data Change==============
    def AddFolderPath(self,path):
        if path == "":
            return
        if path not in self.data.folderPaths:
            self.data.folderPaths.append(path)
            self.RefreshJson()
            return True
            
        else:
            return False
        
    def DelFolderPath(self,pathin):
        if pathin == "":
            return False
        
        for i,path in enumerate(self.data.folderPaths):
            if path == pathin:
                self.data.folderPaths.pop(i)
                self.RefreshJson()
                return True
        return False
    
    def AddFileKeyword(self,keyword):
        if keyword not in self.data.file_keywords:
            self.data.file_keywords.append(keyword)
            self.RefreshJson()
            return True
        else:
            return False
        
    def ChangeFileKeyword(self,index,keyword):
        if keyword == "":
            return
        self.data.file_keywords[index] = keyword
        self.RefreshJson()

    def DelFileKeyword(self,keyword):
        for i,w in enumerate(self.data.file_keywords):
            if w == keyword:
                self.data.file_keywords.pop(i)
                self.RefreshJson()
                return True
        return False
            

    def AddKeyword(self,keyword):
        if keyword == "":
            return
        if keyword not in self.data.keywords:
            self.data.keywords.append(keyword)
            self.RefreshJson()
            return True
        else:
            return False
        
    def ChangeKeyword(self,index,keyword):
        if keyword == "":
            return False
        self.data.keywords[index] = keyword
        self.RefreshJson()
        
    def DelKeyword(self,keyword):
        if keyword == "":
            return False
        
        for i,w in enumerate(self.data.keywords):
            if w == keyword:
                self.data.keywords.pop(i)
                self.RefreshJson()
                return True
        return False
    
    def SetAvtiveGroup(self,index):
        self.data.activeGroup = index
        self.RefreshJson()

    def AddTagGroup(self,groupName):
        if groupName == "":
            return False
        for group in self.data.tagGroups:
            if groupName == group.groupName:
                return False
        self.data.tagGroups.append(TagGroup(groupName))
        self.RefreshJson()
        return True
    
    def RenameTagGroup(self,ind,newGroupName):
        if newGroupName == "":
            return False
        self.data.tagGroups[ind].groupName = newGroupName
        self.RefreshJson()
        return True
    
    def DelTagGroup(self,groupName):
        if groupName == "":
            return False
        for i, g in enumerate(self.data.tagGroups):
            if groupName == g.groupName:
                self.data.tagGroups.pop(i)
                self.RefreshJson()
                return True
        return False
    
    def AddTag(self,groupName,tagName):
        if tagName == "":
            return False
        for g in self.data.tagGroups:
            if g.groupName == groupName:
                for tag in g.tagList:
                    if tag.tagInfo["名称"] == tagName:
                        return False
                g.tagList.append(Tag(tagName))
                self.RefreshJson()
                return True
        return False
    
    def DelTag(self,groupName,tagName):
        if tagName == "":
            return False
        for g in self.data.tagGroups:
            if g.groupName == groupName:
                for i, tag in enumerate(g.tagList) :
                    if tag.tagInfo["名称"] == tagName:
                        g.tagList.pop(i)
                        self.RefreshJson()
                        return True
        return False
    
    def ChangeTagActivation(self,groupName,tagName,status):
        for g in self.data.tagGroups:
            if g.groupName == groupName:
                for tag in g.tagList:
                    if tag.tagInfo["名称"] == tagName:
                        tag.isActive = status
                        #print("set status:",groupName,"-",tagName,"-",status)
                        self.RefreshJson()
                        return True
        return False

    def ChangeTagInfo(self,groupName,tagIndex,infoName,value):
        for g in self.data.tagGroups:
            if g.groupName == groupName:
                tag = g.tagList[tagIndex] 
                tag.tagInfo[infoName] = value
                print("set info:",groupName,"-",tagIndex,"-",infoName,"-",value)
                self.RefreshJson()
                return True
        return False
    
    def SetRowFollow(self,status):
        self.data.followRow = status
        self.RefreshJson()

    def SetAutoArrange(self,status):
        self.data.autoArrange = status
        self.RefreshJson()
    
    
    #==========================================


    #Json refresh
    def RefreshJson(self):
        DataMgr.WriteData(self.data,self.dataPath)

class StoreData():
    def __init__(self) -> None:
        self.folderPaths = []
        self.file_keywords = []
        self.keywords = []
        self.tagGroups = []
        self.activeGroup = 0
        self.followRow = True
        self.autoArrange = True

        

class Tag():
    def __init__(self,name) -> None:
        self.tagInfo = {
            "名称":name,
            "工作表":"",
            "坐标":"",
            "单位":"",
        }
        self.isActive = True
        
        

    def SetTagName(self,tagName):
        if type(tagName) == str:
            self.tagInfo["名称"] = tagName

    def SetTagCellCord(self,cord):
        if type(cord) == str:
            self.tagInfo["坐标"] = cord

    def SetTagUnits(self,unit):
        if type(unit) == str:
            self.tagInfo["单位"] = unit

    def IsValid(self):
        return self.tagInfo["名称"]!="" and self.tagInfo["工作表"]!="" and self.tagInfo["坐标"]!= ""

class TagGroup():
    def __init__(self,groupName) -> None:
        #self.tagGroupInfo = {
        #    "groupName" : groupName,
        #    "tagList":[]
        #}
        self.groupName = groupName
        self.tagList = []
        
    
    def AddTag(self,tag):
        self.tagList.append(tag)

    def Rename(self,name):
        if type(name) == str:
         self.tagList = name
  