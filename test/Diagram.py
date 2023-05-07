# import tkinter as tk
# from tkinter import filedialog
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import cv2

# # Load ảnh từ file
# file_path = filedialog.askopenfilename()
# img = cv2.imread(file_path)
# # Tạo biểu đồ histogram của ảnh
# fig = Figure(figsize=(5, 4), dpi=100)
# ax = fig.add_subplot(111)
# ax.hist(img.ravel(), bins=256, range=(0, 255))
# ax.set_xlabel('Pixel value')
# ax.set_ylabel('Frequency')
# ax.set_title('Histogram')

# # Chuyển đổi biểu đồ thành widget tkinter
# root = tk.Tk()
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# # Hiển thị cửa sổ tkinter
# root.mainloop()
######################################################################################################################
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# from tkinter import filedialog

# # Load image
# file_path = filedialog.askopenfilename()
# img = cv2.imread(file_path)

# # Split channels
# b, g, r = cv2.split(img)

# # Create color maps for each channel
# cm_r = plt.cm.colors.LinearSegmentedColormap.from_list('Reds', [(1, 0, 0), (1, 1, 1)], N=256)
# cm_g = plt.cm.colors.LinearSegmentedColormap.from_list('Greens', [(0, 1, 0), (1, 1, 1)], N=256)
# cm_b = plt.cm.colors.LinearSegmentedColormap.from_list('Blues', [(0, 0, 1), (1, 1, 1)], N=256)

# # Plot histograms with color maps
# fig, ax = plt.subplots(figsize=(10, 5))

# # Plot red channel histogram
# hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
# ax.fill_between(np.arange(256), np.ravel(hist_r), color=cm_r(hist_r / np.max(hist_r)), alpha=0.5, label='Red')

# # Plot green channel histogram
# hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
# ax.fill_between(np.arange(256), np.ravel(hist_g), color=cm_g(hist_g / np.max(hist_g)), alpha=0.5, label='Green')

# # Plot blue channel histogram
# hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
# ax.fill_between(np.arange(256), np.ravel(hist_b), color=cm_b(hist_b / np.max(hist_b)), alpha=0.5, label='Blue')

# # Configure plot
# ax.set_xlim([0, 256])
# ax.set_xlabel('Pixel Value')
# ax.set_ylabel('Pixel Count')
# ax.set_title('RGB Histogram')
# ax.legend()

# plt.show()

###########################################################################################################

import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Load image
file_path = filedialog.askopenfilename()
img = cv2.imread(file_path)

# Split channels
b, g, r = cv2.split(img)
print(np.max(r))
print(np.max(g))
print(np.max(b))

# Create color maps for each channel
cm_r = plt.cm.colors.LinearSegmentedColormap.from_list('Reds', [(1, 0, 0), (1, 1, 1)], N=256)
cm_g = plt.cm.colors.LinearSegmentedColormap.from_list('Greens', [(0, 1, 0), (1, 1, 1)], N=256)
cm_b = plt.cm.colors.LinearSegmentedColormap.from_list('Blues', [(0, 0, 1), (1, 1, 1)], N=256)

# Create a Tkinter window
root = tk.Tk()
root.title('RGB Histogram')
root.geometry('200x300')
# Create a frame for the plot
frame = tk.Frame(root)
frame.pack()

# Create a Figure object and a canvas for it
fig = plt.Figure(figsize=(10, 5))
canvas = FigureCanvasTkAgg(fig, master=frame)

# Add an Axes to the Figure
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
ax.set_title('RGB Histogram')
ax.legend()
ax.set_axis_off()
ax.legend().remove()

# Add the canvas to the frame
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()

#==============================================Test===============================