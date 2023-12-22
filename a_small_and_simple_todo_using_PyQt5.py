# A small and simple To-Do app 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget, QLineEdit, QPushButton, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

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

        # list of all the widgets
        self.list = QListWidget()
        self.list.itemClicked.connect(self.updateItem)
        self.list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list.customContextMenuRequested.connect(self.showContextMenu)

        # button to add the new task
        self.button = QPushButton("Add task")
        self.button.clicked.connect(self.addTask)  # Connect to the class method

        # add widgets to the layout
        layout.addWidget(self.input_task)
        layout.addWidget(self.list)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.show()

    # Define addTask as a method of the class
    def addTask(self):
        new_text = self.input_task.text()
        if new_text:
            selected_item = self.list.currentItem()

            if selected_item:
                # If an item is selected, update its text
                selected_item.setText("~ " + new_text)
                self.list.clearSelection()
            else:
                # If no item is selected, add a new item
                self.list.addItem("~ " + new_text)
    
            self.input_task.clear()
        self.input_task.setFocus()

    def updateItem(self, item):
        text = item.text()
        text = text[1:]
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
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyApplication()
    sys.exit(app.exec_())
