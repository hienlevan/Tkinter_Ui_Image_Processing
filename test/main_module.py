from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
from define import *

class ImageFrame(Canvas):
    def __init__(self, master, path, *pargs, **kw):
        Canvas.__init__(self, master, *pargs, **kw)
        self.img_copy = Image.open(path)
        self.image = Image.new("RGB", (self.img_copy.width, self.img_copy.height)) # initialize to black placeholder

        self.bind("<Configure>", self._resize_image)

    def _resize_image(self, event):
        # calculate resize parameters
        w_ratio = event.width / self.img_copy.width
        h_ratio = event.height / self.img_copy.height
        ratio = min(w_ratio, h_ratio)
        new_size = (int(self.img_copy.width * ratio), int(self.img_copy.height * ratio))

        # resize image and update canvas
        if new_size != self.image.size:
            self.image = self.img_copy.resize(new_size)
            self.background_image = ImageTk.PhotoImage(self.image)
            self.delete("bg")
            self.create_image(0, 0, anchor="nw", image=self.background_image, tags="bg")
            self.tag_lower("bg", "all")

class user_interface(Frame):
    """docstring for user_interface"""

    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.counter = 0

        self.heading = Frame(self.root,bg='white')
        self.heading.place(relx=0.5, rely=0, anchor="n",
                    width=self.root.winfo_screenwidth(), height=115)

        self.heading.logo = ImageTk.PhotoImage(Image.open(PATH_LOGO))
        self.heading.logo_ute = Label(self.heading, image=self.heading.logo, bg=COLOR_WHITE)
        self.heading.logo_ute.place(relx=0.01, rely=0.49, anchor="w")
        self.heading.school = Label(
    self.heading, text="Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM", font=FONT_SCHOOL, bg=COLOR_WHITE)
        self.heading.school.place(relx=0.11, rely=0.2, anchor="w")
        self.heading.subject = Label(self.heading, text="Môn học: Xử Lý Ảnh Số", font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.subject.place(relx=0.11, rely=0.45, anchor="w")
        self.heading.lophoc = Label(self.heading, text="Lớp: DIPR430685_22_2_05CLC", font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.lophoc.place(relx=0.11, rely=0.7, anchor="w")

        self.heading.st_name_1 = Label(self.heading, text="Trương Tấn Phúc", font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_name_1.place(relx=0.85, rely=0.2, anchor="e")
        self.heading.st_id_1 = Label(self.heading, text="20110554",
                            font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_id_1.place(relx=0.95, rely=0.2, anchor="e")

        self.heading.st_name_2 = Label(self.heading, text="Lê Văn Hiền",
                                font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_name_2.place(relx=0.821, rely=0.45, anchor="e")
        self.heading.st_id_2 = Label(self.heading, text="20110475",
                            font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_id_2.place(relx=0.95, rely=0.45, anchor="e")

        self.heading.st_name_3 = Label(self.heading, text="Lê Hải",
                                font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_name_3.place(relx=0.79, rely=0.7, anchor="e")
        self.heading.st_id_3 = Label(self.heading, text="20110464",
                            font=FONT_ST_INFO, bg=COLOR_WHITE)
        self.heading.st_id_3.place(relx=0.95, rely=0.7, anchor="e")

        self.container1 = Frame(self.root, bg='blue')
        self.container1.place(relx=0.5, rely=0.15, anchor='n', width=self.root.winfo_screenwidth(), height=115)

        self.word_enter = Label(self.container1, text="Select Image             : ", fg="black", font="Times 13 bold")
        self.word_enter.place(x=20, y=30)

        self.word_enter1 = Label(self.container1, text="Output Destination : ", fg="black", font="Times 13 bold")
        self.word_enter1.place(x=20, y=80)

        self.entry1 = Text(self.container1)
        self.entry1.place(x=180, y=30, height=25, width=300)

        self.entry2 = Text(self.container1)
        self.entry2.place(x=180, y=80, height=25, width=300)

        self.next_btn = Button(self.container1, text="Select", bg="#535C68", fg="white", command=lambda: self.next_click(),
                               font="Courier 13 bold")

        self.next_btn.place(x=500, y=30, width=80, height=25)

        self.gen_btn = Button(self.container1, text="Select", bg="#535C68", fg="white",
                              command=lambda: self.gen_img(), font="Courier 13 bold")
        self.gen_btn.place(x=500, y=80, width=80, height=25)

        self.gen_btn2 = Button(self.container1, text="Convert", bg="#535C68", fg="white",
                               command=lambda: self.cvt(), font="Courier 13 bold")
        self.gen_btn2.place(x=500, y=130, width=80, height=25)

        self.container2 = Frame(
    self.root, bd=3,background=COLOR_BG_1, highlightthickness=1, highlightbackground='black')
        self.container2.place(relx=0.003, rely=0.64, anchor="w",
                    width=270, height=570)
        
        self.blur = Label(self.container2, text="Select Blur : ", fg="black", font="Times 10 bold")
        self.blur.place(x=10, y=10)

        self._job = None
        self.slider = Scale(self.container2, from_=1, to=100, orient=HORIZONTAL, command=self.updateValue)
        self.slider.place(x=10, y=130)

        self.hvar = IntVar()
        self.vvar = IntVar()
        self.svar = IntVar()
        self.hBlur = Checkbutton(self.container2, text="Horizontal Blur", variable=self.hvar).place(x=10, y=40)
        self.vBlur = Checkbutton(self.container2, text="Vertical Blur", variable=self.vvar).place(x=10, y=70)
        self.sharp = Checkbutton(self.container2, text="Sharpness", variable=self.svar).place(x=10, y=100)

    def updateValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(500, self._do_something)

    def _do_something(self):
        self._job = None
        self.counter = self.slider.get()
        self.editor(self.root.filename, self.counter)
        self.im = ImageFrame(self.root, self.root.filename + "Blurred.png")
        self.im.place(x=700, y=251)
        self.im.update()
    
    def next_click(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        
        self.im = ImageFrame(self.root, self.root.filename)
        self.im.place(x=280, y=251)
        self.entry1.insert(INSERT, self.root.filename)

    def gen_img(self):
        self.root.dir = filedialog.askdirectory()
        self.entry2.insert(INSERT, self.root.dir)

    def cvt(self):
        try:
            file = self.root.filename
            cv2.imwrite(self.root.dir + "\\test.jpg", self.output10)
            messagebox.showinfo("Output","Image Saved !")
        except:
            messagebox.showerror("Something Went Wrong !", "Select Output Path")

    def unsharp_mask(self, image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
        """Return a sharpened version of the image, using an unsharp mask."""
        blurred = cv2.GaussianBlur(image, kernel_size, sigma)
        sharpened = float(amount + 1) * image - float(amount) * blurred
        sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
        sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
        sharpened = sharpened.round().astype(np.uint8)
        if threshold > 0:
            low_contrast_mask = np.absolute(image - blurred) < threshold
            np.copyto(sharpened, image, where=low_contrast_mask)
        return sharpened

    def editor(self, img, num):
        if num != 0:
            if self.hvar.get() == 1 and self.vvar.get() == 1:
                img = cv2.imread(img)
                kernel_3 = np.ones((num, num), dtype=np.float32) / (num * num)
                self.output10 = cv2.filter2D(img, -1, kernel_3)
                cv2.imwrite(self.root.filename + "Blurred.png", self.output10)

            elif self.hvar.get() == 1:
                h_blur = np.zeros((num, num))
                h_blur[num // 2, :] = np.ones(num)
                h_blur = h_blur / num
                self.output10 = cv2.filter2D(cv2.imread(img), -1, h_blur)
                cv2.imwrite(self.root.filename + "Blurred.png", self.output10)

            elif self.vvar.get() == 1:
                v_blur = np.zeros((num, num))
                v_blur[:, num // 2] = np.ones(num)
                v_blur = v_blur / num
                self.output10 = cv2.filter2D(cv2.imread(img), -1, v_blur)
                cv2.imwrite(self.root.filename + "Blurred.png", self.output10)

            elif self.svar.get() == 1:
                self.output10 = self.unsharp_mask(cv2.imread(img), (5, 5), 2, num, 0)
                cv2.imwrite(self.root.filename + "Blurred.png", self.output10)

            else:
                pass