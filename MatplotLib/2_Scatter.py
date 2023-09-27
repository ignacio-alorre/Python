import matplotlib.pyplot as plt

# Datasets to compare player level with revenue generated
ply_lvl = [20, 35, 22, 50, 57, 70]
ply_rev = [10, 25, 0, 30, 27, 55]

# Generate a scatter plot
plt.scatter(ply_lvl, ply_rev)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()