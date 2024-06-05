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
r2 = 0.5 + np.random.rand(100) * 1.0
data2 = np.c_[r2 * np.cos(theta) - 3, r2 * np.sin(theta) - 3, np.random.randn(100) * 2 - 3]

# Create a large figure to hold all subplots
fig = plt.figure(figsize=(45, 45))  # Adjust the size as needed

# Number of subplots
n_plots = 50
n_rows = n_plots // 7 + (n_plots % 7 > 0)  # Calculate rows needed
n_cols = 7  # Set columns

for i in range(n_plots):
    ax = fig.add_subplot(n_rows, n_cols, i + 1, projection='3d')
    ax.set_facecolor('white')

    # Plot the data with adjusted colors for better contrast
    ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2],
               c='#efedf5', edgecolors='black', s=30, marker='o', label='Dataset 1')
    ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2],
               c='#756bb1', edgecolors='black', s=30, marker='o', label='Dataset 2')

    # Remove axes, grid, labels, and legend
    ax.set_axis_off()

    # Set the view angle
    ax.view_init(azim=i * 1, roll=i * 10, elev=i * 15)

    # Save each subplot individually
    individual_fig = plt.figure()
    individual_ax = individual_fig.add_subplot(111, projection='3d')
    individual_ax.set_facecolor('white')
    individual_ax.scatter(data1[:, 0], data1[:, 1], data1[:, 2], c='#efedf5', edgecolors='black', s=30, marker='o')
    individual_ax.scatter(data2[:, 0], data2[:, 1], data2[:, 2], c='#756bb1', edgecolors='black', s=30, marker='o')
    individual_ax.set_axis_off()
    individual_ax.view_init(azim=i * 1, roll=i * 10, elev=i * 15)
    individual_fig.savefig(f'../images/kernel_trick_plot_individual_{i}.png', format='png', transparent=True)
    plt.close(individual_fig)  # Close the individual figure to free up memory

# Save the large figure containing all subplots
fig.savefig('../images/kernel_trick_plot_all_subplots.png', format='png', transparent=True)
plt.close(fig)  # Close the figure to free up memory