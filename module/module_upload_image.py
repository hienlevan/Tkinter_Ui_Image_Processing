
import sys
from PIL import ImageTk, Image
from tkinter import filedialog
from PIL import Image, ImageTk


sys.path.append("module")
import module_upload_image
import module_zoom_image
from module_zoom_image import *

class AutoScrollbar(ttk.Scrollbar):
    ''' A scrollbar that hides itself if it's not needed.
        Works only if you use the grid geometry manager '''
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with this widget')

    def place(self, **kw):
        raise tk.TclError('Cannot use place with this widget')

def resize_image(image, max_size):
    # Tính tỷ lệ khung hình của ảnh và khung.
    image_ratio = image.width / image.height
    frame_ratio = max_size[0] / max_size[1]
    if image.width < max_size[0] or image.height < max_size[1]:
        if max_size[0] - image.width < max_size[1] - image.height:
            new_width = max_size[0]
            new_height = round(new_width / image_ratio)
        else:
            new_height = max_size[1]
            new_width = round(new_height * image_ratio)
    else:
        if image_ratio > frame_ratio:
            new_width = max_size[0]
            new_height = round(new_width / image_ratio)
        else:
            new_height = max_size[1]
            new_width = round(new_height * image_ratio)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return image

# def upload_image(frame1, frame2):
#     # Xóa ảnh cũ (nếu có)
#     frame1.delete("all")
#     frame2.delete("all")
#     # Hiển thị hộp thoại để chọn tệp ảnh
#     file_path = filedialog.askopenfilename()
#     if not file_path:
#         return
#     # Đọc tệp ảnh và tạo một đối tượng Image
#     image1 = Image.open(file_path)
#     image2 = Image.open(file_path)
#     # Thay đổi kích thước ảnh để nằm trong khung nhưng vẫn giữ được tỷ lệ ảnh
#     max_size1 = (frame1.winfo_width(), frame1.winfo_height())
#     image1_resize= resize_image(image1, max_size1)
#     max_size2 = (frame2.winfo_width(), frame2.winfo_height())
#     image2_resize= resize_image(image2, max_size2)
#     # Tạo một đối tượng ImageTk từ đối tượng Image
#     photo1 = ImageTk.PhotoImage(image1_resize)
#     photo2 = ImageTk.PhotoImage(image2_resize)
#     # Lưu trữ đối tượng photo để tránh bị xóa khỏi bộ nhớ
#     frame1.image = photo1
#     frame2.image = photo2
#     # Hiển thị ảnh trên khung
#     x1 = frame1.winfo_width() / 2
#     y1 = frame1.winfo_height() / 2
#     frame1.create_image(x1, y1, image=photo1, anchor="center", tags="image")
#     x2 = frame2.winfo_width() / 2
#     y2 = frame2.winfo_height() / 2
#     frame2.create_image(x2, y2, image=photo2, anchor="center", tags="image")

def upload_image(frame1, frame2, frame3):
    # Xóa ảnh cũ (nếu có)
    frame1.delete("all")
    frame2.delete("all")
    frame3.delete("all")
    # Hiển thị hộp thoại để chọn tệp ảnh
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    # Đọc tệp ảnh và tạo một đối tượng Image
    image1 = Image.open(file_path)
    image2 = Image.open(file_path)
    image3 = Image.open(file_path)
    # Thay đổi kích thước ảnh để nằm trong khung nhưng vẫn giữ được tỷ lệ ảnh
    max_size1 = (frame1.winfo_width(), frame1.winfo_height())
    image1_resize= resize_image(image1, max_size1)

    max_size2 = (frame2.winfo_width(), frame2.winfo_height())
    image2_resize= resize_image(image2, max_size2)

    max_size3 = (frame3.winfo_width(), frame3.winfo_height())
    image3_resize= resize_image(image3, max_size3)
    # Tạo một đối tượng ImageTk từ đối tượng Image
    photo1 = ImageTk.PhotoImage(image1_resize)
    photo2 = ImageTk.PhotoImage(image2_resize)
    photo3 = ImageTk.PhotoImage(image3_resize)
    # Lưu trữ đối tượng photo để tránh bị xóa khỏi bộ nhớ
    frame1.image = photo1
    frame2.image = photo2
    frame3.image = photo3
    # Hiển thị ảnh trên khung
    x1 = frame1.winfo_width() / 2
    y1 = frame1.winfo_height() / 2
    frame1.create_image(x1, y1, image=photo1, anchor="center", tags="image")
    
    x2 = frame2.winfo_width() / 2
    y2 = frame2.winfo_height() / 2
    frame2.create_image(x2, y2, image=photo2, anchor="center", tags="image")

    x3 = frame3.winfo_width() / 2
    y3 = frame3.winfo_height() / 2
    frame3.create_image(x3, y3, image=photo3, anchor="center", tags="image")


