import tkinter as tk
from define import *


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Xử Lý Ảnh Số")
        self.iconbitmap(PATH_ICON)
        self.state('zoomed')
        # self.geometry("1400x700")

        # Tính toán kích thước khung và vị trí của chúng
        frame_width = 700
        frame_height = 500

        # Khởi tạo khung trên cùng để hiển thị hình ảnh và label
        screen_width = self.winfo_screenwidth()
        self.top_frame = tk.Frame(
            self, bd=2, relief="groove")
        self.top_frame.place(relx=0.5, rely=0, anchor="n",
                             width=screen_width, height=50)

        # Thêm label studen vào cột cuối của grid
        max_column = self.top_frame.grid_size()[0]
        self.studen_1 = tk.Label(
            self.top_frame, text="20110xxx - Nguyen Van A")
        self.studen_1.grid(row=0, column=3)

        self.studen_2 = tk.Label(
            self.top_frame, text="20110xxx - Nguyen Van A")
        self.studen_1.grid(row=0, column=2)

        # Khởi tạo khung bên trái để hiển thị hình ảnh
        self.image_frame_left = tk.Frame(
            self, width=frame_width, height=frame_height, bd=2, relief="groove")
        self.image_frame_left.place(
            relx=0.02, rely=0.1, width=frame_width, height=frame_height, anchor="nw")

        # Khởi tạo khung bên phải để hiển thị nội dung khác
        self.content_frame_right = tk.Frame(
            self, width=frame_width, height=frame_height, bd=2, relief="groove")
        self.content_frame_right.place(
            relx=1-0.02, rely=0.1, width=frame_width, height=frame_height, anchor="ne")


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
