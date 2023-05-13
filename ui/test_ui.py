from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
import sys
import cv2
from matplotlib import pyplot as plt
import numpy as np
sys.path.append("module")
from define import *

# global label1, label2, label3
# label1 = None
# label2 = None
# label3 = None


# Chức năng làm mờ, gồm có: ... sliderbar
global slider_lam_mo_kernel_gaussian_ksize, slider_lam_mo_kernel_gaussian_sigma, slider_lam_mo_kernel_blur, slider_lam_mo_kernel_median
slider_lam_mo_kernel_gaussian_ksize = None
slider_lam_mo_kernel_gaussian_sigma = None
slider_lam_mo_kernel_blur = None
slider_lam_mo_kernel_median = None


# Chức năng thay đổi độ tương phản, gồm có: ... sliderbar
global slider_tuong_phan_logarit, slider_tuong_phan_unsharp_mask
slider_tuong_phan_logarit = None
slider_tuong_phan_unsharp_mask = None

# Chức năng làm mịn, gồm có: ... sliderbar
global slider_lam_min_median
slider_lam_min_median = None

# Chức năng tăng giảm sáng, gồm có: ... sliderbar
global slider_tang_giam_sang_
slider_lam_min_median = None



# Ảnh hiển thị trên khung ảnh bên trái có label "Before"
global img_f4
img_f4 = None 

# Ảnh Mặc định người dùng tải lên, được dùng 
# để reset về hình ảnh gốc để áp dụng phép
# xử lý ảnh khi người dùng chọn một chức năng khác trên giao diện
global anh_goc
anh_goc = None

# Ảnh hiện tại - ảnh kết quả sau khi đã được áp dụng phép xử lý ảnh
# Ảnh đang hiển thị trên khung ảnh bên phải có Label "After"
global img_cur
img_cur = None


root = tk.Tk()
root.title("Project Xử Lý Ảnh Số")
root.iconbitmap(PATH_ICON)
root.state('zoomed')
root.config(background=COLOR_MAIN_BACKGROUND)

# Frame 1 -  Frame chứa button "file" dùng để upload, export và exit khỏi giao diện
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
menu.add_command(label='Export', command=lambda:save_photo())
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

# func lưu ảnh khi người dùng chọn export 
# trong menu popup của button "file"
def save_photo():
    global img_cur
    if img_cur is not None:
        path_save_photo = filedialog.asksaveasfilename(defaultextension=".png")
        # print(path_save_photo)
        img_save = cv2.cvtColor(np.array(img_cur), cv2.COLOR_BGR2RGB)
        cv2.imwrite(path_save_photo, img_save)
        messagebox.showinfo('Success!',"Lưu ảnh thành công!\n{}".format(str(path_save_photo)))
    else:
        messagebox.showerror('Error!',"Bạn chưa tải ảnh để xử lý\nHãy tải ảnh và thực hiện xử lý!")

###

# Frame 2 - Frame chứa thông tin của đồ án
# Bao gồm: Logo, thông tin Trường Đại học, Lớp học
# và thông tin của các sinh viên thực hiện đồ án
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

# Frame 3 - Frame chứa khung để hiển thị chart RGB-histogram
# và các Radio-button để người dùng chọn chức năng
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
radiobutton_2 = ctk.CTkRadioButton(master=frame_3_child_2, text="Thay đổi độ tương phản", variable=radio_var, value=2, font=FONT_CHOOSE, command=lambda:choose_filter())
radiobutton_3 = ctk.CTkRadioButton(master=frame_3_child_2, text="Làm mịn và giảm nhiễu", variable=radio_var, value=3, font=FONT_CHOOSE, command=lambda:choose_filter())
radiobutton_4 = ctk.CTkRadioButton(master=frame_3_child_2, text="Tăng giảm sáng", variable=radio_var, value=4, font=FONT_CHOOSE, command=lambda:choose_filter())

# radio_var.trace("w", lambda name, index, mode, var=radio_var: print("Current Radio Button Value: {}".format(var.get())))

radiobutton_1.place(x = 25, y = 10)
radiobutton_2.place(x = 25, y = 60)
radiobutton_3.place(x = 25, y = 110)
radiobutton_4.place(x = 25, y = 160)

