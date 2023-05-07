
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
import sys
import cv2

import numpy as np

sys.path.append("module")
from module_zoom_image import *
from module_upload_image import *
from define import *


global f_container
f_container =None
global f_imscale
f_imscale = 1.0
global f_delta
f_delta = 1.3
global f_width
f_width = None
global f_height
f_height = None
global img
global img2

global img_f4
img_f4 = None 

global anh_xl
anh_xl = None
global anh_xl2
anh_xl2 = None
global anh_xl3
anh_xl3 = None

global flag
flag = 1





root = tk.Tk()
root.title("Project Xử Lý Ảnh Số")
root.iconbitmap(PATH_ICON)
root.state('zoomed')
root.config(background=COLOR_MAIN_BACKGROUND)

# Frame 1
menubar = tk.Menu(root)
root.config(menu=menubar)

top_frame = tk.Frame(root,relief='groove' ,height=10, bg='white')
top_frame.pack(side=tk.TOP, fill=tk.X)

filemenu = tk.Menubutton(
    top_frame, text="File", borderwidth=0, bg=COLOR_WHITE)
filemenu.pack(side=tk.LEFT, pady=1)

menu = tk.Menu(filemenu, tearoff=0)
filemenu["menu"] = menu
menu.add_command(label="Upload", command=lambda:open_file_dialog())
menu.add_command(label='Export')
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

# export_button = tk.Button(
#     top_frame, text="Export", borderwidth=0, bg=COLOR_WHITE)
# export_button.pack(side=tk.LEFT, pady=2)

###

# Frame 2
screen_width = root.winfo_screenwidth()
frame_2 = tk.Frame(
    root, bd=0, relief="groove", background=COLOR_WHITE, highlightthickness=1, highlightbackground='black')
frame_2.place(relx=0.5, rely=0.044, anchor="n",
                    width=screen_width, height=115)

logo = ImageTk.PhotoImage(Image.open(PATH_LOGO))
logo_ute = tk.Label(frame_2, image=logo, bg=COLOR_WHITE)
logo_ute.place(relx=0.01, rely=0.49, anchor="w")

school = tk.Label(
    frame_2, text="Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM", font=FONT_SCHOOL, bg=COLOR_WHITE)
school.place(relx=0.11, rely=0.2, anchor="w")
subject = tk.Label(frame_2, text="Môn học: Xử Lý Ảnh Số", font=FONT_ST_INFO, bg=COLOR_WHITE)
subject.place(relx=0.11, rely=0.45, anchor="w")
lophoc = tk.Label(frame_2, text="Lớp: DIPR430685_22_2_05CLC", font=FONT_ST_INFO, bg=COLOR_WHITE)
lophoc.place(relx=0.11, rely=0.7, anchor="w")

st_name_1 = tk.Label(frame_2, text="Trương Tấn Phúc", font=FONT_ST_INFO, bg=COLOR_WHITE)
st_name_1.place(relx=0.85, rely=0.2, anchor="e")
st_id_1 = tk.Label(frame_2, text="20110554",
                    font=FONT_ST_INFO, bg=COLOR_WHITE)
st_id_1.place(relx=0.95, rely=0.2, anchor="e")

st_name_2 = tk.Label(frame_2, text="Lê Văn Hiền",
                        font=FONT_ST_INFO, bg=COLOR_WHITE)
st_name_2.place(relx=0.821, rely=0.45, anchor="e")
st_id_2 = tk.Label(frame_2, text="20110475",
                    font=FONT_ST_INFO, bg=COLOR_WHITE)
st_id_2.place(relx=0.95, rely=0.45, anchor="e")

st_name_3 = tk.Label(frame_2, text="Lê Hải",
                        font=FONT_ST_INFO, bg=COLOR_WHITE)
st_name_3.place(relx=0.79, rely=0.7, anchor="e")
st_id_3 = tk.Label(frame_2, text="20110464",
                    font=FONT_ST_INFO, bg=COLOR_WHITE)
st_id_3.place(relx=0.95, rely=0.7, anchor="e")

##

