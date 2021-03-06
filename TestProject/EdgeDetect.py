import cv2
import numpy as np

from matplotlib import pyplot as plt
img = cv2.imread('messi56.png',0)
kernel = np.ones((5,5),np.float32)/25

blur = cv2.pyrDown(img)
blur2 = cv2.pyrUp(blur)
dst = cv2.filter2D(blur2,-1,kernel)
edges = cv2.Canny(dst,30,70)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()