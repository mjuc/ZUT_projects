import math
import numpy as np

MB = 1048576
GB = 1073741824
TB = 1099511627776

def a4Amount(bytes):
    maxMBytesperUnit = 8840/MB
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))

def hddAmount(bytes):
    maxMBytesperUnit = (4 * TB)/MB
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))

def ssdAmount(bytes):
    maxMBytesperUnit = TB/MB
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))

def cdAmount(bytes):
    maxMBytesperUnit = 700
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))

def dvdAmount(bytes):
    maxMBytesperUnit = (4.7 * GB)/MB
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))

def microSDAmount(bytes):
    maxMBytesperUnit = (64 * GB)/MB
    res = bytes/maxMBytesperUnit
    return(math.ceil(res))
    
def aggregateData(bytes):
    print("##########################")
    a = a4Amount(bytes)
    print("A4s needed: ",a)
    print("Mass: ", a * 0.005, " kg")
    print("Volume: ", a * 6.1746, " cm3")
    print("Price: ", a *0.05, " PLN")
    print("##########################")
    h = hddAmount(bytes)
    print("HDDs needed: ", h)
    print("Mass: ", h * 0.23, " kg")
    print("Volume: ", a * 187.9064, " cm3")
    print("Price: ", a * 399, " PLN")
    print("##########################")
    s = ssdAmount(bytes)
    print("SSDs needed: ",s)
    print("Mass: ", s * 0.057, " kg")
    print("Volume: ", a * 47.498, " cm3")
    print("Price: ", a * 399, " PLN")
    print("##########################")
    c = cdAmount(bytes)
    print("CDs needed: ",c)
    print("Mass: ", c * 0.015, " kg")
    print("Volume: ", c * 4.5215, " cm3")
    print("Price: ", c * 2.99, " PLN")
    print("##########################")
    d = dvdAmount(bytes)
    print("DVDs needed: ",d)
    print("Mass: ", d * 0.015, " kg")
    print("Volume: ", d * 4.5215, " cm3")
    print("Price: ", d * 2.99, " PLN")
    print("##########################")
    m = microSDAmount(bytes)
    print("Micro SDs needed: ",m)
    print("Mass: ", d * 0.002, " kg")
    print("Volume: ", d * 0.0016, " cm3")
    print("Price: ", d * 68, " PLN")
    print("##########################")


#book 34 lines 68 chars 387 pages 894744 chars overall
#enc bytannica ~300000000 chars as per wikipedia
#english wikipedia 24000000000 chars as per wikipedias assesment
#photo 108 Mpx 3 bytes per pixel 12 000 000 pixels in photo
#vid vhs 150000 pixels 3 bytes per pixel 30 fps
#vid full hd 3 bytes per pixel 2073600 pixels 30 fps
#vid 4k 3 bytes per pixel 8847360 pixels 30 fps
#yt data for feb 2020 500h of vid a minute 

chars = 894744
bytes = chars * 16
print("Book")
print(bytes, " B")
aggregateData(bytes)
print("Encyclopeadia Brittanica")
bytes = 3000000000 * 16
print(bytes, " B")
aggregateData(bytes)
print("108 Mpix photo")
bytes = 3 * 12000000
print(bytes, " B")
aggregateData(bytes)
print("VHS standard video 1,5h long")
bytes = 3 * 150000 * 30 * 3600 * 1.5
print(bytes, " B")
aggregateData(bytes)
print("Full HD video 1,5h long")
bytes = 3 * 2073600 * 30 * 3600 * 1.5
print(bytes, " B")
aggregateData(bytes)
# print("4K video 1,5h long")
# bytes = 3 * (8847360/TB) * 30 * 3600 * 1,5
# print(bytes.astype(np.float32), " B")
# aggregateData(bytes.astype(np.float32))
# print("YouTube videos added in one day assuming average video is Full HD")
# bytes = 500 * 3600 * 3 * 2073600 * 30 * 24 * 3600
# print(bytes.astype(np.float32)/TB, " TB")
# aggregateData(bytes)