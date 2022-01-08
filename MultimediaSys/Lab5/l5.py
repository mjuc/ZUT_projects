from numpy.lib.function_base import copy
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from progress.bar import Bar

u=255

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

def uLawEncode(input):
    res = []
    bar = Bar("muLaw encoding",max=len(input))
    for i in input:
        res.append(np.sign(i)*(np.log(1 + (u * np.abs(i)))/np.log(1 + u)))
        bar.next()
    bar.finish()
    return np.array(res)

def uLawDecode(input):
    res = []
    bar = Bar("muLaw decoding",max=len(input))
    for i in input:
        res.append((np.sign(i)*(((1+u)**np.abs(i))-1))/u)
        bar.next()
    bar.finish()
    return np.array(res)

def DPCMEncode(input,bit=8):
    res = []
    bar = Bar("DPCM encoding",max=len(input))
    res.append(input[0])
    e = input[0]
    bar.next()
    for i in range(1,len(input)):
        tmp = input[i] - e
        y = bitRed(tmp,bit)
        e += y
        res.append(y)
        bar.next()
    bar.finish()
    return np.array(res)

def DPCMDecode(input):
    res = []
    bar = Bar("DPCM decoding",max=len(input))
    res.append(input[0])
    bar.next()
    for i in range(1,len(input)):
        res.append(res[i-1]-input[i])
        bar.next()
    bar.finish()
    return np.array(res).astype(np.int32)

FILES = ['sing_medium1.wav','sing_medium2.wav','sing_low1.wav','sing_low2.wav','sing_high2.wav']
BITS = [8,6,4,2]

for file in FILES:
    print("Reading {}".format(file))
    snd, fs = sf.read(file, dtype=np.int32)
    for bit in BITS:
        sound = bitRed(snd,bit)
        x = np.linspace(0,1000,1000)
        plt.plot(x,sound[:1000])
        plt.savefig("{}_{}bit_orgPlot.jpg".format(file,bit))
        plt.clf()
        ulaw = uLawEncode(sound)
        dulaw = uLawDecode(ulaw)
        plt.plot(x,dulaw[:1000])
        plt.savefig("{}_{}bit_postULAW.jpg".format(file,bit))
        plt.clf()
        sf.write("{}_{}bit_afterUlaw.wav".format(file,bit),dulaw,fs)
        dpcm = DPCMEncode(sound,bit)
        ddpcm = DPCMDecode(dpcm)
        plt.plot(x,ddpcm[:1000])
        plt.savefig("{}_{}bit_postDPCM.jpg".format(file,bit))
        plt.clf()
        sf.write("{}_{}_afterDPCM.wav".format(file,bit),ddpcm,fs)