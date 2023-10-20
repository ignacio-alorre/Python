import pandas as pd

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama'] ,
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador'] ,
    'color' : ["Grey", "Black", "Yellow", "Brown"],
    'weight' : ['30', '16', '23', '23'],
    'height' : ['0.7', '0.35', '0.40', '0.32'],
})

print(dogs)
'''
    name     breed   color weight height
0  Pinon    Mastin    Grey     30    0.7
1  Trufa   Shepard   Black     16   0.35
2   Scot  Labrador  Yellow     23   0.40
3   Dama  Labrador   Brown     23   0.32
'''

# 1- Sorting by multiple variables
dogs.sort_values(["weight", "height"], ascending=[True, False])
print(dogs)
'''
    name     breed   color weight height
0  Pinon    Mastin    Grey     30    0.7
1  Trufa   Shepard   Black     16   0.35
2   Scot  Labrador  Yellow     23   0.40
3   Dama  Labrador   Brown     23   0.32
'''

# 2- Subsetting based on multiple conditions
brown_labrador = dogs[(dogs["breed"] == "Labrador") & (dogs["color"] == "Brown")]
print(brown_labrador)

'''
   name     breed  color weight height
3  Dama  Labrador  Brown     23   0.32
'''

# 3- Subsetting using .isin()
black_or_brown = dogs[dogs["color"].isin(["Brown", "Black"])]
print(black_or_brown)

'''
    name     breed  color weight height
1  Trufa   Shepard  Black     16   0.35
3   Dama  Labrador  Brown     23   0.32
'''

# 4- Subsetting columns of dataframe
name_and_breed = dogs[["name", "breed"]]
print(name_and_breed)

'''
    name     breed
0  Pinon    Mastin
1  Trufa   Shepard
2   Scot  Labrador
3   Dama  Labrador
'''