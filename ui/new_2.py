import random
import tkinter as tk
from PIL import ImageTk, Image
import sys

sys.path.append("module")
import module_upload_image
import module_zoom_image
from module_zoom_image import *
from module_upload_image import *
from define import *


f_container = None
f_width = None
f_height = None
f_imscale = 1.0
f_delta = 1.3
path_img = ''
img = None


class AutoScrollbar(tk.Scrollbar):
    ''' A scrollbar that hides itself if it's not needed.
        Works only if you use the grid geometry manager '''
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            tk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with this widget')

    def place(self, **kw):
        raise tk.TclError('Cannot use place with this widget')


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Xử Lý Ảnh Số")
        self.iconbitmap(PATH_ICON)
        self.state('zoomed')
        self.config(background=COLOR_MAIN_BACKGROUND)

        # Frame 1
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        top_frame = tk.Frame(self,relief='groove' ,height=10, bg=COLOR_WHITE)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        filemenu = tk.Menubutton(
            top_frame, text="File", borderwidth=0, bg=COLOR_WHITE)
        filemenu.pack(side=tk.LEFT, pady=1)

        menu = tk.Menu(filemenu, tearoff=0)
        filemenu["menu"] = menu
        menu.add_command(label="Upload", command=lambda: (open_file_dialog(self.frame_4) ))
        menu.add_command(label='Export')
        menu.add_separator()
        menu.add_command(label="Exit", command=self.quit)

        # export_button = tk.Button(
        #     top_frame, text="Export", borderwidth=0, bg=COLOR_WHITE)
        # export_button.pack(side=tk.LEFT, pady=2)

        ###

        # Frame 2
        screen_width = self.winfo_screenwidth()
        self.frame_2 = tk.Frame(
            self, bd=0, relief="groove", background=COLOR_WHITE, highlightthickness=1, highlightbackground='black')
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

        ###

        # Frame 3
        self.frame_3 = tk.Frame(
            self, bd=3,background=COLOR_BG_1, highlightthickness=1, highlightbackground='black')
        self.frame_3.place(relx=0.003, rely=0.598, anchor="w",
                           width=270, height=630)

        self.frame_3_child = tk.Canvas(
            self.frame_3, bd=0,background=COLOR_MAIN_BACKGROUND,highlightthickness=1, highlightbackground='black')
        self.frame_3_child.place(relx=0.5, rely=0.216, anchor="center",
                                 width=260, height=260)
        
        self.frame_3_child_2 = tk.Frame(self.frame_3, background=COLOR_MAIN_BACKGROUND, height=350, highlightthickness=1, highlightbackground='black')
        self.frame_3_child_2.pack(fill=tk.X, side="bottom")

        selected = tk.StringVar()
        r1 = tk.Radiobutton(self.frame_3_child_2, text='Làm mờ ảnh',bg=COLOR_WHITE,indicatoron=0,
                            value='1', variable=selected,font=FONT_CHOOSE, selectcolor=COLOR_BG_3, anchor='w')
        r2 = tk.Radiobutton(self.frame_3_child_2, text='Làm nét ảnh',bg=COLOR_WHITE,indicatoron=0,
                            value='2', variable=selected, font=FONT_CHOOSE, selectcolor=COLOR_BG_3, anchor='w')
        r3 = tk.Radiobutton(self.frame_3_child_2, text='Tách phông nền',bg=COLOR_WHITE,indicatoron=0,
                            value='3', variable=selected, font=FONT_CHOOSE, selectcolor=COLOR_BG_3, anchor='w')

        r4 = tk.Radiobutton(self.frame_3_child_2, text='Làm mịn, giảm nhiễu ảnh',bg=COLOR_WHITE,indicatoron=0,
                            value='4', variable=selected,font=FONT_CHOOSE, selectcolor=COLOR_BG_3, anchor='w')
    
        r1.place(x = 25, y = 10, width=220)
        r2.place(x = 25, y = 60, width=220)
        r3.place(x = 25, y = 110, width=220)
        r4.place(x = 25, y = 160, width=220)

        ###

        # Container_4_5
        self.container_4_5 = tk.Canvas(self,bg='black', highlightthickness=1)
        self.container_4_5.place(relx=0.5, rely=0.598, anchor='center',width=960, height=630)

        ###
        vbar = AutoScrollbar(self.container_4_5, orient='vertical')
        hbar = AutoScrollbar(self.container_4_5, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
        ###

        # Frame 4
        # Tạo một đối tượng Canvas để hiển thị ảnh
        self.frame_4 = tk.Canvas(
            self.container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
        self.frame_4.place(relx=0.25, rely=0.5,
                           anchor="center", width=478, height=628)
        
        vbar = AutoScrollbar(self.frame_4, orient='vertical')
        hbar = AutoScrollbar(self.frame_4, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
        self.frame_4.config(yscrollcommand=vbar.set, xscrollcommand=hbar.set)
        self.frame_4.update()
        
        # self.canvas.update()  
        vbar.configure(command=lambda *args:scroll_y(self.frame_4, *args))  
        hbar.configure(command=lambda *args:scroll_x(self.frame_4, *args))

        self.frame_4.rowconfigure(0, weight=1)
        self.frame_4.columnconfigure(0, weight=1)

        # # Frame 5
        self.frame_5 = tk.Canvas(
            self.container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
        self.frame_5.place(relx=0.75, rely=0.5, anchor="center",
                           width=478, height=628)
        

        x_line = 480 # tọa độ x của điểm bắt đầu
        y_line = 0  # tọa độ y của điểm bắt đầu
        length_line = 630 # chiều dài của đường thẳng
        self.container_4_5.create_line(x_line, y_line, x_line, y_line+length_line, fill='white')

        # FRAME 6
        self.frame_6 = tk.Frame(
            self, bd=0, relief="flat", background=COLOR_BG_1)
        self.frame_6.place(relx=0.997, rely=0.598, anchor="e",
                           width=270, height=630)

        self.btn_reset = tk.Button(
            self.frame_6, relief="raised", bd=0, text="Reset", bg=COLOR_BG_3, fg="#000")
        self.btn_reset.pack(side=tk.BOTTOM, fill=tk.X)


        ###
        # self.frame_4.bind('<Configure>', lambda event:show_image(self.frame_4, event))  
        self.frame_4.bind('<ButtonPress-1>', lambda event:(move_from(self.frame_4, event), hide_image(self.frame_4)))
        self.frame_4.bind('<B1-Motion>', lambda event:(move_to(self.frame_4, event), hide_image(self.frame_4)))
        self.frame_4.bind('<MouseWheel>', lambda event:(wheel(self.frame_4, event), hide_image(self.frame_4)))  
        self.frame_4.bind('<Button-4>', lambda event:wheel(self.frame_4, event))  
        self.frame_4.bind('<Button-5>', lambda event:wheel(self.frame_4, event))  
        # self.canvas.bind('<Button-5>',   self.wheel)  
        # self.canvas.bind('<Button-4>',   self.wheel)
        ###


        print("The image with the path: " + str(path_img) + "\nhas a size of: " +str(f_width) + "x" + str(f_height))

        def hide_image(self):
            ''' Hide the image to avoid multiple images when scrolling '''
            # Kiểm tra nếu hình ảnh tồn tại trên Canvas thì mới tiếp tục
            if self.find_withtag('image'):
                if self.itemcget('image', 'state') != 'hidden':
                    self.itemconfig('image', state='hidden')

        def open_file_dialog(self):
            global path_img
            global img
            global f_width 
            global f_height
            global f_container
            global f_imscale 
            global f_delta
            f_imscale = 1.0
            f_delta = 1.3
            self.delete("all")
            path_image = filedialog.askopenfilename()
            path_img = path_image
            img = Image.open(path_img)
            f_width, f_height = img.size
            max_size = (self.winfo_width(), self.winfo_height())
            img_resize = resize_image(img, max_size)
            photo = ImageTk.PhotoImage(img_resize)
            self.image = photo
            x1 = self.winfo_width() / 2
            y1 = self.winfo_height() / 2
            self.create_image(x1, y1, image=photo, anchor="center", tags="image")
            print("The image with the path: " + str(path_img) + "\nhas a size of: " +str(f_width) + "x" + str(f_height))
            f_container = self.create_rectangle(0, 0,f_width, f_height, width=0)
            # hide_image(self)
            # self.after(10, lambda: show_image(self))
            # minsize, maxsize, number = 5, 20, 10
            # for n in range(number):
            #     x0 = random.randint(0, f_width - maxsize)
            #     y0 = random.randint(0, f_height - maxsize)
            #     x1 = x0 + random.randint(minsize, maxsize)
            #     y1 = y0 + random.randint(minsize, maxsize)
            #     color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
            #     self.create_rectangle(x0, y0, x1, y1, fill=color, activefill='black')

        
        def wheel(self, event):
            ''' Zoom with mouse wheel '''
            global f_container
            global f_imscale
            global f_delta
            global f_width
            global f_height
            global img

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


        def show_image(self, event=None):
            ''' Show image on the Canvas '''
            global f_container
            global f_imscale
            global f_delta
            global f_width
            global f_height
            global img

            bbox1 = self.bbox(f_container)  # get image area
            # Remove 1 pixel shift at the sides of the bbox1
            bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1)
            bbox2 = (self.canvasx(0),  # get visible area of the canvas
                    self.canvasy(0),
                    self.canvasx(self.winfo_width()),
                    self.canvasy(self.winfo_height()))
            bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]),  # get scroll region box
                    max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
            if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]:  # whole image in the visible area
                bbox[0] = bbox1[0]
                bbox[2] = bbox1[2]
            if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]:  # whole image in the visible area
                bbox[1] = bbox1[1]
                bbox[3] = bbox1[3]
            self.configure(scrollregion=bbox)  # set scroll region
            x1 = max(bbox2[0] - bbox1[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
            y1 = max(bbox2[1] - bbox1[1], 0)
            x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
            y2 = min(bbox2[3], bbox1[3]) - bbox1[1]

            if int(x2 - x1) > 0 and int(y2 - y1) > 0:  # show image if it in the visible area
                x = min(int(x2 / f_imscale), f_width)   # sometimes it is larger on 1 pixel...
                y = min(int(y2 / f_imscale), f_height)  # ...and sometimes not
                image = img.crop((int(x1 / f_imscale), int(y1 / f_imscale), x, y))
                imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1))))
                imageid = self.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),
                                                anchor='nw', image=imagetk)
                self.lower(imageid)  # set image into background
                self.imagetk = imagetk

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

        # def scroll_y(self, *args, **kwargs):
        #     ''' Scroll canvas vertically and redraw the image '''
        #     self.yview(*args, **kwargs)  
        #     show_image(self)  

        # def scroll_x(self, *args, **kwargs):
        #     ''' Scroll canvas horizontally and redraw the image '''
        #     self.xview(*args, **kwargs)  
        #     show_image(self)

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

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
