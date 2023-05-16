from PySide6.QtWidgets import *

class PathMgr:
    def __init__(self) -> None:
        pass

    def AddFolderPath() -> str:
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getExistingDirectory(mainWindow,"选择文件夹")
        return selectedDir
    
    def SelectExportFilePath():
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getSaveFileName(mainWindow,"导出","","Excel Files(*.xlsx)")
        return selectedDir
    
    def SelectExcelFile():
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        path,_ = fileDialog.getOpenFileName(mainWindow,"选择输入表格","","Excel Files(*.xlsx)")
        return path