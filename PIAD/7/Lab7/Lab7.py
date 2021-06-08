import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import scipy as sp
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D
from sklearn import mixture
from copy import copy, deepcopy
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from scipy.cluster import hierarchy
from sklearn.metrics import jaccard_score
from sklearn.decomposition import PCA
import sys
import itertools

np.set_printoptions(threshold=sys.maxsize)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def distp(X, C, e=1):
    dimX = np.shape(X)[0];
    dimC = np.shape(C)[0]
    wyn = np.zeros((dimX, dimC))
    temp = 0
    for index_i, arg_x in enumerate(X):
        for index_j, arg_c in enumerate(C):
            for ind in range(np.shape(arg_c)[0]):
                temp += np.power((arg_x[ind] - arg_c[ind]), 2)
            wyn[index_i, index_j] = np.sqrt(temp)
            temp = 0
    return wyn

def distm(X, C, V):
    return np.sqrt((X - C) * np.power(V, -1) * np.transpose(X - C))

def new_C(C, X, pos):
    suma = []
    for i in range(np.shape(C[0])[0]):
        suma.append(int(0))
    count = 0
    for i in range(np.shape(C)[0]):
        for j in range(np.shape(pos)[0]):
            if pos[j] == i:
                for k in range(np.shape(suma)[0]):
                    suma[k] += X[j][k]
                count += 1;
        if count != 0:
            for k in range(np.shape(suma)[0]):
                C[i][k] = suma[k] / count
                suma[k] = 0
            count = 0
        else:
            for k in range(np.shape(suma)[0]):
                C[i][k] = np.random.randint(np.amin(X, axis=0)[k] * 1.25, np.amax(X, axis=0)[k] * 0.75)
    return None

def kmean(X, k, sort=False, vis=False):
    Maksimum = np.amax(X, axis=0)
    Minimum = np.amin(X, axis=0)
    xlim_MAX = np.amax(np.array(X))
    ylim_MIN = np.amin(np.array(X))

    C = []
    for i in range(k):
        temp = []
        for j in range(np.shape(X)[1]):
            temp.append(np.random.uniform(Minimum[j], Maksimum[j], 1))
        C.append(temp.copy())
        temp.clear()
    C = np.array(C)

    if vis == True:
        colors = itertools.cycle(["r.", "y.", "g.", "m.", "c."])
        if np.shape(X)[1] == 3:
            ax = plt.axes(projection='3d')
            plt.xlim(ylim_MIN, xlim_MAX)
            plt.ylim(ylim_MIN, xlim_MAX)
            ax.plot3D(X.values[:, 0], X.values[:, 1], X.values[:, 2], '.')
            for j in range(k):
                ax.plot3D(C[j][0], C[j][1], C[j][2], next(colors), markersize=12)
        elif np.shape(X)[1] == 2:
            plt.xlim(ylim_MIN, xlim_MAX)
            plt.ylim(ylim_MIN, xlim_MAX)
            plt.plot(X[:, 0], X[:, 1], '.')
            for j in range(k):
                plt.plot(C[j][0], C[j][1], next(colors), markersize=12)
        elif np.shape(X)[1] == 1:
            plt.xlim(ylim_MIN, xlim_MAX)
            plt.plot(X.values[:, 0], '.')
            for j in range(k):
                plt.plot(C[j][0], next(colors), markersize=12)
        plt.show()

    temp = distp(np.array(X), C)
    pos = np.argmin(temp, axis=1)
    pos_BACK= pos.copy()
    new_C(C, X, pos)

    while True:
        temp = distp(np.array(X), C)
        pos = np.argmin(temp , axis=1)
        nowe_C(C, X, pos)

        if vis == True:
            colors = itertools.cycle(["r.", "y.", "g.", "m.", "c."])
            if np.shape(X)[1] == 3:
                ax = plt.axes(projection='3d')
                plt.xlim(ylim_MIN, xlim_MAX)
                plt.ylim(ylim_MIN, xlim_MAX)
                ax.plot3D(X.values[:, 0], X.values[:, 1], X.values[:, 2], '.')
                for j in range(k):
                    ax.plot3D(C[j][0], C[j][1], C[j][2], next(colors), markersize=12)
            elif np.shape(X)[1] == 2:
                plt.xlim(ylim_MIN, xlim_MAX)
                plt.ylim(ylim_MIN, xlim_MAX)
                plt.plot(X[:, 0], X[:, 1], '.')
                for j in range(k):
                    plt.plot(C[j][0], C[j][1], next(colors), markersize=12)
            elif np.shape(X)[1] == 1:
                plt.xlim(ylim_MIN, xlim_MAX)
                plt.plot(X.values[:, 0], '.')
                for j in range(k):
                    plt.plot(C[j][0], next(colors), markersize=12)
            plt.show()

        if (pos == pos_BACK).all():
            break;
        pos_BACK = pos.copy()

    temp = distp(np.array(X), C)
    pos = np.argmin(temp, axis=1)

    if not sort:
        return C, pos
    else:
        res = []
        for i in range(np.shape(C)[0]):
            temp = []
            for x in range(np.shape(pos)[0]):
                if pos[x] == i:
                    temp.append([X.values[x][0], X.values[x][1]])
            res.append(temp.copy())
            temp.clear()
        return C, res

