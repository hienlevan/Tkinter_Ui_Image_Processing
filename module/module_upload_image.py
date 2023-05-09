

import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.slider_1 = None
        self.slider_2 = None

        self.create_radiobutton()
        self.create_menu()

    # def create_radiobutton(self):
    #     self.radiobutton_var = tk.StringVar(value="option 1")
    #     self.radiobutton = tk.Radiobutton(self.frame, text="Select option", variable=self.radiobutton_var,
    #                                          value="option 1", command=self.create_menu)
    #     self.radiobutton.pack()
    def create_radiobutton(self):
        self.radiobutton_var = tk.StringVar(value="option 1")
        self.radiobutton_1 = tk.Radiobutton(self.frame, text="Option 1", variable=self.radiobutton_var,
                                                value="option 1", command=self.create_menu)
        self.radiobutton_2 = tk.Radiobutton(self.frame, text="Option 2", variable=self.radiobutton_var,
                                                value="option 2", command=self.create_menu)
        self.radiobutton_1.pack()
        self.radiobutton_2.pack()


    def create_menu(self):
        self.clear_sliders()

        option = self.radiobutton_var.get()

        if option == "option 1":
            self.create_menu_1()
        elif option == "option 2":
            self.create_menu_2()

    def create_menu_1(self):
        menu_1 = tk.Menu(self.root, tearoff=False)

        slider_1 = tk.Scale(self.frame, from_=0, to=100, orient="horizontal")
        slider_1.pack()
        slider_1.place(relx=0.5, rely=0.5, anchor="center")


        menu_1.add_command(label="Slider 1", command=lambda: slider_1.lift())
        menu_1.add_command(label="Exit", command=self.clear_sliders)

        self.slider_1 = slider_1

        self.root.config(menu=menu_1)

    def create_menu_2(self):
        menu_2 = tk.Menu(self.root, tearoff=False)

        slider_2 = tk.Scale(self.frame, from_=0, to=100, orient="vertical")
        slider_2.pack()
        slider_2.place(relx=0.5, rely=0.8, anchor="center")

        menu_2.add_command(label="Slider 2", command=lambda: slider_2.lift())
        menu_2.add_command(label="Exit", command=self.clear_sliders)

        self.slider_2 = slider_2

        self.root.config(menu=menu_2)

    def clear_sliders(self):
        if self.slider_1:
            self.slider_1.destroy()
            self.slider_1 = None

        if self.slider_2:
            self.slider_2.destroy()
            self.slider_2 = None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x300')
    app = App(root)
    root.mainloop()