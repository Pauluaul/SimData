import numpy as np
import matplotlib.pyplot as plt
import tifffile as tif

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

for i in range(2 ** 7):
    x0, y0, z0 = 2 * np.random.rand(3) - 1
    K = ((X - x0) ** 2 + (Y - y0) ** 2 + (Z - z0) ** 2 < r ** 2)
    CheckOverlap = np.logical_and(K, V)
    if not CheckOverlap.any():
        V = np.logical_or(K, V)
    else:
        print("Overlap detected")

print("circles done")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z, x, y = V.nonzero()
ax.scatter(x, y, z, c=z+0.1*y+0.3*x, alpha=1, cmap='copper')
plt.show()

if generate_pic:
    a = V.astype('int8')
    tif.imsave('CircleAsTif.tif', a)
