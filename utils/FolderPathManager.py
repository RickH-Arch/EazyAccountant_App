from PySide6.QtWidgets import *

class FolderPathMgr:
    def __init__(self) -> None:
        pass

    def AddFolderPath(list) -> str:
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getExistingDirectory(mainWindow,"选择文件夹")
        return selectedDir
    
    def SelectExportFilePath():
        mainWindow = QMainWindow()
        fileDialog = QFileDialog(mainWindow)
        selectedDir = fileDialog.getSaveFileName(mainWindow,"导出","","Excel Files(*.xlsx)")
        return selectedDir