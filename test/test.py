
import cv2 as cv2
from matplotlib import pyplot as plt
import numpy as np

img_bgr = cv2.imread('C:/Users/levan/Desktop/images/anh_toi.jpg')
img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img = np.array(img_bgr, 'float')
maxV = 255 /np.log(1 + np.max(img_bgr))
vars = np.linspace(0, maxV, 8, dtype=int)
plt.figure(figsize=(3,3), dpi=600)
subf=plt.subplot(3,3,1)
subf.imshow(img_bgr)
subf.set_title('Anh goc');subf.axis('off')

for i,c in enumerate(vars):
    log_image = c *(np.log(img+1))
    log_image = np.array(log_image, dtype='uint8')
    subf=plt.subplot(3,3,i+2)
    subf.imshow(log_image)
    subf.set_title('c='+str(c)); subf.axis('off')
plt.rcParams.update({'font.size': 7})
plt.figure(dpi=600)
plt.show()
# plt.show()
