from palette import Pallete

from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QMainWindow, QDialog,  QMessageBox, QGraphicsBlurEffect



class DragDrop(QWidget):
    def __init__():
        super().__init__()
        
    



class Button(QPushButton):
    def __init__(self,text:str, variant:str, fn):
        super().__init__()
        self.setText(text)
        if(variant=="ghost"):
            # blur = QGraphicsBlurEffect()
            # # blur.setBlurRadius(2)
            # # self.setGraphicsEffect(blur)
            self.setAcceptDrops(True)
            self.setStyleSheet("""
                QPushButton {
                    background-color: """+Pallete.ghost+""";
                    border: 4px dashed """+Pallete.gray+""";
                    height: 300px;
                    width:200px;
                    font-weight:600;
                    color: #3363FF
                }        
                QPushButton:hover {
                    background-color: #76DAFF;            
                }
            """)
        elif(variant == "primary"):
            self.setStyleSheet("""
                QPushButton {
                    background-color: """+Pallete.white+""";
                    border-style:outset;
                    border-radius: 32px;
                    border-width: 2px;
                    padding: 8px;
                    color: #3363FF;
                } 
                QPushButton:hover {
                    background-color: #76DAFF;            
                }
                QPushButton:clicked{
                    background-color: #FF0000;
                }
            """)
        self.clicked.connect(fn)