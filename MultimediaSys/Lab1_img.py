import numpy as np
import matplotlib.pyplot as plt
import cv2

#matplotlib
imgc = plt.imread('pic1.png')
# print(img1.dtype)
# print(img1.shape)
# img2 = plt.imread('pic2.jpg')
# print(img2.dtype)
# print(img2.shape)

# R=img1[:,:,0]
# G=img1[:,:,1]
# B=img1[:,:,2]
# Y1=0.299 * R + 0.587 * G +0.114 * B
# Y2=0.2126 * R + 0.7152 * G + 0.0722 * B
# plt.imshow(Y2,cmap=plt.cm.gray)
# plt.show()

# plt.imshow(img1)
# plt.show()

#opencv
#imgc = cv2.imread('pic1.png')

print(imgc.dtype)
print(imgc.shape)

Rc=imgc[:,:,0]
Gc=imgc[:,:,1]
Bc=imgc[:,:,2]
Yc1=0.299 * Rc + 0.587 * Gc +0.114 * Bc
Yc2=0.2126 * Rc + 0.7152 * Gc + 0.0722 * Bc

plt.subplot(3,3,1)
plt.imshow(imgc)
plt.subplot(3,3,2)
plt.imshow(Yc1,cmap=plt.cm.gray)
plt.subplot(3,3,3)
plt.imshow(Yc2,cmap=plt.cm.gray)
plt.subplot(3,3,4)
plt.imshow(Rc,cmap=plt.cm.gray)
plt.subplot(3,3,5)
plt.imshow(Gc,cmap=plt.cm.gray)
plt.subplot(3,3,6)
plt.imshow(Bc,cmap=plt.cm.gray)
plt.subplot(3,3,7)
i = imgc.copy()
i[:,:,1:2]=0
plt.imshow(i)
plt.subplot(3,3,8)
i = imgc.copy()
i[:,:,0:2]=0
plt.imshow(i)
plt.subplot(3,3,9)
i = imgc.copy()
i[:,:,0:1]=0
plt.imshow(i)
plt.show()
