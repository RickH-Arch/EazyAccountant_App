import os
from openpyxl import load_workbook

class ExcelLoader:
    def __init__(self):
        self.workbookCache = []
        self.workbookNameCache = []
    
    
    def LoadExcelWorkBookFromPath(self,folder_path):
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file_name)
            if os.path.isdir(file_path):
                self.LoadExcelWorkBookFromPath(file_path)
            elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
                if file_name not in self.workbookNameCache:
                    workbook = load_workbook(file_path)
                    self.workbookCache.append(workbook)
                    self.workbookNameCache.append(file_name)
        return self.workbookCache,self.workbookNameCache

    
    def LoadExcelWorkBookFromPaths(self,paths):
        
        for path in paths:
            self.LoadExcelWorkBookFromPath(path)
        return self.workbookCache,self.workbookNameCache
    
    def ResetCache(self):
        self.workbookCache.clear()
        self.workbookNameCache.clear()
