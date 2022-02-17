import numpy
import tifffile
from matplotlib import pyplot as plt

pic = tifffile.imread("trained_generators\CircleGen\CircleGen.tif")
pic = numpy.array(pic)

plot = pic.astype(bool)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

z, x, y = plot.nonzero()
ax.scatter(x, y, z, c=z, alpha=1, cmap='copper')
plt.show()
