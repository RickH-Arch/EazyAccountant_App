import json
import jsonpickle
from json import JSONEncoder

class DataMgr:
    def __init__(self) -> None:
        pass
    def LoadData(Path):
        try: 
            with open(Path,"r") as f:
                return jsonpickle.decode(f.read())
        except FileNotFoundError:
            return None
        
    def WriteData(data,Path):
        d = jsonpickle.encode(data,unpicklable=True,indent = 4)
        with open(Path,"w") as f:
            f.write(d)
            