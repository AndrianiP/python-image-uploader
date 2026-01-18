from PyQt5.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent
from palette import Pallete
from PyQt5.QtGui import QDrag
from PyQt5.QtCore import QSize, QRect, Qt, QMimeData
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QMainWindow, QDialog,  QMessageBox, QGraphicsBlurEffect


class Button(QPushButton):
    def __init__(self,text:str, variant:str, fn):
        super().__init__()
        self.setText(text)
        if(variant == "primary"):
            self.setAcceptDrops(False)
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
                QPushButton:pressed{
                    background-color: """+Pallete.ghost+""";
                }
            """)
        elif(variant == "destructive"):
            self.setAcceptDrops(False)
            self.setStyleSheet("""
                QPushButton {
                    background-color: """+Pallete.destructive+""";
                    border-style:outset;
                    border-radius: 32px;
                    border-width: 2px;
                    padding: 8px;
                    color: #FFFFFF;
                } 
                QPushButton:hover {
                    background-color: #76DAFF;            
                }
                QPushButton:pressed{
                    background-color: """+Pallete.ghost+""";
                }
            """)
        #Function to run when clicked
        self.clicked.connect(fn)
