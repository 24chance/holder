import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import os
import mysql.connector


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("EON")
window.setFixedWidth(700)
window.setFixedHeight(300)
window.setStyleSheet("background: #111;")

layout = QGridLayout()

# global widget dictionary
widgets = {
    "textArea": [],
    "saveBtn": [],
    "clearBtn": [],
    "exitBtn": [],
    "header": [],
    "username": [],
    "password": [],
    "login_button": []
}
content_file = "contOfTheContent_24.txt"

# functions

def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_error(title, message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStyleSheet(
        "background: #111;" +
        "color: #aaa;" +
        "font-size: 20px;"
    )
    msg_box.exec_()


def show_warning(title, message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStyleSheet(
        "background: #111;" +
        "color: #aaa;" +
        "font-size: 20px;"
    )
    msg_box.exec_()


def frame1():

    # functions

    def create_buttons(cont, func, wName):
        button = QPushButton(cont)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(
            "*{background: #0a0a0a;" +
            "border: 1px solid #fff;" +
            "color: #aaa;" +
            "font-size: 15px;" +
            "font-family: Verdana;" +
            "margin: 10px;" +
            "padding: 7px;}" +
            "*:hover{background: #000;"
            "color: #fff}"
        )
        button.clicked.connect(func)
        widgets[wName].append(button)
    

    def load_content_at_startup():
        if os.path.exists(content_file) and os.path.isfile(content_file):
            with open(content_file, 'r') as file:
                content = file.read()
                textArea.setText(content)
                cursor = textArea.textCursor()
                cursor.movePosition(cursor.End)
                textArea.setTextCursor(cursor)


    def save_file( ):
        if os.path.exists(content_file) and os.path.isfile(content_file):
            with open(content_file, 'w') as file:
                text_content = textArea.toPlainText()
                file.write(text_content)
        else:
            with open(content_file, 'w') as file:
                text_content = textArea.toPlainText()
                file.write(text_content)

    def clear_textArea():
        textArea.setText("")
        textArea.setFocus()

    def exit():
        sys.exit()


    # widgets
        
    textArea = QTextEdit()
    textArea.setPlaceholderText("Type your shit here!")
    textArea.setStyleSheet(
        "*{background: #0a0a0a;" +
        "border: 1px solid #fff;" +
        "color: #aaa;" +
        "font-size: 15px;" +
        "font-family: Verdana;" +
        "margin: 10px;" +
        "padding: 10px;}" +
        "*:focus{background: #000}"
    )
    textArea = textArea
    widgets["textArea"].append(textArea)


    create_buttons("Save", save_file, "saveBtn")
    create_buttons("Clear", clear_textArea, "clearBtn")
    create_buttons("Exit", exit, "exitBtn")
    
    layout.addWidget(widgets["textArea"][-1], 0, 0, 1, 3)
    layout.addWidget(widgets["saveBtn"][-1], 1, 0)
    layout.addWidget(widgets["clearBtn"][-1], 1, 1)
    layout.addWidget(widgets["exitBtn"][-1], 1, 2)

    load_content_at_startup()

    return textArea
    

def frame0():

    # functions


    def login():

        conn = mysql.connector.connect(
                host="localhost", 
                user="none", 
                password="i want in",
                database="test"
        )
        if conn:
            
            uname = username.text().strip()
            pwd = password.text()



        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_table WHERE uname= %s AND password= %s", (uname, pwd))
        res = cursor.fetchall()

        if uname == "" or pwd == "":
            show_warning("Really?", "Both of this shit can't be empty")
        else:
            if res:
                clear_widgets()
                frame1()
            else:
                show_error("Bruuh?", "C'mon, enter the real deal!")

        cursor.close()
        conn.close()




    def create_inputs(placeholder, wName):
        input = QLineEdit()
        input.setPlaceholderText(placeholder)
        input.setStyleSheet(
            "*{background: #0a0a0a;" +
            "border: 1px solid #fff;" +
            "height: 30px;" +
            "color: #aaa;" +
            "font-size: 15px;" +
            "font-family: Verdana;" +
            "margin: 10px;" +
            "padding: 7px;" +
            "color: #fff;}"
        )
        widgets[wName].append(input)
        return input
    


    # widgets

    header = QLabel("ONLY WAY IN!")
    header.setAlignment(QtCore.Qt.AlignCenter)
    header.setStyleSheet(
        "color: #fff;" +
        "font-size: 25px;" +
        "font-family: Shanti;" +
        "margin: 10px;" +
        "padding: 7px;"
    )
    widgets["header"].append(header)
    
    username = create_inputs("Username bruuh?", "username")
    password = create_inputs("And that password?", "password")
    password.setEchoMode(QLineEdit.Password)


    login_button = QPushButton("GET IN")
    login_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    login_button.setStyleSheet(
        "*{background: #0a0a0a;" +
        "border: 1px solid #fff;" +
        "color: #fff;" +
        "font-size: 15px;" +
        "font-family: Verdana;" +
        "margin: 10px;" +
        "padding: 7px;}" +
        "*:hover{background: #000;"
        "color: #fff}"
    )
    login_button.clicked.connect(login)
    widgets["login_button"].append(login_button)

    
    
    
    layout.addWidget(widgets["header"][-1], 0, 0)
    layout.addWidget(widgets["username"][-1], 1, 0)
    layout.addWidget(widgets["password"][-1], 2, 0)
    layout.addWidget(widgets["login_button"][-1], 3, 0)

    username.returnPressed.connect(login)
    password.returnPressed.connect(login)
    

frame0()



window.setLayout(layout)

window.show()
sys.exit(app.exec())