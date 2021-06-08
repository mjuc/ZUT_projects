import math as mt
import numpy as np
import imageio as im
import matplotlib.pyplot as mpl
import matplotlib.image as img

f = 2.4

fs = [20,21,30,45,50,100,150,200,250,1000]

for j in fs:
    t = np.arange(0,1,1/j)
    sin = []
    for i in t:
        sin.append(mt.sin(2*mt.pi*f))
    print(t)
    print(sin)

imag = im.imread("img.png")

shape = imag.shape
size = len(imag[-1])

print(imag)
gr2 = []
gr3 = imag

def rgb2gr(rgb):
    return ((max(rgb[...,:3])*min(rgb[...,:3]))/2)

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.21, 0.72, 0.07])

gr1 = rgb2gr(rgb2gr)

gr2 = np.mean(imag,-1)

gr3 = rgb2gray(imag)

hist1 = np.histogram(gr1)
hist2 = np.histogram(gr2)
hist3 = np.histogram(gr3)

hist_red = np.histogram(gr1,16)

mpl.show(hist1)
mpl.show(hist2)
mpl.show(hist3)

mpl.imshow(gr1)
mpl.imshow(gr2)
mpl.imshow(gr3)
mpl.imshow(imag)
