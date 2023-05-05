extract_Table = '''*{background-color: rgb(255, 255, 255);\n
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

btn_Enable = '''
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

btn_Disable = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(255, 255, 255);
	background-color:lightgray ;
}


'''

btn_OnProcess = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(90,90,90);
	background-color:rgb(195, 241, 121) ;
}

*:hover{
	background-color: rgb(255, 179, 54);
}
'''

btn_OnStart = '''
*{border-radius:5px;
	font-size:12px;
	color: rgb(255,255,255);
	background-color:rgb(81, 66, 147) ;
}

*:hover{
	background-color: rgb(255, 179, 54);
}
'''



write_writerBox = '''
*{
background-color: rgb(249, 246, 255);
border:1px solid rgb(239, 239, 248);
border-radius:10px;
}

QPushButton{
	background-color: rgb(227, 216, 255);
border-radius:10px;
	color: rgb(255, 255, 255);
}

QPushButton:hover{
	
	background-color: rgb(255, 179, 54);
}
QPushButton:pressed{
	
	background-color: rgb(235, 159, 34);
}
'''

write_writerBox_selected = '''
*{
background-color: rgb(249, 246, 255);
border:2px solid rgb(212, 189, 248);
border-radius:10px;
}

QPushButton{
	background-color: rgb(227, 216, 255);
border-radius:10px;
	color: rgb(255, 255, 255);
}

QPushButton:hover{
	
	background-color: rgb(255, 179, 54);
}
QPushButton:pressed{
	
	background-color: rgb(235, 159, 34);
}
'''

write_btn_editWriter = '''
*{background-color:rgb(230, 230, 230);
}
QPushButton:hover{
	
	background-color: rgb(255, 179, 54);
}

QPushButton:pressed{
	
	background-color: rgb(235, 159, 34);
}
'''

write_btn_deleteWriter = '''
*{background-color:rgb(243, 165, 166);}
*:hover{
	
	background-color: rgb(223, 145, 146);
}

*:pressed{
background-color: rgb(203, 125, 126);
}
'''

write_btn_writerName = '''
color:rgb(72, 72, 72);
background-color:rgb(249, 246, 255);
border:none;
'''
def EditorName(name):
    return u'''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: "\2610"; }
li.checked::marker { content: "\2612"; }
</style></head><body style=" font-family:'Microsoft YaHei UI'; font-size:15px; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:700;">'''+name+u'''</span></p></body></html>
    '''
    

def KeyName(name):
    return '''<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n
p, li { white-space: pre-wrap; }\n
hr { height: 1px; border-width: 0; }\n
li.unchecked::marker { content: \"\\2610\"; }\n
li.checked::marker { content: \"\\2612\"; }\n
</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11px; font-weight:400; font-style:normal;\">\n
<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">'''+name+"</span></p></body></html>"