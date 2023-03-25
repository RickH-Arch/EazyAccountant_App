class Tag:
    def __init__(self) -> None:
        self.name = ""
        self.cellCord = ""
        self.units = ""

    def SetTagName(self,tagName):
        if type(tagName) == str:
            self.name = tagName

    def SetTagCellCord(self,cord):
        if type(cord) == str:
            self.cellCord = cord

    def SetTagUnits(self,unit):
        if type(unit) == str:
            self.units = unit

class TagGroup:
    def __init__(self) -> None:
        self.groupName = "新标签组"
        self.tagList = []
        
    
    def AddTag(self,tag):
        self.tagList.append(tag)

    def Rename(self,name):
        if type(name) == str:
         self.groupName = name