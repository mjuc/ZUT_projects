import matplotlib.pyplot as mpl
import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris, load_digits
from sklearn.utils.extmath import svd_flip

np.random.seed(0)

def wiPCA(X, n):
    s = X.mean(axis = 0)
    x_Pca = X - s
    U, S, V = np.linalg.svd(x_Pca, full_matrices = False)
    U, V = svd_flip(U, V)
    w = (S ** 2) / (X.shape[0] - 1)
    k = V[: n, :]
    w2 = w[: n]
    compTrn = k.T
    X_reduced = np.dot(x_Pca, compTrn)
    return X_reduced, w2, k, s

def wiPCA_reverted(X_reduced, components, mn, n):
    return np.dot(X_reduced[:, : n], components[: , : n]) + mn

def euclid_dst(x1, x2):
    return math.sqrt(sum((x1 - x2) ** 2))

def cumulated_dst(x1, x2):
    dst = 0
    for p_1, p_2 in zip(x1, x2):
        dst += euclid_dst(p_1, p_2)
    return dst

def arrow(begin, end, ax = None):
    ax = ax or mpl.gca()
    s = dict(arrowstyle = '->', linewidth = 2, shrinkA = 0, shrinkB = 0)
    ax.annotate('', end, begin, arrowprops = s)

# Zadanie 1
#a)
x = np.random.randn(200)
#b)
y = 0.25 * x + np.random.randn(200) / 5
p = []
for p_x, p_y in zip(x, y):
    p.append([p_x, p_y])

p = np.array(p)

xMIN = p[:, 0].min()
xMAX = p[:, 0].max()
yMIN = p[:, 0].min()
yMAX = p[:, 0].max()

mpl.figure(figsize = (20, 10))
mpl.subplot(1, 2, 1)
#c)
pca = PCA(2)
p_reduced = pca.fit_transform(p)

pca1D = PCA(n_components = 1)
p_reduced_1D = pca1D.fit_transform(p)
p_reduced_WI1D = p_reduced_1D
p_reduced_1D = pca1D.inverse_transform(p_reduced_1D)

for length, vector in zip(pca.explained_variance_, pca.components_):
    w = vector * np.sqrt(length) * 2
    arrow(pca.mean_, pca.mean_ + w)

mpl.scatter(p[:, 0], p[:, 1])
mpl.scatter(p_reduced_1D[:, 0], p_reduced_1D[:, 1])
mpl.xlim(xMIN, xMAX)
mpl.ylim(yMIN + 0.2, yMAX + 0.2)
mpl.title('Default PCA')
mpl.subplot(1, 2, 2)

p_z_WI, w, k, s = wiPCA(p, 2)
p_z_WI1D, w1D, k1D, s1D = wiPCA(p, 1)
p_z_WI1D = wiPCA_reverted(p_z_WI1D, k1D, s1D, 2)

for length, vector in zip(w, k):
    w = vector * np.sqrt(length) * 2
    arrow(s, s + w)

mpl.scatter(p[:, 0], p[:, 1])
mpl.scatter(p_z_WI1D[:, 0], p_z_WI1D[:, 1])
mpl.xlim(xMIN, xMAX)
mpl.ylim(yMIN + 0.2, yMAX + 0.2)
mpl.title('PCA')
mpl.savefig('1.png')


# Zadanie 2
#a)
iris = load_iris()
X = iris.data
Y = iris.target
#b)
pca = PCA(4)
pca.fit(X)
X_reduced, w, k, s = wiPCA(X, 4)

mpl.figure(figsize = (20, 10))
mpl.title('Iris PCA')
mpl.scatter(X_reduced[:, 0], X_reduced[:, 1], c = Y)
mpl.xlabel('Component 1)')
mpl.ylabel('Component 2)')
mpl.savefig('2.png')

# Zadanie 3
#a)
zbior_digits = load_digits()
X = zbior_digits.data
Y = zbior_digits.target

#b)
pca = PCA(2)
pca.fit(X)
X_reduced2 = pca.transform(X)
X_reduced, w, k, s = wiPCA(X, 2)

mpl.figure(figsize = (15, 10))
mpl.title('Digit PCA')
mpl.scatter(X_reduced[:, 0], X_reduced[:, 1], c = Y, alpha = 0.6, cmap = mpl.cm.get_cmap('rainbow', 20))
mpl.xlabel('Component 1)')
mpl.ylabel('Component 2)')
mpl.colorbar()
mpl.tight_layout()
#c)
mpl.savefig('3c.png')

z_digits = load_digits()
X = z_digits.data
Y = z_digits.target

X_reduced, variance, components, mn = wiPCA(X, 64)
mpl.figure(figsize = (15, 10))
wsp_war = variance / variance.sum()
mpl.plot(np.cumsum(wsp_war))
mpl.xlim(0, 63)
mpl.ylim(0, 1.1)
mpl.grid()
mpl.xlabel('Liczba składników')
mpl.ylabel('Współczynnik wariancji')

#d)
mpl.savefig('Zadanie3d.png')

#e)
zbior_digits = load_digits()
X = zbior_digits.data
Y = zbior_digits.target
roznice = []
n = list(range(1, 64))

for i in n:
    X_reduced, w, k, s = wiPCA(X, i)
    X_reduced = wiPCA_reverted(X_reduced, k, s, 64)
    roznice.append(cumulated_dst(X, X_reduced) / len(Y))

mpl.figure(figsize = (15, 10))
wsp_war = variance / variance.sum()
mpl.plot(n, roznice)
mpl.xlim(0, 63)
mpl.grid()
mpl.xlabel('Liczba składników')
mpl.ylabel('Odległość')
mpl.savefig("Zadanie3e.png")
mpl.show()
