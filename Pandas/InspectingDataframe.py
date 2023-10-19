import pandas as pd


dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama'] ,
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador'] ,
    'weight' : ['30', '16', '23', '20']
})

print(dogs)
'''
    name     breed weight
0  Pinon    Mastin     30
1  Trufa   Shepard     16
2   Scot  Labrador     23
3   Dama  Labrador     20
'''

print(dogs.head())
'''
    name     breed weight
0  Pinon    Mastin     30
1  Trufa   Shepard     16
2   Scot  Labrador     23
3   Dama  Labrador     20
'''

print(dogs.info())
'''
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object
 1   breed   4 non-null      object
 2   weight  4 non-null      object
dtypes: object(3)
memory usage: 224.0+ bytes
None
'''

print(dogs.shape)
'''
(4, 3)
'''

print(dogs.describe())
'''
         name     breed weight
count       4         4      4
unique      4         3      4
top     Trufa  Labrador     20
freq        1         2      1
'''
