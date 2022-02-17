import numpy as np
import matplotlib.pyplot as plt
import tifffile as tif
import helper
from scipy.spatial.transform import Rotation as R

generate_pic = False
N = 2 ** 8
X = np.linspace(-1, 1, N)
Y = np.linspace(-1, 1, N)
Z = np.linspace(-1, 1, N)
r = 2 ** -4

print("prep done")

X, Y, Z = np.meshgrid(X, Y, Z)

print("meshgrid done")

V = np.zeros((N, N, N), dtype=bool)

for i in range(2**7):
    x0, y0, z0 = 2 * np.random.rand(3) - 1
    alpha, beta, gamma = R.random().as_euler('xyz', degrees=True)
    X_, Y_, Z_ = helper.rotate(X, Y, Z, alpha, beta, gamma)
    K = (0.25*(X_ - x0) ** 2 + (Y_ - y0) ** 2 + (Z_ - z0) ** 2 < r ** 2)
    CheckOverlap = np.logical_and(K, V)
    if not CheckOverlap.any():
        V = np.logical_or(K, V)
    else:
        print("Overlap detected")

print("cubes done")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z, x, y = V.nonzero()
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()

if generate_pic:
    a = V.astype('int8')
    tif.imsave('EllipsoidAsTif.tif', a)
