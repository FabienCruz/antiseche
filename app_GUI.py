import screen, file, service

from tkinter import *

window=Tk()

directory = file.Directory('contents/')
extension = '.md'
screen.Screen(window, directory, extension)

window.mainloop()