# Container_4_5 - Frame chứa hai khung hiển thị ảnh:
# Khung bên trái có label "Before" dùng để hiển thị ảnh gốc tải lên từ thiết bị,
# Khung bên phải có label "After" dùng để hiển thị ảnh đã được áp dụng phép xử
# lý ảnh
container_4_5 = tk.Canvas(root,bg='black', highlightthickness=1)
container_4_5.place(relx=0.585, rely=0.598, anchor='center',width=1240, height=630)

# Frame 4 - Khung bên trái có label "Before" dùng để hiển thị ảnh gốc tải lên từ thiết bị
# Tạo một đối tượng Canvas để hiển thị ảnh
frame_4 = tk.Canvas(
    container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
frame_4.place(relx=0.002, rely=0.998,
                    anchor="sw", width=615, height=607)
frame_4_label_after_image = tk.Label(container_4_5, text="Before",background='#585858', fg='white', width=20)
frame_4_label_after_image.place(relx=0.38, rely=0.002, anchor="nw")
# # Frame 5 - dùng để hiển thị ảnh đã được áp dụng phép xử lý ảnh
frame_5 = tk.Canvas(
    container_4_5, bd=0, relief="groove", background='black', highlightthickness=0)
frame_5.place(relx=0.998, rely=0.998, anchor="se",
                    width=615, height=607)
frame_5_label_after_image = tk.Label(container_4_5, text="After",background='#585858', fg='white', width=20)
frame_5_label_after_image.place(relx=0.6215, rely=0.002, anchor="ne")

x_line = 620 # tọa độ x của điểm bắt đầu
y_line = 0  # tọa độ y của điểm bắt đầu
length_line = 630 # chiều dài của đường thẳng
container_4_5.create_line(x_line, y_line, x_line, y_line+length_line, fill='white')


### CÁC FUNCTION 

# Hàm dùng để thay đổi kích thước ảnh nhưng vẫn giữ được tỉ lệ
# của hình ảnh để hiển thị ảnh nằm vừa trong các khung hiển thị
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

# Hàm dùng để thực hiện việc upload ảnh từ 
# thiết bị của người dùng lên giao diện
def open_file_dialog():
    frame_4.delete("all")
    frame_5.delete("all")
    file_path = filedialog.askopenfilename()
    if not file_path:
        messagebox.showwarning("Warning!", "Bạn chưa chọn ảnh để tải lên!\nHãy tải ảnh để thực hiện việc xử lý")
    else: 
        img = cv2.imread(file_path)
        # Chuyển đổi ảnh thành định dạng hình ảnh PIL
        global img_f4
        img_f4 = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
        global hien_thi_f4
        max_size_frame4 = (frame_4.winfo_width(), frame_4.winfo_height())
        img_resize_frame_4 = resize_image(img_f4, max_size_frame4)
        hien_thi_f4 = ImageTk.PhotoImage(img_resize_frame_4)
        x1_f4 = frame_4.winfo_width() / 2
        y1_f4 = frame_4.winfo_height() / 2
        frame_4.create_image(x1_f4, y1_f4, image=hien_thi_f4, anchor="center", tags="image")

# Hàm dùng để cập nhật những thay đổi 
# của hình ảnh trên giao diện
def update_(canvas, image):
    global hien_thi_canvas
    # canvas.delete('all')
    # Tạo một đối tượng ImageTk từ hình ảnh PIL để hiển thị trên canvas
    max_size = (canvas.winfo_width(), canvas.winfo_height())
    img_resize = resize_image(image, max_size)
    hien_thi_canvas = ImageTk.PhotoImage(img_resize)
    x1 = canvas.winfo_width() / 2
    y1 = canvas.winfo_height() / 2
    canvas.create_image(x1, y1, image=hien_thi_canvas, anchor="center", tags="image")

# Hàm dùng để hiển thị Chart-histogram
def chart_histogram():
    global img_cur
    imm_chart = np.array(img_cur)
    # img_chart = cv2.cvtColor(np.array(img_cur), cv2.COLOR_BGR2RGB)
    b, g, r = cv2.split(imm_chart)
    # Create color maps for each channel
    cm_r = plt.cm.colors.LinearSegmentedColormap.from_list('Reds', [(1, 0, 0), (1, 1, 1)], N=256)
    cm_g = plt.cm.colors.LinearSegmentedColormap.from_list('Greens', [(0, 1, 0), (1, 1, 1)], N=256)
    cm_b = plt.cm.colors.LinearSegmentedColormap.from_list('Blues', [(0, 0, 1), (1, 1, 1)], N=256)

    # Destroy all children of frame_3_child
    for widget in frame_3_child.winfo_children():
        widget.destroy()
    # Create a Figure object and a canvas for it
    fig = plt.Figure(figsize=(10, 5))
    canvas = FigureCanvasTkAgg(fig, master=frame_3_child)
    # Add an Axes to the Figure
    # global ax
    ax = fig.add_subplot(111)
    
    # Plot histograms with color maps
    # Plot red channel histogram
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    ax.fill_between(np.arange(256), np.ravel(hist_r), color=cm_r(hist_r / np.max(hist_r)), alpha=0.5, label='Red')

    # Plot green channel histogram
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    ax.fill_between(np.arange(256), np.ravel(hist_g), color=cm_g(hist_g / np.max(hist_g)), alpha=0.5, label='Green')

    # Plot blue channel histogram
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    ax.fill_between(np.arange(256), np.ravel(hist_b), color=cm_b(hist_b / np.max(hist_b)), alpha=0.5, label='Blue')

    # Configure plot
    ax.set_xlim([0, 256])
    ax.set_title('RGB Histogram', color='white')
    ax.tick_params(axis='both', labelsize=7)
    # Set the border color to white
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(colors='white')

    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.set_facecolor('black')
    # Vô hiệu hóa đường viền trên và bên phải
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend()
    # ax.set_axis_off()
    ax.legend().remove()
    # print("Value RGB of Chart:\nR: {}, G: {}, B: {}".format(np.max(r),np.max(g), np.max(b)))
    fig.patch.set_facecolor('black')
    fig.subplots_adjust(left=0.17, right=0.9, bottom=0.1, top=0.9)
    canvas.get_tk_widget().pack()
    # Update canvas on frame_3_child
    canvas.draw()


# def check_and_delete(label_name, new_value=None):
#     # Save the current value of the global variable
#     old_value = globals().get(label_name)
    
#     # Check if the global variable exists and delete it
#     if old_value is not None:
#         old_value.destroy()
        
#     # If a new value is provided, set it as the new global variable
#     if new_value is not None:
#         globals()[label_name] = new_value 
    
#     # Set the value of the global variable to None after the function is called
#     globals()[label_name] = None
    
#     print(label_name + ": " + str(globals()[label_name]))
#     # Return the old value of the global variable
#     return old_value
#     # global_name = old_value

# def test(test_case):
#     global label1, label2, label3
#     # label1 = None
#     # label2 = None
   
#     if test_case == 1:
#         if(label1 is not None):
#             return
#         if(label1 is None):
#             #tạo label 1
#             label1 = tk.Label(master=frame_3_child_2, text='label số 1')
#             # hiển thị nó lên frame 
#             label1.place(relx=0.35, rely=0.7)
#             print("label1: " + str(label1))
#         # if(label1 is not None):
#         #     return
#         if label2 is not None:
#             check_and_delete("label2", None)
    
#         if label3 is not None:
#             check_and_delete("label3", None)

#     if test_case == 2:
#         if(label2 == None):
#             #tạo label 1
#             label2 = tk.Label(master=frame_3_child_2, text='label số 2')
#             # hiển thị nó lên frame 
#             label2.place(relx=0.35, rely=0.8)
#             print("label2: " + str(label2))

#         if label1 is not None:
#             check_and_delete("label1", None)
    
#         if label3 is not None:
#             check_and_delete("label3", None)

#     if test_case == 3:
#         if(label3 == None):
#             #tạo label 1
#             label3 = tk.Label(master=frame_3_child_2, text='label số 3')
#             # hiển thị nó lên frame 
#             label3.place(relx=0.35, rely=0.9)
#             print("label3: " + str(label3))
#         if label1 is not None:
#             check_and_delete("label1", None)
    
#         if label2 is not None:
#             check_and_delete("label2", None)

# Hàm dùng để ẩn đi slider bar khi người dùng chọn một chức năng mới
def check_and_delete_slider(slider_name, new_value=None):
    # Save the current value of the global variable
    old_value = globals().get(slider_name)
    
    # Check if the global variable exists and delete it
    if old_value is not None:
        old_value.destroy()
        
    # If a new value is provided, set it as the new global variable
    if new_value is not None:
        globals()[slider_name] = new_value 
    
    # Set the value of the global variable to None after the function is called
    globals()[slider_name] = None
    
    # print(slider_name + ": " + str(globals()[slider_name]))
    # Return the old value of the global variable
    return old_value
    # global_name = old_value


# Hàm gọi các phép làm mờ
def call_lam_mo(case):
    global slider_lam_mo_kernel_gaussian_ksize, slider_lam_mo_kernel_gaussian_sigma, slider_lam_mo_kernel_blur, slider_lam_mo_kernel_median 
    global slider_tuong_phan_logarit, slider_tuong_phan_unsharp_mask
    global slider_lam_min_median

    # Hàm gọi các phép làm mờ chỉ có 
    # một giá trị cần thay đổi trên sliderbar 
    def slider_one_event(name_func,value):
                # clear terminal
                os.system('cls')
                print("{} - value Of Kernel Size: {}\n{}".format(name_func,int(value), "="*25))
                name_func(cv2.cvtColor(np.array(anh_goc), cv2.COLOR_BGR2RGB),value)
                chart_histogram()

    # Hàm gọi các phép làm mờ có 
    # hai giá trị cần thay đổi trên sliderbar 
    def slider_two_event(name_func,value_1, value_2):
                # clear terminal
                os.system('cls')
                print("{} - value Of Kernel Size: {}, value Of Sigma: {}\n{}".format(name_func,int(value_1), value_2, "="*55))
                # print("value sigma: {}".format(value_2))           
                name_func(cv2.cvtColor(np.array(anh_goc), cv2.COLOR_BGR2RGB),value_1, value_2)
                chart_histogram()

    # Lựa chọn Popup thứ nhất của Radio-Button làm mờ - "Kernel Gaussian"
    if(case == 1):
        if(slider_lam_mo_kernel_gaussian_ksize is None or slider_lam_mo_kernel_gaussian_sigma is None):
            slider_lam_mo_kernel_gaussian_ksize = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=3, 
                                    to=300,
                                    )
            slider_lam_mo_kernel_gaussian_ksize.set(3)
            slider_lam_mo_kernel_gaussian_ksize.place(relx=0.35, rely=0.8, anchor='center')
            
            slider_lam_mo_kernel_gaussian_sigma = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=20,
                                    )
            slider_lam_mo_kernel_gaussian_sigma.set(0)
            slider_lam_mo_kernel_gaussian_sigma.place(relx=0.35, rely=0.9, anchor='center')
           
            slider_lam_mo_kernel_gaussian_ksize.bind('<Button-1>', lambda event: slider_two_event(lam_mo_kernel_gaussian_active, slider_lam_mo_kernel_gaussian_ksize.get(), slider_lam_mo_kernel_gaussian_sigma.get()))

            slider_lam_mo_kernel_gaussian_sigma.bind('<Button-1>', lambda event: slider_two_event(lam_mo_kernel_gaussian_active, slider_lam_mo_kernel_gaussian_ksize.get(), slider_lam_mo_kernel_gaussian_sigma.get()))

        # Ẩn các thanh sliderbar của phép làm mờ thứ 2
        if slider_lam_mo_kernel_blur is not None:
            check_and_delete_slider("slider_lam_mo_kernel_blur", None)
        # Ẩn các thanh sliderbar của phép làm mờ thứ 3
        if slider_lam_mo_kernel_median is not None:
            check_and_delete_slider("slider_lam_mo_kernel_median", None)

        # Ẩn các thanh sliderbar của chức năng thay đổi độ tương phản
        if slider_tuong_phan_logarit is not None:
            check_and_delete_slider("slider_tuong_phan_logarit", None)
        if slider_tuong_phan_unsharp_mask is not None:
            check_and_delete_slider("slider_tuong_phan_unsharp_mask", None)

        # Ẩn các thanh sliderbar của chức năng làm mịn
        if slider_lam_min_median is not None:
            check_and_delete_slider("slider_lam_min_median", None)

    if(case == 2):
        if(slider_lam_mo_kernel_blur is None):
            slider_lam_mo_kernel_blur = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=10,
                                    command=lambda value: slider_one_event(lam_mo_kernel_blur_active, value)
                                    )
            slider_lam_mo_kernel_blur.set(0)
            slider_lam_mo_kernel_blur.place(relx=0.35, rely=0.8, anchor='center')

        # Ẩn các thanh sliderbar của phép làm mờ thứ nhất
        if slider_lam_mo_kernel_gaussian_ksize is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_ksize", None)
        if slider_lam_mo_kernel_gaussian_sigma is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_sigma", None)
        # Ẩn các thanh sliderbar của phép làm mờ thứ 3
        if slider_lam_mo_kernel_median is not None:
            check_and_delete_slider("slider_lam_mo_kernel_median", None)
        

        # Ẩn các thanh sliderbar của chức năng thay đổi độ tương phản
        if slider_tuong_phan_logarit is not None:
            check_and_delete_slider("slider_tuong_phan_logarit", None)
        if slider_tuong_phan_unsharp_mask is not None:
            check_and_delete_slider("slider_tuong_phan_unsharp_mask", None)

        # Ẩn các thanh sliderbar của chức năng làm mịn
        if slider_lam_min_median is not None:
            check_and_delete_slider("slider_lam_min_median", None)
    if(case == 3):
        if(slider_lam_mo_kernel_median is None):
            slider_lam_mo_kernel_median = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=10,
                                    command=lambda value: slider_one_event(lam_mo_kernel_median_active, value)
                                    )
            slider_lam_mo_kernel_median.set(0)
            slider_lam_mo_kernel_median.place(relx=0.35, rely=0.8, anchor='center')

        # Ẩn các thanh sliderbar của phép làm mờ thứ nhất
        if slider_lam_mo_kernel_gaussian_ksize is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_ksize", None)
        if slider_lam_mo_kernel_gaussian_sigma is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_sigma", None)
        # Ẩn các thanh sliderbar của phép làm mờ thứ 2
        if slider_lam_mo_kernel_blur is not None:
            check_and_delete_slider("slider_lam_mo_kernel_blur", None)
        

        # Ẩn các thanh sliderbar của chức năng thay đổi độ tương phản
        if slider_tuong_phan_logarit is not None:
            check_and_delete_slider("slider_tuong_phan_logarit", None)
        if slider_tuong_phan_unsharp_mask is not None:
            check_and_delete_slider("slider_tuong_phan_unsharp_mask", None)

        # Ẩn các thanh sliderbar của chức năng làm mịn
        if slider_lam_min_median is not None:
            check_and_delete_slider("slider_lam_min_median", None)

    
            
