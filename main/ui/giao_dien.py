import tkinter as tk
from PIL import ImageTk, Image
from define import *


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Xử Lý Ảnh Số")
        self.iconbitmap(PATH_ICON)
        self.state('zoomed')
        self.config(background='#000')

        screen_width = self.winfo_screenwidth()

        # FRAME 1

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        top_frame = tk.Frame(self, height=10, bg=COLOR_WHITE)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        filemenu = tk.Menubutton(
            top_frame, text="File", borderwidth=0, bg=COLOR_WHITE)
        filemenu.pack(side=tk.LEFT, pady=1)

        menu = tk.Menu(filemenu, tearoff=0)
        filemenu["menu"] = menu
        menu.add_command(label="Upload")
        menu.add_separator()
        menu.add_command(label="Exit", command=self.quit)

        export_button = tk.Button(
            top_frame, text="Export", borderwidth=0, bg=COLOR_WHITE)
        export_button.pack(side=tk.LEFT, pady=2)

        # END FRAME 1

        # FRAME 2
        self.frame_2 = tk.Frame(
            self, bd=2, relief="groove", background=COLOR_WHITE)
        self.frame_2.place(relx=0.5, rely=0.044, anchor="n",
                           width=screen_width, height=115)

        self.logo = ImageTk.PhotoImage(Image.open(PATH_LOGO))
        logo_ute = tk.Label(self.frame_2, image=self.logo, bg=COLOR_WHITE)
        logo_ute.place(relx=0.01, rely=0.49, anchor="w")

        school = tk.Label(
            self.frame_2, text="Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM", font=FONT_SCHOOL, bg=COLOR_WHITE)
        school.place(relx=0.11, rely=0.2, anchor="w")
        subject = tk.Label(
            self.frame_2, text="Môn học: Xử Lý Ảnh Số", font=FONT_ST_INFO, bg=COLOR_WHITE)
        subject.place(relx=0.11, rely=0.45, anchor="w")
        lophoc = tk.Label(
            self.frame_2, text="Lớp: DIPR430685_22_2_05CLC", font=FONT_ST_INFO, bg=COLOR_WHITE)
        lophoc.place(relx=0.11, rely=0.7, anchor="w")

        st_name_1 = tk.Label(
            self.frame_2, text="Trương Tấn Phúc", font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_name_1.place(relx=0.85, rely=0.2, anchor="e")
        st_id_1 = tk.Label(self.frame_2, text="20110554",
                           font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_id_1.place(relx=0.95, rely=0.2, anchor="e")

        st_name_2 = tk.Label(self.frame_2, text="Lê Văn Hiền",
                             font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_name_2.place(relx=0.821, rely=0.45, anchor="e")
        st_id_2 = tk.Label(self.frame_2, text="20110475",
                           font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_id_2.place(relx=0.95, rely=0.45, anchor="e")

        st_name_3 = tk.Label(self.frame_2, text="Lê Hải",
                             font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_name_3.place(relx=0.79, rely=0.7, anchor="e")
        st_id_3 = tk.Label(self.frame_2, text="20110464",
                           font=FONT_ST_INFO, bg=COLOR_WHITE)
        st_id_3.place(relx=0.95, rely=0.7, anchor="e")

        # END FRAME 2

        # Khung số 3
        self.frame_3 = tk.Frame(
            self, bd=2, relief="groove", background='#292929')
        self.frame_3.place(relx=0, rely=0.598, anchor="w",
                           width=270, height=630)

        # Khung số 4
        self.frame_4 = tk.Frame(
            self, bd=2, relief="groove", background='#7f7f7f')
        self.frame_4.place(relx=0.5, rely=0.598, anchor="center",
                           width=964, height=630)

        # Khung số 5
        self.frame_5 = tk.Frame(
            self, bd=2, relief="groove", background='#292929')
        self.frame_5.place(relx=1, rely=0.598, anchor="e",
                           width=270, height=630)


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
