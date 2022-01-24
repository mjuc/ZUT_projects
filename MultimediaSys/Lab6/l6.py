import numpy as np
from numpy.lib.type_check import imag
import scipy.fftpack
import cv2

def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a.astype(float), axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a.astype(float), axis=0 , norm='ortho'), axis=1 , norm='ortho')

def zigzag(A):
    template= n= np.array([
            [0,  1,  5,  6,  14, 15, 27, 28],
            [2,  4,  7,  13, 16, 26, 29, 42],
            [3,  8,  12, 17, 25, 30, 41, 43],
            [9,  11, 18, 24, 31, 40, 44, 53],
            [10, 19, 23, 32, 39, 45, 52, 54],
            [20, 22, 33, 38, 46, 51, 55, 60],
            [21, 34, 37, 47, 50, 56, 59, 61],
            [35, 36, 48, 49, 57, 58, 62, 63],
            ])

    if len(A.shape)==1:
        B=np.zeros((8,8))
        for r in range(0,8):
            for c in range(0,8):
                B[r,c]=A[template[r,c]]
    else:
        B=np.zeros((64,))
        for r in range(0,8):
            for c in range(0,8):
                B[template[r,c]]=A[r,c]
    return B

def chromaSubsampling(fragment,variant):
    if variant == '4:4:4':
        res = fragment 
    elif variant == '4:2:2':
        res = fragment[:, ::2]
    return res

def chroma_resampling(fragment, chsub):
    if chsub == '4:4:4':
        return fragment
    elif chsub == '4:2:2':
        tab = np.tile(fragment[:, [0]], (1, 2))
        for i in range(1,fragment.shape[1]):
            tab = np.hstack((fragment, np.tile(fragment[:, [i]], (1, 2))))
        return tab

def separateIntoBlocks(image):
    pass

def encode(img):
    image = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb).astype(int)

