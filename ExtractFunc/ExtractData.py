import json

class ExtractDataManager:
    def __init__(self):
        #self.folderPaths = []
        #self.keywords = []
        self.storeData = {
            "folderPaths":[],
            "keywords":[],
            "TagGroups":[],
        }

        try:
            with open("extractData.json","r") as f:
                indata = json.load(f)
                self.storeData["folderPaths"] = indata["folderPaths"]
                self.storeData["keywords"] = indata["keywords"]
        except FileNotFoundError:
            pass


    #=================Data Change==============
    def AddFolderPath(self,path):
        if path == "":
            return
        if path not in self.storeData["folderPaths"]:
            self.storeData["folderPaths"].append(path)
            self.RefreshJson()
            return True
            
        else:
            return False
        
    def DelFolderPath(self,pathin):
        if pathin == "":
            return False
        
        for i,path in enumerate(self.storeData["folderPaths"]):
            if path == pathin:
                self.storeData["folderPaths"].pop(i)
                self.RefreshJson()
                return True
        return False
            

    def AddKeyword(self,keyword):
        if keyword == "":
            return
        if keyword not in self.storeData["keywords"]:
            self.storeData["keywords"].append(keyword)
            self.RefreshJson()
            return True
        else:
            return False
        
    def DelKeyword(self,keyword):
        if keyword == "":
            return False
        
        for i,w in enumerate(self.storeData["keywords"]):
            if w == keyword:
                self.storeData["keywords"].pop(i)
                self.RefreshJson()
                return True
        return False
    
    def AddTagGroup(self,groupName):
        if groupName == "":
            return False
        for group in self.storeData["TagGroups"]:
            if groupName == group.groupName:
                return False
        self.storeData["TagGroups"].append(TagGroup(groupName))
        self.RefreshJson()
        return True
    
    def RenameTagGroup(self,ind,newGroupName):
        if newGroupName == "":
            return False
        self.storeData["TagGroups"][ind].groupName = newGroupName
        self.RefreshJson()
        return True
    
    def DelTagGroup(self,groupName):
        if groupName == "":
            return False
        for i, g in enumerate(self.storeData["TagGroups"]):
            if groupName == g.groupName:
                self.storeData["TagGroup"].pop(i)
                self.RefreshJson()
                return True
        return False
    #==========================================


    #Json refresh
    def RefreshJson(self):
        
        with open('extractData.json','w') as f:
            json.dump(self.storeData,f,indent = 4)


class Tag:
    def __init__(self) -> None:
        self.info = {
            "名称":"",
            "坐标":"",
            "关键词":"",
            "单位":"",
        }
        self.isActivate = True
        

    def SetTagName(self,tagName):
        if type(tagName) == str:
            self.info["名称"] = tagName

    def SetTagCellCord(self,cord):
        if type(cord) == str:
            self.info["坐标"] = cord

    def SetTagUnits(self,unit):
        if type(unit) == str:
            self.info["单位"] = unit

class TagGroup:
    def __init__(self,groupName) -> None:
        self.groupName = groupName
        self.tagList = []
        
    
    def AddTag(self,tag):
        self.tagList.append(tag)

    def Rename(self,name):
        if type(name) == str:
         self.groupName = name
  