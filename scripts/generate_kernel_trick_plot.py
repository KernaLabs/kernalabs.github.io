import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random data in a circular distribution
np.random.seed(0)
theta = 2 * np.pi * np.random.rand(100)
r = 0.5 + np.random.rand(100) * 0.5

# Dataset 1: More compact and taller
data1 = np.c_[r * np.cos(theta) + 3, r * np.sin(theta) + 3, np.random.randn(100) * 0.5 + 3]

# Dataset 2: More diffuse and squat
r2 = 0.5 + np.random.rand(100) * 1.0  # Increased radius range for more diffusion
data2 = np.c_[r2 * np.cos(theta) - 3, r2 * np.sin(theta) - 3, np.random.randn(100) * 2 - 3]  # Increased Z variance and shifted down

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('white')  # Set background to white

# Plot the data with adjusted colors for better contrast
ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2],
           c='#efedf5', edgecolors='black', s=60, marker='o', label='Dataset 1')  # Darker color, white outline, larger size
ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2],
           c='#756bb1', edgecolors='black', s=60, marker='o', label='Dataset 2')  # Lighter color, black outline, smaller size

# Remove axes, grid, labels, and legend
ax.set_axis_off()

plt.show()

fig.savefig('kernel_trick_plot.eps', format='eps')
