import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)
    if isinstance(obj,np.ndarray):
        size += obj.nbytes
    elif isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def RLEencode(input):
    tmp = input.copy()
    tmp = tmp.flatten()
    cnt = 0
    res = []
    for i in range(len(tmp)):
        if i != 0 and tmp[i] != tmp[i - 1]:
            res.append(cnt)
            res.append(tmp[i - 1])
            cnt = 0
        if i == len(tmp) - 1:
            cnt += 1
            res.append(cnt)
            res.append(tmp[i])
        cnt += 1
    return res

def RLEdecode(input, shape):
    res = []
    cnt = []
    val = []
    for i in range(len(input)):
        if (i % 2 != 0):
            val.append(input[i])
        else:
            cnt.append(input[i])

    j = 0
    for i in cnt:
        for k in range(i):
            res.append(val[j])
        j+=1
            
    res = np.array(res).reshape(shape)
    return res

class QuadTree:
    
    def insert(self, xMIN, xMAX, yMIN, yMAX):
        self.xMIN = xMIN
        self.xMAX = xMAX
        self.yMIN = yMIN
        self.yMAX = yMAX
        self.node = []
        self.leaf = 0
        
    def setLeaf(self, leaf):
        self.leaf = leaf

def equalEval(data):
    first=data[0]
    second=data[:,0]
    
    for i in range(data.shape[0]):
        if not np.all(data[i] == first):
            return False
    for j in range(data.shape[1]):
        if not np.all(data[:,j] == second):
            return False
    return True

def quadRec(input, xMIN, xMAX, yMIN, yMAX):   
    tree = QuadTree()
    tree.insert(xMIN, xMAX, yMIN, yMAX)
    if equalEval(input[xMIN:xMAX, yMIN:yMAX]):
        tree.setLeaf(input[xMIN, yMIN])
    else:
        if (yMAX - yMIN) == 1:
            tree.node.append(quadRec(input, xMIN, (xMAX + xMIN) // 2, yMIN, yMAX))
            tree.node.append(quadRec(input, ((xMAX + xMIN) // 2), xMAX, yMIN, yMAX))
        elif (xMAX - xMIN) == 1:
            tree.node.append(quadRec(input, xMIN, xMAX, yMIN, (yMIN + yMAX) // 2 ))
            tree.node.append(quadRec(input, xMIN, xMAX, ((yMIN + yMAX) // 2 ), yMAX)) 
        else:
            tree.node.append(quadRec(input, xMIN, (xMAX + xMIN) // 2, yMIN, (yMIN + yMAX) // 2 )) 
            tree.node.append(quadRec(input, ((xMAX + xMIN) // 2), xMAX, ((yMIN + yMAX) // 2 ), yMAX)) 
            tree.node.append(quadRec(input, ((xMAX + xMIN) // 2), xMAX, yMIN, (yMIN + yMAX) // 2 )) 
            tree.node.append(quadRec(input, xMIN, (xMAX + xMIN) // 2, ((yMIN + yMAX) // 2 ), yMAX))
    return tree

def quadEncode(input):
    xMIN = 0
    xMAX = input.shape[0]
    yMIN = 0
    yMAX = input.shape[1]
    res = quadRec(input, xMIN, xMAX, yMIN, yMAX)
    return res

def quadDecode(tree, iter, dec):
    if iter == 0:
        dec = np.zeros((tree.xMAX, tree.yMAX, 3)).astype(int)
        dec = quadDecode(tree, 1, dec)
    else:
        if len(tree.node) == 0:
            dec[tree.xMIN:tree.xMAX, tree.yMIN:tree.yMAX] = tree.leaf
        else:
            for i in range(len(tree.node)):
                dec = quadDecode(tree.node[i], 1, dec)
    return dec

IMAGES = ["0001.jpg","tec.jpeg","doc.png",]

for image in IMAGES:
    print(image)
    img = mpimg.imread(image)
    orgSize = get_size(img)
    print("Image size: ",orgSize)
    print("RLE encode")
    enc = RLEencode(img)
    encSize = get_size(enc)
    print("Size after RLE compression: ",encSize)
    print("RLE compression effectiveness: ",encSize/orgSize," %")
    print("RLE decode")
    dec = RLEdecode(enc,img.shape)
    plt.imshow(dec)
    plt.savefig("{}RLEdecompressed.jpg".format(image))
    plt.clf
    enc = None
    encSize = None
    dec = None
    print("Quad Tree compression")
    qEnc = quadEncode(img)
    # qeSize = get_size(qEnc)
    # print("Size after Quad TRee compression: ",qeSize)
    # print("Quad Tree effectiveness: ",qeSize/orgSize," %")
    print("Quad Tree decompression")
    qDec = quadDecode(qEnc,0,[])
    plt.imshow(qDec)
    plt.savefig("{}quadTreeDecompressed.jpg".format(image))
    plt.clf
    qEnc = None
    qDec = None