import sys
import threading
import socket
import json
from utils import english_to_french,french_to_english
from wiki import wikipedia_search
from PyQt5.QtCore import QSize,QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLineEdit,QLabel,QRadioButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.set_ui()
        self.set_event_listeners()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get local machine name
        self.host = socket.gethostbyname(socket.gethostname())
        self.my_port = 9999
        self.socket.connect((self.host,self.my_port))
    def set_ui(self):
        self.setWindowTitle("My App")
        self.setStyleSheet('background-color:#02203c;padding:5px;font-size:40px;')
        self.setFixedSize(QSize(1000,600))
        self.setWindowTitle('Sammy And Rabiaa Search Engine')
        self.label = QLabel(self)
        self.label.setGeometry(200,100,600,500)
        self.label.setStyleSheet('background-color:#161616;border-radius:20px;color:whitesmoke;font-size:20px;')
        self.label.setText('Results will be shown here.\nThank You.')
        self.line = QLineEdit(self)
        self.line.setText('Search...')
        self.line.setGeometry(150,30,700,100)
        self.line.setStyleSheet('background-color:royalblue;padding:20px;color:whitesmoke;border-radius:50;border:none;font-size:30px;text-align:center;')
        self.button = QPushButton("",self)
        self.button.setGeometry(790,60,50,50)
        self.button.setStyleSheet('background-color:#02203c;padding:10px;color:white;border:2px solid white;border-radius:25;font-size:35px;')
        self.clear_screen = QPushButton('clear',self)
        self.clear_screen.setGeometry(35,520,150,50)
        self.clear_screen.setStyleSheet('background-color:#02203c;border:1px solid white;border-radius:6px;color:whitesmoke;')
        self.exit_window = QPushButton('exit',self)
        self.exit_window.setGeometry(820,520,150,50)
        self.exit_window.setStyleSheet('background-color:#02203c;border:1px solid white;border-radius:6px;color:whitesmoke;')
        self.eng = QRadioButton(self)
        self.eng.setGeometry(20, 120, 100, 50)
        self.eng.setText('En')
        self.selected_language = 'en'
        self.eng.toggled.connect(self.english_selected)
        self.eng.setStyleSheet('background-color:whitesmoke;border:1px solid white;border-radius:6px;color:black;')
        self.fr = QRadioButton(self)
        self.fr.setGeometry(20, 200, 100, 50)
        self.fr.setText('Fr')
        self.fr.toggled.connect(self.french_selected)
        self.fr.setStyleSheet('background-color:whitesmoke;border:1px solid white;border-radius:6px;color:black;')
        # self.wrap = textwrap.TextWrapper(width=60)
    def english_selected(self, selected):
        if selected:
            if self.selected_language == 'fr':
                self.selected_language = 'en'
        print(self.selected_language)
    def french_selected(self, selected):
        if selected:
            if self.selected_language =='en':
                self.selected_language = 'fr'
        print(self.selected_language)
    def set_event_listeners(self):
           self.button.clicked.connect(self.display_result)
           self.clear_screen.clicked.connect(self.clear_the_screen)
           self.exit_window.clicked.connect(self.exit_window_handler)
    def display_result(self):
        text = self.line.text()
        search_value = text
        self.line.setText(text)
        lang = self.selected_language
        try:
            while search_value != text:
                pass
            m = dict(lang=lang,word=text)
            m = json.dumps(m)
            self.socket.sendall(bytes(m,encoding='utf-8'))
            data = self.socket.recv(1024).decode('utf-8')
            print(data)
            self.label.setText(data)
            search_value = None
            
            
            # if lang == 'en':
            #     msg = english_to_french(str(text))
            #     if msg != 'does not exist in this dictionary.':
            #         self.label.setText(msg)
            #     else:
            #         self.label.setText(wikipedia_search(text,'A'))
            # else:
            #     msg = french_to_english(str(text))
            #     if msg != 'n"existe pas dans cette dictionnaire.':
            #         self.label.setText(msg)
            #     else:
            #         self.label.setText(wikipedia_search(text,'B'))
                
        except :
            self.socket.close()
            self.label.setText('Nothing found.\nSearch for something else.')
    def clear_the_screen(self):
        self.label.setText('')
    def exit_window_handler(self):
        self.close()
        


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    sys.exit(app.exit())