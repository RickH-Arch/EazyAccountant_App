
from PySide6.QtCore import QTimer

class DoubleClickChecker:
    def __init__(self,event) -> None:
        self.click_timer = QTimer()
        self.click_timer.setSingleShot(True)
        self.click_timer.timeout.connect(self.Check)
        self.doubleClickFunc = event
        self.click_count = 0

    def DoubleClick(self):
        self.click_count+=1
        if not self.click_timer.isActive():
            self.click_timer.start(250)
         
    def Check(self):
        if self.click_count >= 2:
            self.doubleClickFunc()
        self.click_count = 0
