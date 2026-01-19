from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QLabel
class Title(QLabel):
    def __init__(self, text, color:str):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                font-size: 40px;
                margin:0px;
                padding:0px;
                color: """+color+""";
                font-weight:800;
                font-style: italic;
            }        
        """)

class H2(QLabel):
    def __init__(self, text, color:str):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                font-size: 32px;
                margin:0px;
                padding:0px;
                color: """+color+""";
                font-weight:800;
            }        
        """)

class H3(QLabel):
    def __init__(self, text, color:str):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                font-size: 24px;
                margin:0px;
                padding:0px;
                color: """+color+""";
                font-weight:800;
            }        
        """)

class P(QLabel):
    def __init__(self, text, color:str):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                margin:0px;
                padding:0px;
                color: """+color+""";
                font-weight:800;
            }        
        """)