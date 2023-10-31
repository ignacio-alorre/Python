import pandas as pd
import numpy as np

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama', 'Rubi'],
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador', 'Shepard'],
    'color' : ["Grey", "Black", "Yellow", "Brown", "Brown"],
    'weight' : [30, 16, 23, 23, 22],
    'height' : [0.7, 0.35, 0.40, 0.32, 0.4],
    'date_of_birth': ["05-02-1995", "02-05-2006", "07-07-2014", "15-08-2020", "15-08-1980"]
})
'''
Notes: 
Pivot tables are the standard way of aggregating data in spreadsheets.
In pandas, pivot tables are essentially another way of performing grouped calculations.
 That is, the .pivot_table() method is an alternative to .groupby().
'''

# 1- Group by Pivot Table

print(dogs.groupby("breed")["weight"].mean())
'''
breed
Labrador    23
Mastin      30
Shepard     19
Name: weight, dtype: int64
'''

print(dogs.pivot_table(values="weight", index="breed"))
'''
          weight
breed           
Labrador      23
Mastin        30
Shepard       19
'''

# 2- Multiple Statistics

print(dogs.pivot_table(values="weight", index="breed", aggfunc=[np.median, np.mean]))
'''
         median   mean
         weight weight
breed                 
Labrador     23     23
Mastin       30     30
Shepard      19     19
'''

# 3- Pivot on two variables

print(dogs.pivot_table(values="weight", index="color", columns="breed"))
'''
breed   Labrador  Mastin  Shepard
color                            
Black        NaN     NaN     16.0
Brown       23.0     NaN     22.0
Grey         NaN    30.0      NaN
Yellow      23.0     NaN      NaN
'''

# 4- Filling missing values in pivot tables
print(dogs.pivot_table(values="weight", index="color", columns="breed", fill_value=0))
'''
breed   Labrador  Mastin  Shepard
color                            
Black          0       0       16
Brown         23       0       22
Grey           0      30        0
Yellow        23       0        0
'''

# 5- Summing with pivot tables
print(dogs.pivot_table(values="weight", index="color", columns="breed", fill_value=0, margins=True))
'''
breed   Labrador  Mastin  Shepard   All
color                                  
Black          0       0       16  16.0
Brown         23       0       22  22.5
Grey           0      30        0  30.0
Yellow        23       0        0  23.0
All           23      30       19  22.0

# Note- At the all column/row we have the mean of each row/column
'''