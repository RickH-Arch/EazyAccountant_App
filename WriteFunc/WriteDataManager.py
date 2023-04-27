import json
import jsonpickle
from json import JSONEncoder

class WriteDataManager:
    def __init__(self) -> None:
        pass



class StoreData:
    def __init__(self) -> None:
        self.folderPaths = []
        
class WriterGroup:
    def __init__(self,groupName) -> None:
        self.groupName = groupName
        self.writer = []

class Writer:
    def __init__(self,name) -> None:
        self.name = name
        