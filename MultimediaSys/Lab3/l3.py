from typing import SupportsRound
import numpy as np
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf
from numpy.lib.function_base import copy
from scipy.interpolate import interp1d

def bitRed(snd,n):
    oldtype = snd.dtype
    mn = np.iinfo(oldtype).min
    mx = np.iinfo(oldtype).max

    if snd.dtype != float:
        sound = float(copy(snd))
    else:
        sound = copy(snd)
    
    sound = (sound - mn)/(mx - mn)
    sound = sound * (2 ** n)
    sound = np.round(sound)
    sound = sound / (2 ** n)
    sound = ((sound * (mx - mn)) + mn).astype(oldtype)
    return sound

def dM(snd,n,Fs):
    nFs = Fs/n
    sound = snd[0:snd.size - 1:n]
    return nFs,sound

def interp(snd,Fs,Fs2):
    T = (snd.size - 1)/Fs
    t1 = np.linspace(0,T,snd.size)
    xt = (Fs2 * T) + 1
    t2 = np.linspace(0,T,xt)

    intr = interp1d(t1,snd)
    intr_nonlin = interp1d(t1,snd,kind="cubic")

    res_lin = intr(t2)
    res_nonlin = intr_nonlin(t2)