# this is a simple recorder that says back what you just said

import speech_recognition as sr
import tkinter as tk
from threading import Thread
import pyttsx3
from tkinter import messagebox

class VoiceRecognitionApp:
    

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voice Recognition App")

        self.label = tk.Label(self.root, text="Click 'Start' to begin recording.")
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_recording)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.start_button = tk.Button(self.root, text="Say it", command=self.text_to_speech)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=5)

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.is_recording = False

    def start_recording(self):
        self.label.config(text="Recording...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_recording = True

        # Start a new thread for recording to avoid freezing the GUI
        Thread(target=self.record).start()

    def stop_recording(self):
        self.label.config(text="Click 'Start' to begin recording.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_recording = False

    def record(self):
        while self.is_recording:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio)

                # Save the recognized text to a file
                with open("output.txt", "w") as file:
                    file.write(text)

            except sr.UnknownValueError:
                print("Could not understand audio")

            except sr.RequestError as e:
                print(f"Error with the request to Google Web Speech API: {e}")

    def text_to_speech(self):
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        with open("output.txt", "r") as file:
            # Read the entire content of the file
            text = file.read()
        
        if text:
            # Set properties (optional)
            engine.setProperty("rate", 130)  # Speed of speech
            engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

            # Convert text to speech and play it
            engine.say(text)
            engine.runAndWait()
        else:
            messagebox.showerror("Error", "Please enter text in the Entry field.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VoiceRecognitionApp()
    app.run()
