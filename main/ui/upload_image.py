
from tkinter import filedialog
from PIL import ImageTk, Image

from tkinter import filedialog
from PIL import Image, ImageTk


def upload_image(frame1, frame2):
    # Xóa ảnh cũ (nếu có)
    frame1.delete("all")
    frame2.delete("all")
    # Hiển thị hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    # Đọc tệp ảnh và tạo một đối tượng Image
    image1 = Image.open(file_path)
    image2 = Image.open(file_path)

    # Thay đổi kích thước ảnh để nằm trong khung nhưng vẫn giữ được tỷ lệ ảnh
    max_size1 = (frame1.winfo_width(), frame1.winfo_height())
    image1.thumbnail(max_size1, Image.ANTIALIAS)

    max_size2 = (frame2.winfo_width(), frame2.winfo_height())
    image2.thumbnail(max_size2, Image.ANTIALIAS)
    # Tạo một đối tượng ImageTk từ đối tượng Image
    photo1 = ImageTk.PhotoImage(image1)
    photo2 = ImageTk.PhotoImage(image2)
    # Lưu trữ đối tượng photo để tránh bị xóa khỏi bộ nhớ
    frame1.image = photo1
    frame2.image = photo2
    # Hiển thị ảnh trên khung
    x1 = frame1.winfo_width() / 2
    y1 = frame1.winfo_height() / 2
    frame1.create_image(x1, y1, image=photo1, anchor="center", tags="image")

    x2 = frame2.winfo_width() / 2
    y2 = frame2.winfo_height() / 2
    frame2.create_image(x2, y2, image=photo2, anchor="center", tags="image")
