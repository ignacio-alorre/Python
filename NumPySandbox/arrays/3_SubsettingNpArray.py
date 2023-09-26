# Import numpy
import numpy as np

# Create a numpy array from scores: np_scores
scores = [3, 16, 2, 17, 8, 12]
np_scores = np.array(scores)
print(np_scores)

# Create a np array with booleans for top scores
top_scores = np_scores > 10

# Print booleans for top scores
print(top_scores)

# Print scores above 10
print(np_scores[top_scores])

# Print out score at index 3
print(np_scores[3])

# Print out sub-array of np_scores index 2 to 4 including 4
print(np_scores[2:5])