# Frame 3
frame_3 = tk.Frame(
    root, bd=3,background=COLOR_BG_1, highlightthickness=1, highlightbackground='black')
frame_3.place(relx=0.003, rely=0.598, anchor="w",
                    width=270, height=630)

frame_3_child = tk.Canvas(
    frame_3, bd=0,background=COLOR_MAIN_BACKGROUND,highlightthickness=1, highlightbackground='black')
frame_3_child.place(relx=0.5, rely=0.216, anchor="center",
                            width=260, height=260)

frame_3_child_2 = tk.Frame(frame_3, background=COLOR_MAIN_BACKGROUND, height=350, highlightthickness=1, highlightbackground='black')
frame_3_child_2.pack(fill=tk.X, side="bottom")


# global radio_var
radio_var = tk.IntVar(0)
radiobutton_1 = ctk.CTkRadioButton(master=frame_3_child_2, text="Làm mờ",variable=radio_var, value=1, font=FONT_CHOOSE, command=lambda:choose_filter())
radiobutton_2 = ctk.CTkRadioButton(master=frame_3_child_2, text="Làm nét", variable=radio_var, value=2, font=FONT_CHOOSE, command=lambda:choose_filter())
radiobutton_3 = ctk.CTkRadioButton(master=frame_3_child_2, text="Làm mịn và giảm nhiễu", variable=radio_var, value=3, font=FONT_CHOOSE, command=lambda:choose_filter())
radio_var.trace("w", lambda name, index, mode, var=radio_var: print(var.get()))

radiobutton_1.place(x = 25, y = 10)
radiobutton_2.place(x = 25, y = 60)
radiobutton_3.place(x = 25, y = 110)

# Container_4_5
container_4_5 = tk.Canvas(root,bg='black', highlightthickness=1)
container_4_5.place(relx=0.5, rely=0.598, anchor='center',width=960, height=630)

