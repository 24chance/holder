# This is a simple audio AudioPlayer

import tkinter as tk
from tkinter import filedialog
import pygame

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Player")

        self.file_path = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Audio File:").pack()
        tk.Entry(self.root, textvariable=self.file_path, width=50).pack()

        tk.Button(self.root, text="Browse", command=self.browse_file).pack()
        tk.Button(self.root, text="Play", command=self.play_audio).pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav;")])
        self.file_path.set(file_path)

    def play_audio(self):
        file_path = self.file_path.get()
        if file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioPlayer(root)
    root.mainloop()
