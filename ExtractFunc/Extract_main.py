import json

class ExtractMain:
    def __init__(self):
        self.folderPaths = []
        self.keywords = []
        self.storeData = {
            "folderPaths":self.folderPaths,
            "keywords":self.keywords,
        }

    
    def AddFolderPath(self,path):
        if path not in self.folderPaths:
            self.folderPaths.append(path)
            return True
            self.RefreshJson()
        else:
            return False
        
    def DelFolderPath(self,pathin):
        index = 0
        for path in self.folderPaths:
            if path == pathin:
                self.folderPaths.pop(index)
            index += 1

    def AddKeyword(self,keyword):
        if keyword not in self.keywords:
            self.keywords.append(keyword)
            return True
        else:
            return False
        
    def DelKeyword(self,keyword):
        index = 0
        for w in self.keywords:
            if w == keyword:
                self.keywords.pop(index)
                return True
            index += 1
        return False
    
    def RefreshJson(self):
        with open('extractData.json','w') as f:
            json.dump(self.storeData,f)