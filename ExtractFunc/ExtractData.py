import json

from ExtractFunc.Tags import *

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


    #=================
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
    


    #Json refresh
    def RefreshJson(self):
        
        with open('extractData.json','w') as f:
            json.dump(self.storeData,f,indent = 4)



  