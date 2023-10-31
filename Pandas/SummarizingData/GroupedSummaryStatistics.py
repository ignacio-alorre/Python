import pandas as pd

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama'],
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador'],
    'color' : ["Grey", "Black", "Yellow", "Brown"],
    'weight' : [30, 16, 23, 23],
    'height' : [0.7, 0.35, 0.40, 0.32],
    'date_of_birth': ["05-02-1995", "02-05-2006", "07-07-2014", "15-08-2020"]
})

# 1- Grouped Summaries

print(dogs.groupby("breed")["weight"].mean())
'''
breed
Labrador    23
Mastin      30
Shepard     16
Name: weight, dtype: int64
'''

# 2- Multiple Grouped Summary

print(dogs.groupby("breed")["weight"].agg([min, max, sum]))
'''
          min  max  sum
breed                  
Labrador   23   23   46
Mastin     30   30   30
Shepard    16   16   16
'''

# 3- Grouping by multiple variables

print(dogs.groupby(["color", "breed"])["weight"].mean())
'''
color   breed   
Black   Shepard     16
Brown   Labrador    23
Grey    Mastin      30
Yellow  Labrador    23
Name: weight, dtype: int64
'''

# 4- Many Groups, Many summaries

print(dogs.groupby(["color", "breed"])[["weight", "height"]].mean())
'''
                 weight  height
color  breed                   
Black  Shepard       16    0.35
Brown  Labrador      23    0.32
Grey   Mastin        30    0.70
Yellow Labrador      23    0.40
'''

