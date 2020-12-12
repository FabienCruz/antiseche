import os, glob, pathlib, re, datetime
from tkinter import *
# from tkinter import font, ttk, messagebox

import screen, file, service

window=Tk()

directory = file.Directory('content/')
output = file.Directory('docs/')
extension = '.md'
files = directory.list_files(extension)
screen.Screen(window, directory, extension, files)

window.mainloop()