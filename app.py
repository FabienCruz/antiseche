import screen, file, service

from tkinter import *

window=Tk()

directory = file.Directory('content/')
output = file.Directory('docs/')
extension = '.md'
files = directory.list_files(extension)
screen.Screen(window, directory, extension, files)

window.mainloop()