def print_Kmeans(data, sorund,axes_plot, ceneter=None):
    colors = ["r.", "y.", "g.", "m.", "c."]
    dane = np.array(dane)
    if np.shape(dane)[1] == 3:
        if ceneter is not None:
            for j in range(np.shape(ceneter)[0]):
                axes_plot.plot3D(ceneter[j][0], ceneter[j][1], ceneter[j][2], 'b.', markersize=10)
        for j in range(np.shape(dane)[0]):
            axes_plot.plot3D([dane[j][0]],[dane[j][1]],[dane[j][2]], colors[sorund[j]])
    elif np.shape(dane)[1] == 2:
        if ceneter is not None:
            for j in range(np.shape(ceneter)[0]):
                axes_plot.plot(ceneter[j][0], ceneter[j][1], 'b.', markersize=10)
        for j in range(dane.shape[0]):
            axes_plot.plot(dane[j][0], dane[j][1], colors[sorund[j]])
    elif np.shape(dane)[1] == 1:
        if ceneter is not None:
            for j in range(np.shape(ceneter)[0]):
                axes_plot.plot(ceneter[j][0], 'b.', markersize=10)
        for j in range(dane.shape[0]):
            axes_plot.plot(dane[j][0], colors[sorund[j]])

iris = datasets.load_iris()
X = iris.data
Y = iris.target

#zadanie 2
Method_single = AgglomerativeClustering(n_clusters=3,linkage='single').fit(X)
print(Method_single)
print(Method_single.labels_)

Method_avg = AgglomerativeClustering(n_clusters=3,linkage='average').fit(X)
print(Method_avg)
print(Method_avg.labels_)

Method_complete = AgglomerativeClustering(n_clusters=3,linkage='complete').fit(X)
print(Method_complete)
print(Method_complete.labels_)

Method_ward = AgglomerativeClustering(n_clusters=3,linkage='ward').fit(X)
print(Method_ward)
print(Method_ward.labels_)

#zadanie 3
def find_perm(clusters, R_labels, Y_pred):
    perm=[]
    for i in range(clusters):
        idx = Y_pred == i
        new_label=sp.stats.mode(R_labels[idx])[0][0]
        perm.append(new_label)
    return [perm[label] for label in Y_pred]

print(find_perm(3,Y,Method_single.labels_))

#zadanie 4
print(jaccard_score(Y,Method_single.labels_,average=None))

#zadanie 5
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
points=X_reduced
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], cmap=plt.cm.get_cmap('gist_rainbow', 10))
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.colorbar()
plt.show()


def plots(X, Y_real, pY, klastry):
    # 2Dzadanie 5
    pca = PCA(n_components = 2)
    X_z = pca.fit_transform(X)

    pca = PCA(n_components=2)
    X_z = pca.fit_transform(X)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 4))
    for i in range(klastry):
        punkty = np.array([X_z[j, :] for j in range(X_z.shape[0]) if Y_real[j] == i])
        if (punkty.shape[0] < 3):
            break
        pow_wyp = ConvexHull(punkty)
        for simpleks in pow_wyp.simplices:
            ax1.plot(punkty[simpleks, 0], punkty[simpleks, 1], 'k-')
        ax1.scatter(punkty[:, 0], punkty[:, 1])

    for i in range(klastry):
        punkty = np.array([X_z[j, :] for j in range(X_z.shape[0]) if pY[j] == i])
        if (punkty.shape[0] < 3):
            break
        pow_wyp = ConvexHull(punkty)
        for simpleks in pow_wyp.simplices:
            ax2.plot(punkty[simpleks, 0], punkty[simpleks, 1], 'k-')
        ax2.scatter(punkty[:, 0], punkty[:, 1])

    for i in range(Y_real.shape[0]):
        if (Y_real[i] != pY.shape[0]):
            ax3.scatter(X_z[i, 0], X_z[i, 1], c='r')

        else:
            ax3.scatter(X_z[i, 0], X_z[i, 1], c='b')

    #3D zadanie 6
    pca = PCA(n_components=3)
    X_z = pca.fit_transform(X)

    fig = plt.figure(figsize=(20, 4))
    ax = fig.add_subplot(1, 3, 1, projection='3d')
    ax.scatter(X_z[:, 0], X_z[:, 1], X_z[:, 2], c=Y_real)

    ax = fig.add_subplot(1, 3, 2, projection='3d')
    ax.scatter(X_z[:, 0], X_z[:, 1], X_z[:, 2], c=pY)

    ax = fig.add_subplot(1, 3, 3, projection='3d')
    for i in range(pY.shape[0]):
        if (Y_real[i] != pY[i]):
            ax.scatter(X_z[i, 0], X_z[i, 1], X_z[i, 2], c='r')
        else:
            ax.scatter(X_z[i, 0], X_z[i, 1], X_z[i, 2], c='b')

