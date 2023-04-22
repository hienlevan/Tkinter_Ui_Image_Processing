import tkinter as tk
from define import *


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Xử Lý Ảnh Số")
        self.iconbitmap(PATH_ICON)
        self.state('zoomed')
        self.config(background='#000')
        # self.geometry("1400x700")

        # Tính toán kích thước khung và vị trí của chúng
        frame_width = 700
        frame_height = 500

        # Khung số 1
        screen_width = self.winfo_screenwidth()
        self.frame_1 = tk.Frame(
            self, bd=2, relief="groove", background='#fff', highlightbackground="#000", highlightthickness=1)
        self.frame_1.place(relx=0.5, rely=0, anchor="n",
                           width=screen_width, height=20)

        # Khung số 2
        self.frame_2 = tk.Frame(
            self, bd=2, relief="groove", background='#fff', highlightbackground="#000", highlightthickness=1)
        self.frame_2.place(relx=0.5, rely=0.034, anchor="n",
                           width=screen_width, height=115)

        # Khung số 3
        self.frame_3 = tk.Frame(
            self, bd=2, relief="groove", background='#292929', highlightbackground="#fff", highlightthickness=1)
        self.frame_3.place(relx=0, rely=0.585, anchor="w",
                           width=270, height=630)

        # Khung số 4
        self.frame_4 = tk.Frame(
            self, bd=2, relief="groove", background='#7f7f7f', highlightbackground="#000", highlightthickness=1)
        self.frame_4.place(relx=0.49999, rely=0.585, anchor="center",
                           width=965, height=630)

        # Khung số 5
        self.frame_5 = tk.Frame(
            self, bd=2, relief="groove", background='#292929', highlightbackground="#fff", highlightthickness=1)
        self.frame_5.place(relx=1, rely=0.585, anchor="e",
                           width=270, height=630)

        # # Khởi tạo khung bên trái để hiển thị hình ảnh
        # self.image_frame_left = tk.Frame(
        #     self, width=frame_width, height=frame_height, bd=2, relief="groove")
        # self.image_frame_left.place(
        #     relx=0.02, rely=0.1, width=frame_width, height=frame_height, anchor="nw")


        # # Khởi tạo khung bên phải để hiển thị nội dung khác
        # self.content_frame_right = tk.Frame(
        #     self, width=frame_width, height=frame_height, bd=2, relief="groove")
        # self.content_frame_right.place(
        #     relx=1-0.02, rely=0.1, width=frame_width, height=frame_height, anchor="ne")
if __name__ == "__main__":
    app = GUI()
    app.mainloop()
