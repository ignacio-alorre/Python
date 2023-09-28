# Import numpy
import numpy as np

# Create baseball, a list of lists
ply_scores = [[8, 84],
            [10, 76],
            [12, 69],
            [17, 102]]

# Create a 2D numpy array from ply_scores: np_ply_scores
np_ply_scores = np.array(ply_scores)

# Scores
np_scores = np_ply_scores[:, 0]

# Print out the mean of np_scores
print("mean (avg) "+str(np.mean(np_scores)))
# Print out the median of np_scores
print("median "+str(np.median(np_scores)))
# Print out the standard deviation
print("Standard Deviation: " + str(np.std(np_scores)))
# Print out correlation between first and second column
print("Correlation: " + str(np.corrcoef(np_ply_scores[:,0], np_ply_scores[:,1])))
