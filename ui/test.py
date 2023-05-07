


#%matplotlib notebook
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




#display image
def displayImg(img):
    plt.axis("off")
    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))






#define a box filter
filterSize = 5
boxFilter = (1/filterSize**2) * np.ones((filterSize,filterSize))

#read image
img = cv2.imread("C:/Users/levan/Desktop/images/image01.jpg", 0)
h, w = img.shape

#pad image
paddingThickness = filterSize//2
paddedImg = np.pad(img, paddingThickness,constant_values=(0))
displayImg(img)
resImg = np.array([[(boxFilter*paddedImg[y:y+filterSize,x:x+filterSize]).sum() for x in range(w)] for y in range(h)],'uint8')
plt.figure(1,figsize=(100,100))
ax = plt.subplot(121)
ax.set_title("Original Image",fontsize=100)
displayImg(img)
ax = plt.subplot(122) 
ax.set_title("Filtered image",fontsize=100)
displayImg(resImg)
plt.show()
