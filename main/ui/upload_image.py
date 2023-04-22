
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Hàm xử lý upload ảnh


def upload_image(self, button=None):
    file_path = filedialog.askopenfilename()

    # Xóa tất cả các widget con trong khung bên trái
    for widget in self.image_frame_left.winfo_children():
        widget.destroy()

    # Xử lý logic cho việc hiển thị ảnh trong khung bên trái
    try:
        image = Image.open(file_path)
        # Tính toán tỉ lệ giữa chiều rộng và chiều cao của ảnh
        width, height = image.size
        ratio = min(500 / width, 600 / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        # Thay đổi kích thước của ảnh
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image_tk = ImageTk.PhotoImage(image)
        # Tạo widget Label để hiển thị ảnh
        image_label = tk.Label(self.image_frame_left, image=image_tk)
        # Lưu giữ tham chiếu tới object image_tk để tránh việc bị hủy bởi garbage collector
        image_label.image_tk = image_tk
        image_label.pack()
    except:
        tk.messagebox.showerror("Lỗi", "Không thể mở file ảnh")
    # Disable button sau khi đã upload ảnh
    # if button:
    #    button.config(state="disabled")