# Các Function thực hiện các phép làm mờ
def lam_mo_kernel_gaussian_active(image,ksize,sigma):
    global img_kq
    img_kq = lam_mo_kernel_gaussian(image,ksize,sigma)
    update_(frame_5,img_kq)

def lam_mo_kernel_gaussian(image,ksize,sigma):
    global img_cur
    # Kích thước kernel và độ lệch chuẩn
    # ksize = 100 # ksize tỉ lệ thuận với độ lớn của kernel Gaussian
    # Tạo kernel Gaussian làm mờ ảnh và giảm nhiễu
    ksize = int(ksize)
    kernel = np.zeros((ksize, ksize), dtype=np.float32)
    for i in range(ksize):
        for j in range(ksize):
            x = i - ksize//2
            y = j - ksize//2
            if sigma == 0:
                kernel[i,j] = 0 if x != 0 or y != 0 else 1
            else:
                kernel[i,j] = np.exp(-(x**2 + y**2)/(2*sigma**2))/(2*np.pi*sigma**2)
    # Chuẩn hóa kernel
    kernel /= np.sum(kernel)
    # Áp dụng kernel vào từng kênh của ảnh bằng cách sử dụng filter2D
    blurred = cv2.filter2D(image, -1, kernel)
    img_temp1 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    # cập nhật ảnh trên frame 5
    img_cur = img_temp1
    return img_temp1

