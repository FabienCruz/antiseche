import screen, file, service

from tkinter import *

window=Tk()

directory = file.Directory('content/')
extension = '.md'
screen.Screen(window, directory, extension)

window.mainloop()