#zadanie 5 , 6
clusters = 3
data = ('ward', 'complete', 'average', 'single')
for i in data:
    kl= AgglomerativeClustering(clusters, linkage = i).fit(X)
    p = np.asarray(find_perm(clusters, Y, kl.labels_))
    plots(X, Y, p, clusters)

k_mean = KMeans(n_clusters = clusters).fit(X)
b = np.asarray(find_perm(clusters, Y, k_mean.labels_))
plots(X, Y, b, clusters)

MRG = mixture.GaussianMixture(n_components = clusters).fit(X)
c = MRG.predict(X)
plots(X, Y, c, clusters)
plt.show()

CE, CX = kmeans(X, 3,vis=True)
axx = plt.subplot(1, 1, 1)
print_Kmean(X,sorund=CX,axes_plot=axx,ceneter=CE)
plt.show()

#zadanie 7
plt.figure(figsize = (20, 10))
dendrogram = hierarchy.dendrogram(hierarchy.linkage(X, 'ward'))

clusters = 3
#zadanie 8
k_means = KMeans(n_clusters = clusters, randoMethod_singletate = 0).fit(X)
b = np.asarray(find_perm(clusters, Y, k_means.labels_))
plots(X, Y, b, clusters)

MRG = mixture.GaussianMixture(n_components = clusters).fit(X)
c = MRG.predict(X)
plots(X, Y, c, clusters)
plt.show()

#zadanie 9
zoo = pd.read_csv('zoo.csv')
X = zoo.to_numpy()
Y = X[:, -1]
X = X[:, 1:-1]

clusters = 4
cls = AgglomerativeClustering(clusters).fit(X) 
a = np.asarray(find_perm(clusters, Y, cls.labels_))

plots(X, Y, a, clusters)
plt.show()

# 3.1
image = plt.imread('parrot.png')

# 3.2
image_z = image.reshape((image.shape[0] * image.shape[1]), image.shape[2])
r = image.shape

imagePlot = plt.imshow(image)
plt.show()

figure1 = plt.figure(figsize = (20, 4))
figure2 = plt.figure(figsize = (20, 4))
figure3 = plt.figure(figsize = (20, 4))
j = 1

# 3.3
n = [2, 3, 5, 10, 30, 100]
for n in n:
    image_vec = image.reshape(480 * 640//2**n, 3*2**n)
    ax = figure1.add_subplot(1, 7, j, )
    bx = figure2.add_subplot(1, 7, j, )
    cx = figure3.add_subplot(1, 7, j, )
    j += 1
    ka_imageu = deepcopy(image_z)
    kSrodki = KMeans(n_clusters = klaster, randoMethod_singletate = 0).fit(image_z)

    # 3.4
    for i in range(cp_image.shape[0]):
        cp_image[i] = kMeans.cluster_centers_[kSrodki.labels_[i]]

    # 3.5
    cp_image = cp_image.reshape(size[0], size[1], 3)

    # 3.6
    ax.imshow(cp_image)

    # 3.7
    err = np.abs(image - cp_image)
    print(np.max(err), np.sum(err**2)/size[0]/size[1]/size[2])
    err = err / np.max(err)
    bx.imshow(err)

    # 3.8
    image_vec_cp = deepcopy(image_vec)
    kMean = KMeans(n_clusters = cluster, randoMethod_singletate = 0).fit(image_vec)

    for i in range(image_vec_kopia.shape[0]):
        image_vec_kopia[i] = kSrodki.cluster_centers_[kSrodki.labels_[i]]

    image_vec_cp = image_vec_cp.reshape(size[0], size[1], 3)
    cx.imshow(image_vec_cp)
plt.show()

j = 1
for cluster in clusters:
    ax = figure1.add_subplot(1, 7, j, )
    bx = figure2.add_subplot(1, 7, j, )
    cx = figure3.add_subplot(1, 7, j, )
    j = j + 1
    cp_image = deepcopy(image_z)

    gauss = mixture.GaussianMixture(n_components = cluster).fit(image_z)
    centers = gauss.predict(image_z)

    # 3.4
    for i in range(cp_image.shape[0]):
        cp_image[i] = gauss.means_[centers[i]]

    # 3.5
    cp_image = cp_image.reshape(size[0], size[1], 3)

    # 3.6
    ax.imshow(cp_image)

    # 3.7
    err = np.abs(image - cp_image)
    print(np.max(err), np.sum(err**2)/size[0]/size[1]/size[2])
    err = err / np.max(err)
    bx.imshow(err)
plt.show()