# Frame 4
# Tạo một đối tượng Canvas để hiển thị ảnh
frame_4 = tk.Canvas(
    container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
frame_4.place(relx=0.25, rely=0.5,
                    anchor="center", width=478, height=628)
frame_4_label_after_image = tk.Label(frame_4, text="Before",background='#585858', fg='white', width=20)
frame_4_label_after_image.place(relx=1, y=0, anchor="ne")
# # Frame 5
frame_5 = tk.Canvas(
    container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
frame_5.place(relx=0.75, rely=0.5, anchor="center",
                    width=478, height=628)
frame_5_label_after_image = tk.Label(frame_5, text="After",background='#585858', fg='white', width=20)
frame_5_label_after_image.place(relx=0, y=0, anchor="nw")

frame_5_container_img = tk.Canvas(
    frame_5, bd=0, relief="groove", background='black', highlightthickness=0)
frame_5_container_img.place(x=1, y=22, anchor="nw",
                    width=459, height=588)


vbar = AutoScrollbar(frame_5, orient='vertical')
hbar = AutoScrollbar(frame_5, orient='horizontal')
vbar.grid(row=0, column=1, sticky='ns')
hbar.grid(row=1, column=0, sticky='we', columnspan=2)
frame_5_container_img.config(yscrollcommand=vbar.set, xscrollcommand=hbar.set)
frame_5.update()
vbar.configure(command=lambda *args:scroll_y(frame_5_container_img, *args))  
hbar.configure(command=lambda *args:scroll_x(frame_5_container_img, *args))
frame_5.rowconfigure(0, weight=1)
frame_5.columnconfigure(0, weight=1)


x_line = 480 # tọa độ x của điểm bắt đầu
y_line = 0  # tọa độ y của điểm bắt đầu
length_line = 630 # chiều dài của đường thẳng
container_4_5.create_line(x_line, y_line, x_line, y_line+length_line, fill='white')

# FRAME 6
frame_6 = tk.Frame(
    root, bd=0, relief="flat", background=COLOR_BG_1, highlightthickness=1, highlightbackground='black')
frame_6.place(relx=0.997, rely=0.598, anchor="e",
                    width=270, height=630)

frame_6_chart = tk.Canvas(frame_6, bd=0,background=COLOR_MAIN_BACKGROUND,highlightthickness=1, highlightbackground='black', width=260, height=260)
frame_6_chart.pack(side=tk.TOP, anchor="center", pady=6)

frame_6_container_slider = tk.Canvas(frame_6, bd=0,background=COLOR_MAIN_BACKGROUND,highlightthickness=1, highlightbackground='black')
frame_6_container_slider.place(relx=0.5, rely=0.696, anchor="center",
                            width=260, height=323)

btn_reset = tk.Button(
    frame_6, relief="raised", bd=0, text="Reset", bg=COLOR_BG_3, fg="#000")
btn_reset.place(relx=0.5, rely=0.976, anchor="center", width=260)

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

def open_file_dialog():
    global anh_xl
    global f_container
    global f_imscale
    global f_delta
    global f_width
    global f_height
    frame_4.delete("all")
    frame_5.delete("all")
    file_path = filedialog.askopenfilename()
    img = cv2.imread(file_path)

    # Chuyển đổi ảnh thành định dạng hình ảnh PIL
    global img_f4
    img_f4 = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    anh_xl = img_f4
    # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
    global img_tk
    max_size_frame4 = (frame_4.winfo_width(), frame_4.winfo_height())
    img_resize_frame_4 = resize_image(img_f4, max_size_frame4)
    img_tk = ImageTk.PhotoImage(img_resize_frame_4)
    x1_f4 = frame_4.winfo_width() / 2
    y1_f4 = frame_4.winfo_height() / 2
    frame_4.create_image(x1_f4, y1_f4, image=img_tk, anchor="center", tags="image")

def show_image(self, event=None):
    ''' Show image on the Canvas '''
    global f_container
    global f_imscale
    global f_delta
    global f_width
    global f_height
    global anh_xl
    global anh_xl2
    global anh_xl3
    global flag

    bbox1 = self.bbox(f_container)  
    bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
    bbox2 = (self.canvasx(0),  
            self.canvasy(0),
            self.canvasx(self.winfo_width()),
            self.canvasy(self.winfo_height()))
    bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  
            max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
    if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  
        bbox[0] = bbox1[0]
        bbox[2] = bbox1[2]
    if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  
        bbox[1] = bbox1[1]
        bbox[3] = bbox1[3]
    self.configure(scrollregion=bbox)  
    x1 = max(bbox2[0] - bbox1[0], 0)  
    y1 = max(bbox2[1] - bbox1[1], 0)
    x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
    y2 = min(bbox2[3], bbox1[3]) - bbox1[1]

    if int(x2 - x1) > 0 and int(y2 - y1) > 0: 
        x = min(int(x2 / f_imscale), f_width)   
        y = min(int(y2 / f_imscale), f_height) 
        if(flag %2 != 0):
            image = anh_xl3.crop((int(x1 / f_imscale), int(y1 / f_imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                            anchor='nw', image=imagetk)
            self.lower(imageid)  
            self.imagetk = imagetk
        if(flag %2 == 0):
            image = anh_xl3.crop((int(x1 / f_imscale), int(y1 / f_imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
            imageid = self.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                            anchor='nw', image=imagetk)
            self.lower(imageid)  
            self.imagetk = imagetk

def lam_mo(image, kernel_size, sigma):
    global f_container
    global f_imscale
    global f_delta
    global f_width
    global f_height
    global anh_xl
    global anh_xl2
    global anh_xl3
    global flag

    if(flag % 2 != 0):
        blurred = cv2.GaussianBlur(image, kernel_size, sigma)
        anh_xl2 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
        anh_xl3 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
        show_image(frame_5_container_img)
        anh_xl3 = anh_xl
        flag = flag +1
        print("lần thứ {} có giá trị là: {}".format(flag, flag))
    else:
        if(flag % 2 == 0):
            blurred = cv2.GaussianBlur(image, kernel_size, sigma)
            anh_xl2 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
            anh_xl3 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
            show_image(frame_5_container_img)
            anh_xl2 = anh_xl
            flag = flag +1
            print("lần thứ {} có giá trị là: {}".format(flag, flag))
    
def choose_filter():
    frame_5_container_img.delete('all')
    global f_container
    global f_imscale
    global f_delta
    global f_width
    global f_height
    global img_f4

    global blur_tk 
    
    global anh_xl
    f_imscale = 1.0
    f_delta = 1.3

    if radio_var.get() == 1:
         # Lấy ảnh gốc từ hình ảnh PIL đã chọn
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        anh_xl = img
        # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
        max_size = (frame_5_container_img.winfo_width(), frame_5_container_img.winfo_height())
        img_resize_frame_5_container_img = resize_image(img, max_size)
        blur_tk = ImageTk.PhotoImage(img_resize_frame_5_container_img)
        x1_f4 = frame_5_container_img.winfo_width() / 2
        y1_f4 = frame_5_container_img.winfo_height() / 2
        frame_5_container_img.create_image(x1_f4, y1_f4, image=blur_tk, anchor="center", tags="image")
        f_width, f_height = img.size
        f_container = frame_5_container_img.create_rectangle(0, 0,f_width, f_height, width=0)

        radio_var.trace("w", lambda name, index, mode, var=radio_var: print(var.get()))

        global slider_lam_mo
        def slider_event(value):
            lam_mo(np.array(anh_xl), (5, 5), value)
            print(value)
        slider_lam_mo = slider = ctk.CTkSlider(master=frame_6_container_slider,
                                 width=160,
                                 height=16,
                                 border_width=5.5,from_=0, to=5,command=slider_event)
        slider_lam_mo.set(0)
        slider.place(relx=0.5, rely=0.5, anchor='center')

        # Tạo một Label để hiển thị giá trị của sliderbar
        label_slider_value = tk.Label(master=frame_6_container_slider, text="Current slider value: {}".format(slider_lam_mo.get()))
        label_slider_value.place(relx=0.5, rely=0.4, anchor='center')


        def on_slider_change(event):
            label_slider_value.config(text=f"Giá trị hiện tại: {slider_lam_mo.get()}")

        slider_lam_mo.bind('<ButtonRelease-1>', on_slider_change)
        print(radio_var.get())
    
    if radio_var.get() == 2:
         # Lấy ảnh gốc từ hình ảnh PIL đã chọn
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        anh_xl = img
        # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
        max_size = (frame_5_container_img.winfo_width(), frame_5_container_img.winfo_height())
        img_resize_frame_5_container_img = resize_image(img, max_size)
        blur_tk = ImageTk.PhotoImage(img_resize_frame_5_container_img)
        x1_f4 = frame_5_container_img.winfo_width() / 2
        y1_f4 = frame_5_container_img.winfo_height() / 2
        frame_5_container_img.create_image(x1_f4, y1_f4, image=blur_tk, anchor="center", tags="image")
        f_width, f_height = img.size
        f_container = frame_5_container_img.create_rectangle(0, 0,f_width, f_height, width=0)

        radio_var.trace("w", lambda name, index, mode, var=radio_var: print(var.get()))

        global slider_lam_net 
        slider_lam_net = slider =ctk.CTkSlider(master=frame_6_container_slider,
                                 width=160,
                                 height=16,
                                 border_width=5.5)
        slider.place(relx=0.5, rely=0.5, anchor='center')
        print(radio_var.get())

    if radio_var.get() == 3:
         # Lấy ảnh gốc từ hình ảnh PIL đã chọn
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        anh_xl = img
        # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
        max_size = (frame_5_container_img.winfo_width(), frame_5_container_img.winfo_height())
        img_resize_frame_5_container_img = resize_image(img, max_size)
        blur_tk = ImageTk.PhotoImage(img_resize_frame_5_container_img)
        x1_f4 = frame_5_container_img.winfo_width() / 2
        y1_f4 = frame_5_container_img.winfo_height() / 2
        frame_5_container_img.create_image(x1_f4, y1_f4, image=blur_tk, anchor="center", tags="image")
        f_width, f_height = img.size
        f_container = frame_5_container_img.create_rectangle(0, 0,f_width, f_height, width=0)

        radio_var.trace("w", lambda name, index, mode, var=radio_var: print(var.get()))

        global slider_lam_min 
        slider_lam_min = slider =ctk.CTkSlider(master=frame_6_container_slider,
                                 width=160,
                                 height=16,
                                 border_width=5.5)
        slider.place(relx=0.5, rely=0.5, anchor='center')
        print(radio_var.get())


        





def wheel(self, event):
    ''' Zoom with mouse wheel '''
    global f_container
    global f_imscale
    global f_delta
    global f_width
    global f_height
    x = self.canvasx(event.x)
    y = self.canvasy(event.y)
    bbox = self.bbox(f_container)

    if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: pass 
    else: return
    scale = 1.0
    if event.num == 5 or event.delta == -120:
        i = min(f_width, f_height)
        if int(i * f_imscale) < 30: return
        f_imscale /= f_delta
        scale        /= f_delta
    if event.num == 4 or event.delta == 120:
        i = min(self.winfo_width(), self.winfo_height())
        if i < f_imscale: return
        f_imscale *= f_delta
        scale        *= f_delta
    self.scale('all', x, y, scale, scale)
    show_image(self)  


# def show_image(self, event=None):
#     ''' Show image on the Canvas '''
#     global f_container
#     global f_imscale
#     global f_delta
#     global f_width
#     global f_height
#     global anh_xl
#     bbox1 = self.bbox(f_container)  
#     bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
#     bbox2 = (self.canvasx(0),  
#             self.canvasy(0),
#             self.canvasx(self.winfo_width()),
#             self.canvasy(self.winfo_height()))
#     bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  
#             max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
#     if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  
#         bbox[0] = bbox1[0]
#         bbox[2] = bbox1[2]
#     if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  
#         bbox[1] = bbox1[1]
#         bbox[3] = bbox1[3]
#     self.configure(scrollregion=bbox)  
#     x1 = max(bbox2[0] - bbox1[0], 0)  
#     y1 = max(bbox2[1] - bbox1[1], 0)
#     x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
#     y2 = min(bbox2[3], bbox1[3]) - bbox1[1]

#     if int(x2 - x1) > 0 and int(y2 - y1) > 0: 
#         x = min(int(x2 / f_imscale), f_width)   
#         y = min(int(y2 / f_imscale), f_height)  
#         image = anh_xl.crop((int(x1 / f_imscale), int(y1 / f_imscale), x, y))
#         imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
#         imageid = self.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
#                                         anchor='nw', image=imagetk)
#         self.lower(imageid)  
#         self.imagetk = imagetk

def hide_image(self):
    ''' Hide the image to avoid multiple images when scrolling '''
    # Kiểm tra nếu hình ảnh tồn tại trên Canvas thì mới tiếp tục
    if self.find_withtag('image'):
        if self.itemcget('image', 'state') != 'hidden':
            self.itemconfig('image', state='hidden')

def scroll_y(self, *args):
    ''' Scroll canvas horizontally and redraw the image '''
    self.yview(*args)
    show_image(self)

def scroll_x(self, *args):
    ''' Scroll canvas horizontally and redraw the image '''
    self.xview(*args)
    show_image(self)  

def move_from(self, event):
    ''' Remember previous coordinates for scrolling with the mouse '''
    self.scan_mark(event.x, event.y)
    show_image(self)  

def move_to(self, event):
    ''' Drag (move) canvas to the new position '''
    self.scan_dragto(event.x, event.y, gain=1)
    show_image(self)  

frame_5_container_img.bind('<ButtonPress-1>', lambda event:(move_from(frame_5_container_img, event), hide_image(frame_5_container_img)))
frame_5_container_img.bind('<B1-Motion>', lambda event:(move_to(frame_5_container_img, event), hide_image(frame_5_container_img)))
frame_5_container_img.bind('<MouseWheel>', lambda event:(wheel(frame_5_container_img, event), hide_image(frame_5_container_img)))  
frame_5_container_img.bind('<Button-4>', lambda event:wheel(frame_5_container_img, event))  
frame_5_container_img.bind('<Button-5>', lambda event:wheel(frame_5_container_img, event))
  
root.mainloop()