def lam_mo_kernel_blur_active(image, ksize):
    global img_kq
    img_kq = lam_mo_kernel_blur(image,ksize)
    update_(frame_5,img_kq)

def lam_mo_kernel_blur(image, ksize):
    global img_cur
    ksize = int(ksize)
    blurred = cv2.blur(image, (ksize, ksize))
    img_temp1 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    # cập nhật ảnh trên frame 5
    img_cur = img_temp1
    return img_temp1

def lam_mo_kernel_median_active(image, ksize):
    global img_kq
    img_kq = lam_mo_kernel_blur(image,ksize)
    update_(frame_5,img_kq)

def lam_mo_kernel_median(image, ksize):
    global img_cur
    ksize = int(ksize)
    blurred = cv2.medianBlur(image, (ksize, ksize))
    img_temp1 = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    # cập nhật ảnh trên frame 5
    img_cur = img_temp1
    return img_temp1



###
# Hàm gọi các phép thay đổi độ tương phản 
def call_tuong_phan(case):
    global slider_lam_mo_kernel_gaussian_ksize, slider_lam_mo_kernel_gaussian_sigma, slider_lam_mo_kernel_blur, slider_lam_mo_kernel_median 
    global slider_tuong_phan_logarit, slider_tuong_phan_unsharp_mask
    global slider_lam_min_median

    def slider_event(name_func,value):
                os.system('cls')
                print("{} - value Of Kernel Size: {}\n{}".format(name_func,int(value), "="*25))
                name_func(cv2.cvtColor(np.array(anh_goc), cv2.COLOR_BGR2RGB),value)
                chart_histogram()
    if(case == 1):
        if(slider_tuong_phan_logarit is None):
            slider_tuong_phan_logarit = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=50,
                                    command=lambda value: slider_event(tuong_phan_logarit_active, value)
                                    )
            slider_tuong_phan_logarit.set(0)
            slider_tuong_phan_logarit.place(relx=0.35, rely=0.8, anchor='center')

        # Ẩn các thanh sliderbar của chức năng làm mờ
        if slider_lam_mo_kernel_gaussian_ksize is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_ksize", None)

        if slider_lam_mo_kernel_gaussian_sigma is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_sigma", None)

        if slider_lam_mo_kernel_blur is not None:
            check_and_delete_slider("slider_lam_mo_kernel_blur", None)

        if slider_lam_mo_kernel_median is not None:
            check_and_delete_slider("slider_lam_mo_kernel_median", None)

        # Ẩn các thanh sliderbar của phép thay đổi độ tương phản thứ 2
        if slider_tuong_phan_unsharp_mask is not None:
            check_and_delete_slider("slider_tuong_phan_unsharp_mask", None)

        # Ẩn các thanh sliderbar của chức năng làm mịn
        if slider_lam_min_median is not None:
            check_and_delete_slider("slider_lam_min_median", None)

    if(case == 2):
        if(slider_tuong_phan_unsharp_mask is None):
            slider_tuong_phan_unsharp_mask = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=50,
                                    command=lambda value: slider_event(tuong_phan_unsharp_mask_active, value)
                                    )
            slider_tuong_phan_unsharp_mask.set(0)
            slider_tuong_phan_unsharp_mask.place(relx=0.35, rely=0.8, anchor='center')

        # Ẩn các thanh sliderbar của chức năng làm mờ
        if slider_lam_mo_kernel_gaussian_ksize is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_ksize", None)
        if slider_lam_mo_kernel_gaussian_sigma is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_sigma", None)
        if slider_lam_mo_kernel_blur is not None:
            check_and_delete_slider("slider_lam_mo_kernel_blur", None)
        if slider_lam_mo_kernel_median is not None:
            check_and_delete_slider("slider_lam_mo_kernel_median", None)
        
        # Ẩn các thanh sliderbar phép thay đổi độ tương phản thứ nhất
        if slider_tuong_phan_logarit is not None:
            check_and_delete_slider("slider_tuong_phan_logarit", None)

        # Ẩn các thanh sliderbar của chức năng làm mịn
        if slider_lam_min_median is not None:
            check_and_delete_slider("slider_lam_min_median", None)
    
