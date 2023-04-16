import os
from tkinter import *
from tkinter import font

from define import *
from App import App

window = Tk()
app = App(window)
path_directory = os.path.dirname(__file__)
path_image = os.path.join(os.path.join(
    path_directory, 'images'), 'logo_spkt.png')

photo = PhotoImage(file=path_image)
label_image_logo = Label(window, image=photo).place(x=10, y=10)

window.mainloop()
