# Import pandas as pd
import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country": names, "drives_right": dr, "cars_per_cap": cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)

'''
# Original DataFrame:

         country  drives_right  cars_per_cap
0  United States          True           809
1      Australia         False           731
2          Japan         False           588
3          India         False            18
4         Russia          True           200
5        Morocco          True            70
6          Egypt          True            45
'''

# Extract drives_right column as Series: dr
dr = cars['drives_right']
# Use dr to subset cars: sel
sel = cars[dr == True]
# Print sel
print(sel)

'''
# drives_right countries:

         country  drives_right  cars_per_cap
0  United States          True           809
4         Russia          True           200
5        Morocco          True            70
6          Egypt          True            45
'''


# Convert code to a one-liner
sel = cars[cars['drives_right']]


# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars["cars_per_cap"] > 500]

# Print car_maniac
print(car_maniac)

'''
# Cars with cars_per_cap > 500

         country  drives_right  cars_per_cap
0  United States          True           809
1      Australia         False           731
2          Japan         False           588
'''

# For multiple filtering rules use numpy as well
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]

# Print medium
print(medium)

'''
  country  drives_right  cars_per_cap
4  Russia          True           200
'''