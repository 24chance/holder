# A small and simple To-Do app with a checker for time of the task

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget, QLineEdit, QPushButton, QMenu, QTimeEdit, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTime, QTimer
import os

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        # the file that contains the content of the list 
        self.content_file = "contOfTheContent_24"

        self.initUI()

        # calling the function to display the tasks saved
        self.loadContent()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkTaskTime)
        self.timer.start(1000) 

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('To-Do')

        # Set the application icon
        icon = QIcon('eon_logo.ico')
        QApplication.setWindowIcon(icon)

        # create a layout
        layout = QGridLayout()

        # widgets
        # input to enter the new task
        self.input_task = QLineEdit()
        self.input_task.setPlaceholderText("Enter the new task")
        self.input_task.returnPressed.connect(self.addTask)

        # add time for the task 
        self.time_input = QTimeEdit()
        default_time = QTime(11, 11)
        self.time_input.setTime(default_time)
        self.time_input.editingFinished.connect(self.addTask)

        # list of all the widgets
        self.list = QListWidget()
        self.list.itemClicked.connect(self.updateItem)
        self.list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list.customContextMenuRequested.connect(self.showContextMenu)

        # button to add the new task
        self.button = QPushButton("Add task")
        self.button.clicked.connect(self.addTask)  # Connect to the class method

        # add widgets to the layout
        layout.addWidget(self.input_task, 0,0)
        layout.addWidget(self.time_input, 0,1)
        layout.addWidget(self.button, 1, 0, 1 ,2)
        layout.addWidget(self.list, 2, 0, 1, 2)

        self.setLayout(layout)
        self.show()

    # Define addTask as a method of the class
    def addTask(self):
        new_text = self.input_task.text()

        # Add the time to the listView

        self.time = self.time_input.time().toString()

        # Add the inputed task 
        if new_text:
            selected_item = self.list.currentItem()

            if selected_item:
                # If an item is selected, update its text
                selected_item.setText("~ " + new_text + "  ---->  (" + self.time +")")
                self.list.clearSelection()
                self.list.setCurrentItem(None)
            else:
                # If no item is selected, add a new item
                self.list.addItem("~ " + new_text + "  ---->  (" + self.time +")")
    
            self.input_task.clear()
        self.input_task.setFocus()
        self.saveContent()

    def updateItem(self, item):
        text = item.text()
        text = text[1:-19]
        self.input_task.setText(text)
        self.input_task.setFocus()

    def showContextMenu(self, pos):
        context_menu = QMenu(self)

        delete_action = context_menu.addAction("Delete")
        delete_action.triggered.connect(self.deleteSelectedItem)


        context_menu.exec_(self.list.mapToGlobal(pos))

    def deleteSelectedItem(self):
        selected_item = self.list.currentItem()
        if selected_item:
            self.list.takeItem(self.list.row(selected_item))
            self.input_task.clear()


    def saveContent(self):
        items = [self.list.item(i).text() for i in range(self.list.count())]

        with open(self.content_file, 'w') as file:
            text_content = "\n".join(items)
            file.write(text_content)
    
    
    
    def loadContent(self):
        if os.path.exists(self.content_file) and os.path.isfile(self.content_file):
            with open(self.content_file, 'r') as file:
                cont = file.read().splitlines()
                for task in cont:
                    self.list.addItem(QListWidgetItem(task))
    
    def checkTaskTime(self):
        currentTime = QTime.currentTime().toString()
        for i in range(self.list.count()):
            taskTime = self.list.item(i).text()[-9:-1]

            if taskTime == currentTime:
                task_text = self.list.item(i).text()[1:-19]
                self.showPopup("It's time for the task:\n{}".format(task_text))

    def showPopup(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Task")
        msgBox.exec_()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())
