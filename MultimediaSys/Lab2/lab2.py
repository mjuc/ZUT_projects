from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random
from numpy.core.fromnumeric import shape
from numpy.lib.function_base import copy
from progress.bar import Bar
#'0001.jpg','0003.jpg',
IMAGES = ['0009.png','0012.jpg']
GRAY_BITS = [1,2,4]
COLOR_BITS = [8,16]

PALLETES = [np.array([[0, 0, 0],
[0, 0, 1],
[0, 1, 0],
[0, 1, 1],
[1, 0, 0],
[1, 0, 1],
[1, 1, 0],
[1, 1, 1]]),
np.array([
[0, 0, 0],
[0, 1, 1],
[0, 0, 1],
[1, 0, 1],
[0, 0.5, 0],
[0.5, 0.5, 0.5],
[0, 1, 0],
[0.5, 0, 0],
[0, 0, 0.5],
[0.5, 0.5, 0],
[0.5, 0, 0.5],
[1, 0, 0],
[0.75, 0.75, 0.75],
[0, 0.5, 0.5],
[1, 1, 1],
[1, 1, 0]
]),
np.array([[0.0745098039216,0.090196078,0.105882353],
[0.0863,0.105882353,0.121568627],
[0.094117647,0.121568627,0.121568627],
[0.17254902,0.235294118,0.152941176],
[0,0,0],
[1,1,1],
[0.184313725,0.239215686,0.156862745],
[0.188235294,0.250980392,0.156862745],
[0.203921569,0.254901961,0.168627451],
[0.2,0.254901961,0.156862745],
[0.219607843,0.270588235,0.17254902],
[0.250980392,0.28627451,0.17254902]])]

def bitRed(img,n):
    if img.dtype != float:
        image = copy(img)/255
    else:
        image = copy(img)

    if len(img.shape) < 3:
        palette = np.linspace(0, 1, 2 ** n)
    else:
        p = (n-8)%7
        palette = PALLETES[p]
    return recolorImage(image,palette)

def recolorImage(image,palette):
    img = image.copy()
    if len(img.shape) < 3:
        r,c = img.shape
    else:
        r,c, channels = img.shape
    bar = Bar("Color fit",max=r*c)
    for row in range(r):
        for column in range(c):
            img[row,column] = colorFit(img[row,column],palette)
            bar.next()
    bar.finish()
    return img

def colorFit(col,palette):
    res = palette[np.argmin(np.linalg.norm(col - palette,axis=0))]
    return res
    
def randomDithering(image):
    img = copy(image)
    r,c = img.shape
    bar = Bar("Random ditheirng",max=r*c)
    for row in img:
        for pixel in row:
            tmp = random.random()
            if  pixel < tmp:
                pixel = 0
            else:
                pixel = 1
            bar.next()
    bar.finish()
    return img

def organizedDithering(image,bit):
    M = np.array([[0, 8, 2, 10],
                  [12, 4, 14, 6],
                  [3, 11, 1, 9],
                  [15, 7, 13, 5]
                  ])
    n = M.shape[0]
    img = copy(image)
    if len(img.shape) < 3:
        row,column = img.shape
        palette = np.linspace(0, 1, 2 ** bit)
    else:
        row,column, channels = img.shape
        p = (bit-8)%7
        palette = PALLETES[p]
    Mpre = (M+1) / n ** 2 - 0.5
    bar = Bar("Organized dithering",max=row*column)
    for r in range(row):
        for c in range(column):
            c = colorFit(img[r,c] + Mpre[r % n, c % n],palette)
            bar.next()
    bar.finish()
    return img

def floydSteinberg(image,bit):
    img = copy(image)
    if len(img.shape) < 3:
        row,column = img.shape
        palette = np.linspace(0, 1, 2 ** bit)
    else:
        row,column, channels = img.shape
        p = (bit-8)%7
        palette = PALLETES[p]
    bar = Bar('Floyd-Steinberg',max=row*column)
    for r in range(row):
        for c in range(column):
            oldpixel = copy(img[r,c])
            newpixel  = colorFit(img[r,c], PALLETES[1])
            quantErr = oldpixel - newpixel
            if r < row - 1:
                    img[r + 1][c] = img[r + 1][c] + (quantErr * (7 / 16))
            if r > 0 and c < column - 1:
                img[r - 1][c + 1] = img[r - 1][c + 1] + (quantErr * (3 / 16))
            if c < column - 1:
                img[r][c + 1] = img[r][c + 1] + (quantErr * (5 / 16))
            if r < row - 1 and c < column - 1:
                img[r + 1][c + 1] = img[r + 1][c + 1] + (quantErr * (1 / 16))
            bar.next()
    bar.finish()
    return img

i = 2
for im in IMAGES:
    print(im)
    if i < 2:
        image = cv2.cvtColor(cv2.imread(im),cv2.COLOR_BGR2RGB)
        j = 0
        for bit in COLOR_BITS:
            print(bit," bits")
            tmp = bitRed(image,bit)
            plt.imsave("{}{}bit.jpg".format(im,bit),tmp)
            plt.imsave("orgdith_{}_{}.jpg".format(im,bit),organizedDithering(tmp,bit))
            plt.imsave("fsdith_{}_{}.jpg".format(im,bit),floydSteinberg(tmp,bit))
            j+=1
    else:
        image = cv2.cvtColor(cv2.imread(im),cv2.COLOR_BGR2GRAY)
        for bit in GRAY_BITS:
            print(bit," bit(s)")
            tmp = bitRed(image,bit)
            plt.imsave("{}{}bit.jpg".format(im,bit),tmp)
            plt.imsave("randdith_{}.jpg".format(im),randomDithering(tmp))
            plt.imsave("orgdith_{}_{}.jpg".format(im,bit),organizedDithering(tmp,bit))
            plt.imsave("fsdith_{}_{}.jpg".format(im,bit),floydSteinberg(tmp,bit))
    i+=1
for bit in COLOR_BITS:
    image = cv2.cvtColor(cv2.imread('0002.jpg'),cv2.COLOR_BGR2RGB)
    tmp = bitRed(image,bit)
    plt.imsave("z3{}bits.jpg".format(bit),recolorImage(tmp,PALLETES[2]))
