TableStyleSheet = '''*{background-color: rgb(255, 255, 255);\n
border-radius:10px;}\n
QTableWidget::item:selected{background-color:#bcb5e3}\n
QTableWidget::indicator:checked { background-color: #bcb5e3 ;
border-radius:3px}\n
QTableWidget::indicator:unchecked { background-color: white;
border-radius:3px;
border:1px solid lightgray;}\n

QScrollBar {              \n
            border: none;\n
            background:white;\n
            width:3px;\n
            margin: 0px 0px 0px 0px;\n
        }\n
        QScrollBar::handle {\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n
            min-height: 0px;\n
        }\n
        QScrollBar::add-line{\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n
            height: 0px;\n
            subcontrol-position: bottom;\n
            subcontrol-origin: margin;\n
        }\n
        QScrollBar::sub-line {\n
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n
         stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n
           height: 0 px;\n
            subcontrol-position: top;\n
          subcontrol-origin: margin;\n
        }\n'''

buttonEnable = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(255, 255, 255);
	
	background-color:rgb(81, 66, 147) ;
}

*:hover{
	
	background-color: rgb(255, 179, 54);
}
QPushButton:pressed{
	
	background-color: rgb(235, 159, 34);
}
'''

buttonDisable = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(255, 255, 255);
	background-color:lightgray ;
}


'''

buttonOnProcess = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(90,90,90);
	background-color:rgb(195, 241, 121) ;
}

*:hover{
	background-color: rgb(255, 179, 54);
}
'''

buttonOnStart = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(255,255,255);
	background-color:rgb(81, 66, 147) ;
}

*:hover{
	background-color: rgb(255, 179, 54);
}
'''