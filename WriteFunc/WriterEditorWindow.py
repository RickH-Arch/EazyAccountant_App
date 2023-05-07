import sys
import os 
import platform
from typing import Optional


from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QPropertyAnimation,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget,QTextBrowser)
from PySide6.QtWidgets import *

from .WriterEditor_ui import Ui_WriterEditor

from WriteFunc.Write_main import *

class WriterEditor(QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.ui = Ui_WriterEditor()
        self.ui.setupUi(self)
        self.onDrag = False
        self.setWindowFlag(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,120))
        self.ui.writerEditor_mainWindow.setGraphicsEffect(self.shadow)

        self.setFixedHeight(925)
        self.setFixedWidth(690)

        self.ui.btn_close.clicked.connect(lambda:self.close())

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            if(event.position().y()<50 and event.position().x()>100):
                
                self.OnDrag = True
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if self.OnDrag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.OnDrag = False
