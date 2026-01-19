from components.button import Button
from components.dragdrop import DragDrop
from components.text import Title
from palette import Pallete
from PyQt5.QtCore import QSize, QRect, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QMainWindow, QDialog,  QMessageBox, QGraphicsBlurEffect
import sys
from dotenv import load_dotenv

def printHey():
        print(Pallete.primary)
class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("Image Hub")
        self.setMaximumSize(QSize(1000, 700))
        self.setMinimumSize(QSize(600, 420))
        # Sets starting position/size: X,Y, Width, Height
        self.setGeometry(500,200,1000,700)
        self.init_gui()
        self.setAcceptDrops(True)
        self.setStyleSheet("""
            QWidget {
                background-color: """+Pallete.primary+""";               
            }
        """)

        
    
    def init_gui(self):
        layout = QVBoxLayout()
        title = Title("Image Hub", "#FFFFFF" )
        dragDrop = DragDrop()
        anotherButton = Button("PRIMARY TEST", variant="primary",fn=printHey)
        
        layout.addWidget(title)
        layout.addWidget(dragDrop)
        layout.addWidget(anotherButton)   
        # Displays Everything
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        

load_dotenv()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()