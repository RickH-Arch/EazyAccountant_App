import os
from ExcelFileFunc.ExcelLoader import ExcelLoader

class ExcelManager:
    def __init__(self) -> None:
        self.excelLoader = ExcelLoader()

    def GetExcelWorkBook(self,path):
        self.excelLoader.ResetCache()
        if isinstance(path,list):
            workbooks,names = self.excelLoader.LoadExcelWorkBookFromPaths(path)
            for n in names:
                print(n)
        else:
            self.excelLoader.LoadExcelWorkBookFromPath(path)