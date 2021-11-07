import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
from numpy.lib.function_base import copy

IMAGES = ['0001.jpg','0002.jpg','0003.jpg','0004.png','0005.tif',
        '0006.tif','0008.png','0009.png','0010.jpg','0011.jpg',
        '0012.jpg','0013.jpg','0014.jpg','0015,jpg','0016.jpg']

PALLETES = [np.array([[0, 0, 0],
[0, 0, 1],
[0, 1, 0],
[0, 1, 1],
[1, 0, 0],
[1, 0, 1],
[1, 1, 0],
[1, 1, 1]])]

def readImage(imName):
    img = cv2.imread(imName)
    if (img.dtype == "uint8"):
        img = np.float32(img/255)
        return img
    else:
        return img

def colorFit(col,palette):
    return palette[np.argmin(np.linalg.norm(col - palette,axis=1))]
    
def recolorImage(image,palette,n=1,Mpre=np.zeros((1,1))):
    img = copy(image)
    i = 0
    for row in img:
        j = 0
        for pixel in row:
            pixel=colorFit(pixel + Mpre[i % n,j % n],palette)
            j+=1
        i+=1
    return img

def randomDithering(image):
    img = copy(image)
    for row in img:
        for pixel in row:
            tmp = random()
            if  pixel < tmp:
                pixel = 0
            else:
                pixel = 1
    return img

def organizedDithering(image):
    M = np.array([[0, 8, 2, 10],
                  [12, 4, 14, 6],
                  [3, 11, 1, 9],
                  [15, 7, 13, 5]
                  ])
    n = M.shape[0]
    Mpre = (M+1) / n ** 2 - 0.5
    img = recolorImage(image,PALLETES[0],n,Mpre)
    return img

def floydSteinberg(image):
    img = copy(image)
    row,column = img.shape
    for r in range(row):
        for c in range(column):
            oldpixel = copy(img[r,c])
            newpixel  = colorFit(img[r,c], PALLETES[0])
            quantErr = oldpixel - newpixel
            if r < row - 1:
                    img[r + 1][c] = img[r + 1][c].copy() + quantErr * 7 / 16
            if r > 0 and c < column - 1:
                img[r - 1][c + 1] = img[r - 1][c + 1].copy() + quantErr * 3 / 16
            if c < column - 1:
                img[r][c + 1] = img[r][c + 1].copy() + quantErr * 5 / 16
            if r < row - 1 and c < column - 1:
                img[r + 1][c + 1] = img[r + 1][c + 1].copy() + quantErr * 1 / 16

img = readImage(IMAGES[3])
#recolorImage(img,PALLETES[0])
