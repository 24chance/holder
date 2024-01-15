# this is a real simple journal come on

import tkinter as tk
from tkinter import scrolledtext
import os

app = tk.Tk()
app.title("EON")
app.geometry("800x380")
app.config(bg='#fff')

text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=20)
text_area.pack(padx=10, pady=10)
text_area.configure(bg="white", fg="black")

content_file = "contOfTheContent_24.txt"

def load_content_at_startup():
    global content_file
    if os.path.exists(content_file) and os.path.isfile(content_file):
        with open(content_file, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

load_content_at_startup()

def save_file():
    global content_file
    if content_file:
        with open(content_file, 'w') as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)

def set_dark_mode():
    app.configure(bg="#000")  # Set background color to dark gray
    text_area.configure(bg="#000", fg="white")

# set_dark_mode()


def set_theme(theme):
    if theme == "dark":
        app.configure(bg="#2E2E2E")  # Set background color to dark gray
        text_area.configure(bg="#2E2E2E", fg="white")  # Set text area background to dark gray and text color to white
    else:
        app.configure(bg="white")  # Set background color to white
        text_area.configure(bg="white", fg="black")  # Set text area background to white and text color to black

def toggle_theme():
    current_theme = app.option_get('theme', 'light')
    new_theme = 'dark' if current_theme == 'light' else 'light'
    app.tk_setPalette(background='#2E2E2E', foreground='white') if new_theme == 'dark' else app.tk_setPalette(background='white', foreground='black')
    set_theme(new_theme)
    app.option_add('*TButton*highlightBackground', '#2E2E2E' if new_theme == 'dark' else 'white')

file_menu = tk.Menu(app, tearoff=0)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Dark Mode", command=set_dark_mode)
file_menu.add_command(label="Light Theme", command=toggle_theme)
file_menu.add_command(label="Exit", command=app.destroy)



app.config(menu=file_menu)

app.mainloop()