def tuong_phan_logarit_active(img, c):
    global img_kq
    img_kq = tuong_phan_logarit(img, c)
    update_(frame_5, img_kq)

def tuong_phan_logarit(img, c):
    global img_cur
    img_temp = np.array(img, 'float')
    # C là hệ số tỉ lệ thuận với độ tương phản
    log_image = int(c)*(np.log(img_temp+1))
    log_image = np.array(log_image, dtype='uint8') 
    img_temp1 = Image.fromarray(cv2.cvtColor(log_image, cv2.COLOR_BGR2RGB))
    # cập nhật ảnh trên frame 5
    img_cur = img_temp1
    return img_temp1


def tuong_phan_unsharp_mask_active(img, amount):
    global img_kq
    img_kq = tuong_phan_unsharp_mask(img, amount)
    update_(frame_5, img_kq)

def tuong_phan_unsharp_mask(img, amount):
    global img_cur
    # global sharpened
    kernel_size =(5, 5)
    sigma=1.0
    threshold=0
    # """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(img, kernel_size, sigma)
    sharpened = float(amount + 1) * img - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(img - blurred) < threshold
        np.copyto(sharpened, img, where=low_contrast_mask)
    img_temp1 = Image.fromarray(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
    img_cur = img_temp1
    return img_temp1
# def lam_net_opencv2_active(img, amount):
#     global img_kq
#     img_kq = lam_net_opencv2(img, amount)
#     update_(frame_5, img_kq)

# def lam_net_opencv2(img, amount):
#     global img_cur
#     global blurred
#     global sharpened
#     kernel_size =(5, 5)
#     sigma=1.0
#     threshold=0
#     # """Return a sharpened version of the image, using an unsharp mask."""
#     blurred = cv2.GaussianBlur(img, kernel_size, sigma)
#     sharpened = float(amount + 1) * img - float(amount) * blurred
#     sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
#     sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
#     sharpened = sharpened.round().astype(np.uint8)
#     if threshold > 0:
#         low_contrast_mask = np.absolute(img - blurred) < threshold
#         np.copyto(sharpened, img, where=low_contrast_mask)
#     img_temp1 = Image.fromarray(cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))
#     img_cur = img_temp1
#     return img_temp1

def call_lam_min(case):
    global slider_lam_mo_kernel_gaussian_ksize, slider_lam_mo_kernel_gaussian_sigma,slider_lam_mo_kernel_blur
    global slider_tuong_phan_logarit, slider_tuong_phan_unsharp_mask
    global slider_lam_min_median

    def slider_event(name_func,value):
                os.system('cls')
                print("{} - value Of Kernel Size: {}\n{}".format(name_func,int(value), "="*25))
                name_func(cv2.cvtColor(np.array(anh_goc), cv2.COLOR_BGR2RGB),value)
                chart_histogram()
    if(case == 1):
        if(slider_lam_min_median is None):
            slider_lam_min_median = slider = ctk.CTkSlider(master=frame_3_child_2,
                                    width=160,
                                    height=16,
                                    border_width=5.5,
                                    from_=0, 
                                    to=10,
                                    command=lambda value: slider_event(lam_min_median_active, value)
                                    )
            slider_lam_min_median.set(0)
            slider_lam_min_median.place(relx=0.35, rely=0.8, anchor='center')

        # Ẩn các thanh sliderbar của chức năng làm mờ
        if slider_lam_mo_kernel_gaussian_ksize is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_ksize", None)
        if slider_lam_mo_kernel_gaussian_sigma is not None:
            check_and_delete_slider("slider_lam_mo_kernel_gaussian_sigma", None)
        if slider_lam_mo_kernel_blur is not None:
            check_and_delete_slider("slider_lam_mo_kernel_blur", None)
        if slider_lam_mo_kernel_median is not None:
            check_and_delete_slider("slider_lam_mo_kernel_median", None)

        # Ẩn các thanh sliderbar của chức năng thay đổi độ tương phản
        if slider_tuong_phan_logarit is not None:
            check_and_delete_slider("slider_tuong_phan_logarit", None)
        if slider_tuong_phan_unsharp_mask is not None:
            check_and_delete_slider("slider_tuong_phan_unsharp_mask", None)

def lam_min_median_active(img, sigma):
    global img_kq
    img_kq = lam_min_median(img, sigma)
    update_(frame_5, img_kq)
def lam_min_median(img, sigma):
    global img_cur
    # Chuyển đổi sigma sang kiểu số thực
    sigma = float(sigma)

    # Áp dụng phép lọc Median với kernel size tính toán từ sigma
    kernel_size = int(sigma * 3)
    kernel_size += 1 if kernel_size % 2 == 0 else 0

    # Kiểm tra self.image có khác None hay không
    if img is not None:
        # Chuyển đổi ảnh từ đối tượng Image sang mảng numpy
        img_np = np.array(img)
        # Áp dụng phép lọc Median với kernel size tính toán từ sigma bằng OpenCV
        filtered_image = cv2.medianBlur(img, kernel_size)
        img_temp1 = Image.fromarray(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
        img_cur = img_temp1
        return img_temp1


# Hàm chọn chức năng - Radio-Button và gọi các 
# Phép xử lý tương ứng với Radio-Button đang chọn
def choose_filter():
    frame_5.delete('all')
    global img_f4
    global blur_tk  
    global anh_goc
    global img_cur

    def display_after_img():
        global anh_goc
        global blur_tk
        global img_cur
        max_size = (frame_5.winfo_width(), frame_5.winfo_height())
        img_resize_frame_5 = resize_image(img, max_size)
        # cập nhật ảnh đang nằm trên frame 5
        img_cur = img_resize_frame_5
        anh_goc = img_resize_frame_5
        blur_tk = ImageTk.PhotoImage(img_cur)
        x1 = frame_5.winfo_width() / 2
        y1 = frame_5.winfo_height() / 2
        frame_5.create_image(x1, y1, image=blur_tk, anchor="center", tags="image")

    if radio_var.get() == 1:
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        if(img is not None):
            os.system('cls');print("Bạn đang chọn chức năng: Làm mờ :)")
            menu = tk.Menu(root, tearoff=0)
            menu.add_command(label='Kernel Gaussian', command=lambda: (display_after_img(),chart_histogram(), call_lam_mo(1)))
            menu.add_command(label='Kernel Blur', command=lambda: (display_after_img(),chart_histogram(), call_lam_mo(2)))
            menu.add_command(label='Kernel Median', command=lambda: (display_after_img(),chart_histogram(), call_lam_mo(3)))
            menu.post(radiobutton_1.winfo_rootx(), radiobutton_1.winfo_rooty())

    if radio_var.get() == 2:
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        if(img is not None):
            os.system('cls');print("Bạn đang chọn chức năng: Thay đổi độ tương phản :)")
            menu = tk.Menu(root, tearoff=0)
            menu.add_command(label='Biến đổi Logarit', command=lambda: (display_after_img(),chart_histogram(), call_tuong_phan(1)))
            menu.add_command(label='Unsharp mask', command=lambda: (display_after_img(),chart_histogram(), call_tuong_phan(2)))
            menu.post(radiobutton_2.winfo_rootx(), radiobutton_2.winfo_rooty())
    
    if radio_var.get() == 3:
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        if(img is not None):
            os.system('cls');print("Bạn đang chọn chức năng: Làm min và giảm nhiễu :)")
            menu = tk.Menu(root, tearoff=0)
            menu.add_command(label='Median', command=lambda: (display_after_img(),chart_histogram(), call_lam_min(1)))
            menu.post(radiobutton_3.winfo_rootx(), radiobutton_3.winfo_rooty())

    if radio_var.get() == 4:
        img = img_f4
        if(img is None): messagebox.showerror('Error','Chưa Tải ảnh lên!')
        if(img is not None):
            os.system('cls');print("Bạn đang chọn chức năng: Tăng giảm sáng :)")
            menu = tk.Menu(root, tearoff=0)
            menu.add_command(label='Median', command=lambda: (display_after_img(),chart_histogram(), call_lam_min(1)))
            menu.post(radiobutton_3.winfo_rootx(), radiobutton_3.winfo_rooty())

root.mainloop()




