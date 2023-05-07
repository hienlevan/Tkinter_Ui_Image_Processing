from tkinter import *
from main_module import user_interface as UI
from define import *


def app():
    root = Tk()
    root.state('zoomed')
    
    root.iconbitmap(PATH_ICON)
    root.title("Project Xu Ly Anh So")
    root.resizable(False, False)

    frame = UI(root)
    frame.place()

    root.mainloop()


if __name__ == '__main__':
    app()