
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

from tkinter import filedialog
from PIL import Image, ImageTk


def upload_image(frame):
    # Xóa ảnh cũ (nếu có)
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    # Hiển thị hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Đọc tệp ảnh và tạo một đối tượng Image
    image = Image.open(file_path)

    # Thay đổi kích thước ảnh để nằm trong khung nhưng vẫn giữ được tỷ lệ ảnh
    max_size = (frame.winfo_width(), frame.winfo_height())
    image.thumbnail(max_size, Image.ANTIALIAS)

    # Tạo một đối tượng ImageTk từ đối tượng Image
    photo = ImageTk.PhotoImage(image)

    # Hiển thị ảnh trên khung
    label = tk.Label(frame, image=photo)
    label.image = photo
    label.pack()
