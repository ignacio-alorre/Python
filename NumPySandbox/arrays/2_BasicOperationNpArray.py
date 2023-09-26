# Import numpy
import numpy as np

# Create a numpy array from scores: np_scores
scores = [3, 6, 2, 7, 8, 12]
np_scores = np.array(scores)
print(np_scores)

# Multiply each score by the bonus
bonus = 5
np_bonus_score = np_scores * bonus
print(np_bonus_score)

# If we would have a different bonus for each level
np_bonu_level = np.array([2, 3, 5, 3, 5, 4])
print(np_bonu_level)

# Calculate final score per level
np_final_score = np_scores * np_bonu_level
print(np_final_score)

# Reverse np_final_score
np_final_score_rev = np_final_score[::-1]
print(np_final_score_rev)

# Find non-zero elements
np_with_zero_scores = np.array([1,2,0,0,4,0])
nz = np_with_zero_scores[np.nonzero(np_with_zero_scores)]
print(nz)

# Find the max and min of an array
s_max, s_min = np_scores.max(), np_scores.min()
print(s_max, s_min)

# Normalize a 5x5 random matrix
mtx_3 = np.random.random((3,3))
m_max, m_min = mtx_3.max(), mtx_3.min()
mtx_3norm = (mtx_3 - m_min) / (m_max - m_min)
print(mtx_3)
print(mtx_3norm)

# Negate all even number from an array
np_scores[np_scores % 2 == 0] *= -1
print(np_scores)

# Extract integer part of random array in different ways
rnd = np.random.uniform(0, 10, 10)
print(rnd)
print(rnd - rnd%1)
print(np.floor(rnd))
print(np.ceil(rnd) - 1)
print(rnd.astype(int))
print(np.trunc(rnd))

# Sorting a vector
rnd_8 = np.random.random(8)
print(rnd_8)
rnd_8.sort()
print(rnd_8)

# Summing elements of array
rnd_int = np.random.randint(1, 11, 5)
print(rnd_int)
rnd_int_sum = np.add.reduce(rnd_int)
print(rnd_int_sum)

# Comparing np arrays
a1 = np.random.randint(0, 2, 5)
a2 = np.random.randint(0, 2, 5)
equal = np.allclose(a1, a2)
print(a1)
print(a2)
print(equal)

# Find closest value to a given scalar
arr = np.arange(10)
v = np.random.uniform(0, 10)
index = (np.abs(arr-v)).argmin()
print(arr)
print(v)
print(arr[index])
