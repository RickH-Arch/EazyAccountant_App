
import os
from openpyxl import load_workbook


class ExcelManager:
    def __init__(self) -> None:
        self.workbookCache = []
        self.workbookNameCache = []

    def GetExcelWorkBook(self,path,words):
        self.ResetCache()
        if isinstance(path,list):
            workbooks,names = self.LoadExcelWorkBookFromPaths(path,words)
        else:
            workbooks,names = self.LoadExcelWorkBookFromPath(path,words)
        return workbooks,names
    
    def GetSheetsFromWorkbook(self,workbook,keywords):
        sheets = []
        sheetNames = []
        sheet_names = workbook.sheetnames
        for sheetName in sheet_names:
            if len(keywords) != 0:
                get = False
                for keyword in keywords:
                    if self.AnalyzeFileName(sheetName,keyword):
                        get = True
                if get:
                    sheets.append(workbook[sheetName])
                    sheetNames.append(sheetName)
            else:
                sheets.append(workbook[sheetName])
                sheetNames.append(sheetName)
        return sheets,sheetNames
    
    
    def LoadExcelWorkBookFromPath(self,folder_path,file_keywords):
        
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file_name)
            if os.path.isdir(file_path):
                self.LoadExcelWorkBookFromPath(file_path,file_keywords)
            elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
                if len(file_keywords)!=0:
                    getKeyword = False
                    for w in file_keywords:
                        if self.AnalyzeFileName(file_name,w):
                            getKeyword = True
                    if file_name not in self.workbookNameCache and getKeyword:
                        workbook = load_workbook(file_path)
                        self.workbookCache.append(workbook)
                        self.workbookNameCache.append(file_name)
                elif file_name not in self.workbookNameCache:
                    workbook = load_workbook(file_path)
                    self.workbookCache.append(workbook)
                    self.workbookNameCache.append(file_name)

        return self.workbookCache,self.workbookNameCache

    
    def LoadExcelWorkBookFromPaths(self,paths,file_keywords):
        
        for path in paths:
            self.LoadExcelWorkBookFromPath(path,file_keywords)
        return self.workbookCache,self.workbookNameCache
    
    
    def ResetCache(self):
        self.workbookCache.clear()
        self.workbookNameCache.clear()
    



    @classmethod
    def AnalyzeFileName(self,target_str,specific_str):
        ind = 0
        get = False
        start = False
        if '*' in specific_str:
            for i,w in enumerate(target_str) :
                if ind>=len(specific_str):
                    continue
                if specific_str[ind] == '*':
                    ind += 1
                    continue
                if w == specific_str[ind]:
                    start = True
                    get = True
                    ind += 1
                elif(start):
                    get = False
                    start = False
                    ind = 0
        elif specific_str in target_str:
            get = True
        return get



    
