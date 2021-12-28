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
        sound = copy(snd.astype(float))
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
    tmp = snd[::n]
    return int(nFs),tmp

def interp(snd,Fs,Fs2):
    T = (snd.size - 1)/Fs
    t1 = np.linspace(0,T,len(snd))
    xt = int((Fs2 * T) + 1)
    t2 = np.linspace(0,T,xt)

    intr = interp1d(t1,snd)
    intr_nonlin = interp1d(t1,snd,kind="cubic")

    res_lin = intr(t2)
    res_nonlin = intr_nonlin(t2)
    return (res_lin,res_nonlin)

BITS = [4,8,16,24]
FREQS = [2000,4000,8000,16000,24000,41000,16950]
FILES = ['sin_60Hz.wav','sin_440Hz.wav','sin_8000Hz.wav','sin_combined.wav','sing_high2.wav','sing_low1.wav','sing_low2.wav','sing_medium1.wav','sing_medium2.wav']

i = 0
fsize=2**8

for file in FILES:
    print(file)
    sound, fs = sf.read(file, dtype=np.int32)
    plt.figure(figsize=(8,8))
    plt.clf()
    plt.plot(np.linspace(0,(0.001),int(0.001*fs)),sound[:int(0.001*fs)])
    plt.savefig("{}org.jpg".format(file))
    tmp = fftpack.fft(sound,fsize)
    plt.clf()
    plt.figure(figsize=(8,8))
    plt.plot(np.arange(0,fs/2,fs/fsize),20*np.log10(np.abs(tmp[:fsize//2])))
    plt.savefig("{}plot.jpg".format(file))
    nfs, res = dM(sound,int(48000/44100),fs)
    tmp = fftpack.fft(res,fsize)
    sf.write("{}_dec.wav".format(file),res,nfs)
    plt.clf()
    plt.figure(figsize=(8,8))
    plt.plot(np.linspace(0,nfs/2,int(fsize/2)),20*np.log10(np.abs(tmp[:fsize//2])))
    plt.savefig("{}_dec.wav_plot.jpg".format(file))
    if i < 4:
        for bit in BITS:
            sf.write("{}_{}bit.wav".format(file,bit),bitRed(sound, bit),fs)
            tmp = fftpack.fft(bitRed(sound, bit),fsize)
            plt.clf()
            plt.figure(figsize=(8,8))
            plt.plot(np.arange(0,fs/2,fs/fsize),20*np.log10(np.abs(tmp[:fsize//2])))
            plt.savefig("{}_{}plot.jpg".format(file,bit))
        for fr in FREQS:
            ns, nl = interp(sound,fs,fr)
            sf.write("lin{}_{}hz.wav".format(file,fr),ns,fr)
            sf.write("nonlin{}_{}hz.wav".format(file,fr),nl,fr)
            lins = fftpack.fft(ns,fsize)
            nonlins = fftpack.fft(nl,fsize)
            plt.clf()
            plt.figure(figsize=(8,8))
            plt.plot(np.arange(0,fs/2,fs/fsize),20*np.log10(np.abs(lins[:fsize//2])))
            plt.savefig("lin{}_{}hz_plot.jpg".format(file,fr))
            plt.clf()
            plt.figure(figsize=(8,8))
            plt.plot(np.arange(0,fs/2,fs/fsize),20*np.log10(np.abs(nonlins[:fsize//2])))
            plt.savefig("nonlin{}_{}hz_plot.jpg".format(file,fr))
    else:
        for bit in BITS:
            sf.write("{}_{}bit.wav".format(file,bit),bitRed(sound, bit),fs)
        for fr in FREQS:
            if fr != 16950:
                ns, nl = interp(sound,fs,fr)
                sf.write("lin{}_{}hz.wav".format(file,fr),ns,fr)
                sf.write("nonlin{}_{}hz.wav".format(file,fr),nl,fr)
    i+=1
