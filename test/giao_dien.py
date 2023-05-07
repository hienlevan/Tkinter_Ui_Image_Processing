from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog

# Tạo cửa sổ Tkinter
root = Tk()

# Tạo canvas để hiển thị ảnh
canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Load ảnh
img_path = filedialog.askopenfilename()
img = cv2.imread(img_path)

# Chuyển đổi ảnh thành dạng PIL để hiển thị trên canvas
pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
pil_img.thumbnail((canvas_width, canvas_height))

# Tạo đối tượng ImageTk từ ảnh PIL để hiển thị trên canvas
img_tk = ImageTk.PhotoImage(pil_img)
canvas.create_image(canvas_width/2, canvas_height/2, image=img_tk, anchor="center")

# Lưu đối tượng ImageTk của vùng ảnh đã được chọn và áp dụng bộ lọc Gaussian Blur
blur_tk = None

# Lưu tọa độ của chuột
x_start = 0
y_start = 0
x_end = 0
y_end = 0

# Hàm xử lý sự kiện khi bắt đầu chọn vùng ảnh
def on_button_press(event):
    global x_start, y_start
    if event.state & 0x4:
        x_start = event.x
        y_start = event.y

# Hàm xử lý sự kiện khi di chuyển chuột để chọn vùng ảnh
def on_mouse_move(event):
    global x_start, y_start, x_end, y_end
    if event.state & 0x4:
        x_end = event.x
        y_end = event.y

        # Vẽ hình chữ nhật trên canvas để hiển thị vùng ảnh được chọn
        canvas.delete("rect")
        canvas.create_rectangle(x_start, y_start, x_end, y_end, outline="red", tags="rect")

# Hàm xử lý sự kiện khi kết thúc chọn vùng ảnh
def on_button_release(event):
    global x_start, y_start, x_end, y_end, img, canvas, canvas_width, canvas_height

    # Tạo vùng ảnh được chọn
    selection = img[y_start:y_end, x_start:x_end]

    # Áp dụng bộ lọc Gaussian Blur cho vùng ảnh được chọn
    blur = cv2.GaussianBlur(selection, (25, 25), 0)

    # Gán lại giá trị của vùng ảnh đã được chọn trong ảnh gốc với vùng ảnh đã được làm mờ
    img[y_start:y_end, x_start:x_end] = blur

    # Chuyển đổi ảnh thành dạng PIL để hiển thị trên canvas
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    pil_img.thumbnail((canvas_width, canvas_height))

    # Tạo đối tượng ImageTk từ ảnh PIL để hiển thị trên canvas
    img_tk = ImageTk.PhotoImage(pil_img)
    canvas.create_image(canvas_width/2, canvas_height/2, image=img_tk, anchor="center")

    # Xóa hình chữ nhật trên canvas
    canvas.delete("rect")
# Gán các sự kiện chuột cho canvas
canvas.bind("<ButtonPress-1>", on_button_press)
canvas.bind("<B1-Motion>", on_mouse_move)
canvas.bind("<ButtonRelease-1>", on_button_release)

# Hiển thị cửa sổ Tkinter
root.mainloop()
