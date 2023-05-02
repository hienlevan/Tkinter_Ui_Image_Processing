
import tkinter as tk
from PIL import ImageTk, Image
import sys

sys.path.append("module")
import module_upload_image
import module_zoom_image
from module_zoom_image import *
from module_upload_image import *
from define import *

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Xử Lý Ảnh Số")
        self.iconbitmap(PATH_ICON)
        self.state('zoomed')
        self.config(background=COLOR_MAIN_BACKGROUND)

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
        menu.add_command(
            label="Upload", command=lambda: upload_image(self.frame_4, self.frame_3_child, self.frame_5))

        menu.add_separator()
        menu.add_command(label="Exit", command=self.quit)

        export_button = tk.Button(
            top_frame, text="Export", borderwidth=0, bg=COLOR_WHITE)
        export_button.pack(side=tk.LEFT, pady=2)

        # END FRAME 1

        # FRAME 2
        screen_width = self.winfo_screenwidth()
        self.frame_2 = tk.Frame(
            self, bd=0, relief="groove", background=COLOR_WHITE)
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

        # FRAME 3
        self.frame_3 = tk.Frame(
            self, bd=3, relief="flat", background=COLOR_BG_1)
        self.frame_3.place(relx=0.003, rely=0.598, anchor="w",
                           width=270, height=630)

        self.frame_3_child = tk.Canvas(
            self.frame_3, bd=0, relief="flat", background=COLOR_MAIN_BACKGROUND, highlightbackground = '#161e31')
        self.frame_3_child.place(relx=0.5, rely=0.22, anchor="center",
                                 width=260, height=260)
        
        self.frame_3_child_2 = tk.Frame(self.frame_3, background=COLOR_MAIN_BACKGROUND, height=350)
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



        # CONTAINER_4_5
        self.container_4_5 = tk.Canvas(self, bg=COLOR_MAIN_BACKGROUND, highlightthickness=0)
        self.container_4_5.place(relx=0.5, rely=0.598, anchor='center',width=960, height=630)


        # FRAME 4
        # Tạo một đối tượng Canvas để hiển thị ảnh
        self.frame_4 = tk.Canvas(
            self.container_4_5, bd=0, relief="groove", background=COLOR_MAIN_BACKGROUND, highlightthickness=0)
        self.frame_4.place(relx=0, rely=0,
                           anchor="nw", width=480, height=630)
        

        # Vertical and horizontal scrollbars for canvas
        vbar = AutoScrollbar(self.frame_4, orient='vertical')
        hbar = AutoScrollbar(self.frame_4, orient='horizontal')
        vbar.grid(row=0, column=1, sticky='ns')
        hbar.grid(row=1, column=0, sticky='we')
        self.frame_4.update()
        vbar.configure(command=lambda *args,**kwargs:scroll_y(self.frame_4, *args, **kwargs) )  
        hbar.configure(command=lambda *args,**kwargs:scroll_x(self.frame_4, *args, **kwargs) )
        # Make the canvas expandable
        self.frame_4.rowconfigure(0, weight=1)
        self.frame_4.columnconfigure(0, weight=1)
        
        self.frame_4.bind('<ButtonPress-1>', lambda event: move_from(self.frame_4,event))

        self.frame_4.bind('<B1-Motion>', lambda event: move_to(self.frame_4,event))

        # self.frame_4.bind('<MouseWheel>', lambda event: wheel(self.frame_4,event))

        # images = self.frame_4.find_withtag('image')
        # x1, y1, x2, y2 = self.frame_4.coords(images[0])
        # x2 = 206
        # x1=1
        # y2=300
        # y1=2
        # f_width = x2 - x1
        # f_height = y2 - y1
        # self.frame_4.width = f_width
        # self.frame_4.height = f_height

        # frame4_imscale = 1.0
        # frame4_delta = 1.3

        # self.container = self.canvas.create_rectangle(0, 0, self.width, self.height, width=0)


        def scroll_y(self, *args, **kwargs):
            ''' Scroll canvas vertically and redraw the image '''
            self.canvas.yview(*args, **kwargs)  # scroll vertically
            self.show_image()  # redraw the image

        def scroll_x(self, *args, **kwargs):
            ''' Scroll canvas horizontally and redraw the image '''
            self.canvas.xview(*args, **kwargs)  # scroll horizontally
            self.show_image()  # redraw the image

        def move_from(self, event):
            ''' Remember previous coordinates for scrolling with the mouse '''
            self.scan_mark(event.x, event.y)

        def move_to(self, event):
            ''' Drag (move) canvas to the new position '''
            self.scan_dragto(event.x, event.y, gain=1)
            # self.show_image()  # redraw the image

        # def wheel(self, event):
        #     scale = 1.0
        #     _width = f_width
        #     _height = f_height
        #     imscale = frame4_imscale
        #     delta = frame4_delta
        #     x = self.canvasx(event.x)
        #     y = self.canvasy(event.y) 
        #     bbox = self.bbox(self.create_rectangle(0, 0, _width, _height, width=0))
        #     if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: pass
        #     else: return
            
        #     if event.num == 5 or event.delta == -120:
        #         i = min(_width, _height)
        #         if int(i * imscale) < 30: return
        #         imscale /= delta
        #         scale /=delta
        #     if event.num == 4 or event.delta == 120:
        #         i = min(self.winfo_width(), self.winfo_height())
        #         if i < self.imscale: return
        #         imscale *= delta
        #         scale*= delta
        #     self.scale('all', x, y, scale, scale)
            # self.show_image()
        
        # FRAME 5
        self.frame_5 = tk.Canvas(
            self.container_4_5, bd=0, relief="groove", background=COLOR_MAIN_BACKGROUND, highlightthickness=0)
        self.frame_5.place(relx=1.005, rely=0, anchor="ne",
                           width=480, height=630)
        
        x_line = 482 # tọa độ x của điểm bắt đầu
        y_line = 0  # tọa độ y của điểm bắt đầu
        length_line = 630 # chiều dài của đường thẳng
        self.container_4_5.create_line(x_line, y_line, x_line, y_line+length_line, fill='#fff')
        
        # FRAME 6
        self.frame_6 = tk.Frame(
            self, bd=0, relief="flat", background=COLOR_BG_1)
        self.frame_6.place(relx=0.997, rely=0.598, anchor="e",
                           width=270, height=630)

        self.btn_reset = tk.Button(
            self.frame_6, relief="raised", bd=0, text="Reset", bg=COLOR_BG_3, fg="#000")
        self.btn_reset.pack(side=tk.BOTTOM, fill=tk.X)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
