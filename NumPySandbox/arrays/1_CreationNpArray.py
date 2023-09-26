# Import the numpy package as np
import numpy as np

# Create list scores
scores = [3, 6, 2, 7, 8, 7, 9]

# Create a numpy array from scores: np_scores
np_scores = np.array(scores)
print(type(np_scores))
print(scores)

# Create null vector size 5
z = np.zeros(5)
print(z)

# Create np vector with values from 7 to 12
ar = np.arange(7, 13)
print(ar)

# Create a np matrix 3x3
mtx = np.arange(9).reshape(3,3)
print(mtx)

# Create a 3x3 array of random values
mtx_rnd = np.random.random((3,3))
print(mtx_rnd)

# Create an array from a generator function
def generate():
    for x in range(0, 10, 2):
        yield x
np_fromiter = np.fromiter(generate(), dtype=float, count=-1)
print(np_fromiter)

# Make an array immutable (read-only)
z_3 = np.zeros(3)
z_3.flags.writeable = False
#z_3[0] = 1 # Triggers "ValueError: assignment destination is read-only"

