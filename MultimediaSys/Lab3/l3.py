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
    sound = snd[0:snd.size - 1:n]
    return int(nFs),sound

def interp(snd,Fs,Fs2):
    T = (snd.size - 1)/Fs
    t1 = np.linspace(0,T,len(snd)-1)
    xt = int((Fs2 * T) + 1)
    t2 = np.linspace(0,T,xt)

    intr = interp1d(t1,snd)
    intr_nonlin = interp1d(t1,snd,kind="cubic")

    res_lin = intr(t2)
    res_nonlin = intr_nonlin(t2)
    return (res_lin,res_nonlin)

BITS = [4,8,16,24]
FREQS = [2000,4000,8000,16000,24000,41000,16950]
FILES = ['sin_60Hz.wav','sin_440Hz.wav','sin_8000Hz.wav','sin_combined.wav','sing_high1.wav','sing_high2.wav','sing_low1.wav','sing_low2.wav','sing_medium1.wav','sing_medium2.wav']

# i = 0
# for file in FILES:
#     sound, fs = sf.read(file, dtype=np.int32)
#     if i < 4:
#         for bit in BITS:
#             sf.write("{}_{}bit.wav".format(file,bit),bitRed(sound, bit),fs)
#         for fr in FREQS:
#             ns, nl = interp(sound,fs,fr)
#             sf.write("lin{}_{}hz.wav".format(file,fr),ns,fr)
#             sf.write("nonlin{}_{}hz.wav".format(file,fr),nl,fr)
#     else:
#         for bit in BITS:
#             sf.write("{}_{}bit.wav".format(file,bit),bitRed(sound, bit),fs)
#         for fr in FREQS:
#             if fr != 16950:
#                 ns, nl = interp(sound,fs,fr)
#                 sf.write("lin{}_{}hz.wav".format(file,fr),ns,fr)
#                 sf.write("nonlin{}_{}hz.wav".format(file,fr),nl,fr)
#     i+=1

# for file in FILES:
#     sound, fs = sf.read(file,dtype = np.int32)
#     nfs, res = dM(sound,4,fs)
#     sf.write("{}_dec.wav".format(file),res,nfs)

# PLOT_FILES = ['sin_60Hz.wav','sin_440Hz.wav','sin_8000Hz.wav','sin_combined.wav']
# for file in PLOT_FILES:
#     t = 500
#     for bit in BITS:
#         sound , fs = sf.read('{}_{}bit.wav'.format(file,bit))
#         tmp = []
#         for i in range(t):
#             tmp.append(sound[i])
#         plt.plot(np.linspace(0,t,t),tmp)
#         plt.savefig("{}_{}bit_plot.jpg".format(file,bit))
#     for freq in FREQS:
#         lins, a = sf.read("lin{}_{}hz.wav".format(file,freq))
#         nonlins, b = sf.read("nonlin{}_{}hz.wav".format(file,freq))
#         lintmp = []
#         nonlintmp = []
#         for i in range(t):
#             lintmp.append(lins[i])
#             nonlintmp.append(nonlins[i])
#         plt.plot(np.linspace(0,t,t),lintmp)
#         plt.savefig("lin{}_{}hz_plot.jpg".format(file,freq))
#         plt.plot(np.linspace(0,t,t),nonlintmp)
#         plt.savefig("nonlin{}_{}hz_plot.jpg".format(file,freq))

sound, fs = sf.read("sin_60Hz.wav_dec.wav")
t = 500
tmp = []
for i in range(t):
    tmp.append(sound[i])
plt.plot(np.linspace(0,t,t),tmp)
plt.savefig("sin_60Hz.wav_dec.wav_plot.jpg")