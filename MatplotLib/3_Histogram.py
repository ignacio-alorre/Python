import matplotlib.pyplot as plt

# Player revenue
ply_rev = [10, 7, 25, 0, 30, 27, 32, 26, 55, 60, 31, 70, 100]

# Build histogram with 5 bins
plt.hist(ply_rev, 5)
plt.show()
plt.clf() # To clean up plot


# Build histogram with 10 bins
plt.hist(ply_rev, 10)
plt.show()
plt.clf()
