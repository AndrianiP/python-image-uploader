from PyQt5.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent
from components.button import Button
from util.ssh_client import Client
from util.palette import Pallete
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy, QListWidget, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QDialog, QListWidgetItem, QGridLayout


#Break this into different Classes
class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.client = Client()
        self.filePaths = []
        
        layout = QVBoxLayout(self)
        self.dragDrop = DragDropArea()
        layout.addWidget(self.dragDrop)
        #Allows Drag and Drop box to take up max space
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        #Adds buttons
        buttonLayout = QHBoxLayout()
        self.uploadBtn = Button("Upload", variant="primary", fn=lambda:self.upload(self.filePaths))
        self.cancelBtn = Button("Cancel", variant="destructive", fn=lambda:self.clearUploadPaths())
        buttonLayout.addWidget(self.uploadBtn)
        buttonLayout.addWidget(self.cancelBtn)
        layout.addLayout(buttonLayout)
        
        #Adds File list on server
        self.serverList = ServerFileList()
        serverListLayout = QVBoxLayout()
        serverListLayout.addWidget(self.serverList)
        layout.addLayout(serverListLayout)
        
    # Uploads Files and Updates list of files on server
    def upload(self, filePaths):
        self.client.uploadFiles(filePaths)
        self.clearUploadPaths()
        self.serverList.updateFilelist()
        
    def clearUploadPaths(self):
        self.filePaths.clear()
        self.dragDrop.setText("Drag and Drop")
    
    # https://www.youtube.com/watch?v=mcT_bK1px_g
    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        if a0.mimeData().hasUrls():
            a0.accept()
        else:
            a0.ignore()
    def dragMoveEvent(self, a0: QDragMoveEvent) -> None:
        if a0.mimeData().hasUrls():
            a0.accept()
        else:
            a0.ignore()
    def dropEvent(self, a0: QDropEvent) -> None:
        if a0.mimeData().hasUrls() :
            a0.setDropAction(Qt.CopyAction)
            qPaths = a0.mimeData().urls()
            if(qPaths != []):
                for path in qPaths:
                    localPath = path.toLocalFile()
                    if("jpg" in localPath or "png" in localPath):
                        self.filePaths.append(localPath)
                    else:
                        # https://www.pythonguis.com/tutorials/pyqt-dialogs/
                        # Catches Error throws a small dialog box
                        alert = QDialog()
                        alertLayout = QVBoxLayout()
                        message = QLabel("Files must be .jpg or .png")
                        alertLayout.addWidget(message)
                        alert.setWindowTitle("Error")
                        alert.setLayout(alertLayout)
                        alert.exec()
                        a0.ignore()
                        
            self.dragDrop.setText("; ".join(self.filePaths))
            a0.accept()
        else:
            a0.ignore()
            
#Drag Drop Widget Text
# https://doc.qt.io/archives/qt-5.15/qlabel.html
class DragDropArea(QLabel):
    def __init__(self):
        super().__init__()

        self.setText("Drag and Drop")
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setStyleSheet("""
            QLabel {
                background-color: """+Pallete.ghost+""";
                border: 4px dashed """+Pallete.gray+""";
                height: 800px;
                width:200px;
                font-weight:600;
                color: #3363FF
            }        
            QLabel:hover {
                background-color: #76DAFF;            
            }
        """)

# Gets all files from the server and displays them in a list
class ServerFileList(QListWidget):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.updateFilelist()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setStyleSheet("""
            QListWidget {
                background-color: """+Pallete.white+""";
                border: 4px solid """+Pallete.gray+""";
                height: 600px;
                width:200px;
                font: 14px;
                font-weight:600;
                color: #3363FF
            }        
        """)
        
        self.itemPressed.connect(self.requestFile)
    #self.itemPressed.connect(self.client.downloadFiles)
    # Can only concatenate str no QLISTWIDGET ITEM so we go with the method below
    def requestFile(self, item: QListWidgetItem):
        self.client.downloadFiles(item.text())
        
    def updateFilelist(self):
        self.clear()
        self.filePaths = self.client.getServerFiles()
        for file in self.filePaths:
            item = QListWidgetItem(file)
            self.addItem(item)
