import sys, os, pygame
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton, QTimeEdit
from PyQt5 import QtCore


# Initialize the app 
app = QApplication(sys.argv)


# create the window
window = QWidget()
window.setWindowTitle('Simple Time App')
window.setGeometry(100, 100, 300, 150)  # Increased height for the button


# create the layout
layout = QGridLayout()


# global variables
alarm_time = QTime.currentTime()
audio_file = 'Marvels_ anthem.mp3' # This audio file must be in this same directory


# functions
def play_audio(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # Use -1 to play the audio indefinitely

def stop_audio():
    pygame.mixer.music.stop()
    pygame.mixer.quit()

def set_alarm_time():
    global alarm_time
    alarm_time = time_edit.time().toString()


def update_time():
    global central_widget, alarm_time
    currentTime = QTime.currentTime()
    time_text = currentTime.toString('hh:mm:ss')
    current_time.setText(time_text)

    if time_text == alarm_time:
        play_audio(audio_file)


# Widgets

# add current_time time title 
current_time_title = QLabel("TIME:")
current_time_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

# add current_time time on the screen
current_time = QLabel()
current_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

# Add a button to stop the audio playing
stop_button = QPushButton('Stop Alarm')
stop_button.clicked.connect(stop_audio)
layout.addWidget(stop_button, 2, 0,)  # Button spans two columns


# Add a button to set the alarm time
set_alarm_button = QPushButton('Set Alarm')
set_alarm_button.clicked.connect(set_alarm_time)
layout.addWidget(set_alarm_button, 2, 1,)


# add the widgets to the layout
layout.addWidget(current_time_title, 0, 0,)
layout.addWidget(current_time, 0, 1,)
layout.addWidget(QLabel('Set Alarm Time:'), 1, 0)
layout.addWidget(time_edit := QTimeEdit(), 1, 1)

# Setup timer to update the time every second
timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)

# Initial update of the time per second
update_time()

# add the layout to the window
window.setLayout(layout)


# run the f program
if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
