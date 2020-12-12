import datetime
from tkinter import messagebox

def alert(msg):
    return messagebox.askokcancel("Typewriter", msg)

def info(msg):
    return messagebox.showinfo("Typewriter", msg)

def today():
    time = datetime.datetime.now()
    return time.strftime("%d-%m-%Y")