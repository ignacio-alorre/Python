import pandas as pd

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama', 'Pinon', 'Pinon'] ,
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador', 'Mastin', 'Mastin'] ,
    'color' : ["Grey", "Black", "Yellow", "Brown", "Grey", "Grey"],
    'weight' : [30, 16, 23, 23, 32, 28],
    'height' : [0.7, 0.35, 0.40, 0.32, 0.7, 0.7],
    'date_of_birth': ["05-02-1995", "02-05-2006", "07-07-2014", "15-08-2020", "05-02-1995", "05-02-1995"]
})

# 1- Dropping Duplicates
unique_dogs = dogs.drop_duplicates(subset=["name", "breed"])
print(unique_dogs)
'''
    name     breed   color  weight  height date_of_birth
0  Pinon    Mastin    Grey      30    0.70    05-02-1995
1  Trufa   Shepard   Black      16    0.35    02-05-2006
2   Scot  Labrador  Yellow      23    0.40    07-07-2014
3   Dama  Labrador   Brown      23    0.32    15-08-2020
'''

