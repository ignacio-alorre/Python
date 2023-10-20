import pandas as pd

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama'] ,
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador'] ,
    'color' : ["Grey", "Black", "Yellow", "Brown"],
    'weight' : [30, 16, 23, 23],
    'height' : [0.7, 0.35, 0.40, 0.32],
    'date_of_birth': ["05-02-1995", "02-05-2006", "07-07-2014", "15-08-2020"]
})

# 1- Standard summarizing methods
print(dogs["weight"].mean())
print(dogs["weight"].median())
print(dogs["weight"].mode())
print(dogs["weight"].min())
print(dogs["weight"].max())
print(dogs["weight"].var())
print(dogs["weight"].std())
print(dogs["weight"].sum())
print(dogs["weight"].quantile())

'''
23.0
23.0
0    23
dtype: int64
16
30
32.666666666666664
5.715476066494082
92
23.0
'''

# 2- Summarizing dates
print(dogs["date_of_birth"].min())
print(dogs["date_of_birth"].max())
'''
02-05-2006
15-08-2020
'''

# 3- The .agg() method
def pct30(column):
    return column.quantile(0.3)

print(dogs["weight"].agg(pct30))
'''
22.3
'''

print(dogs[["weight", "height"]].agg(pct30))
'''
weight    22.300
height     0.347
dtype: float64
'''

# 4- Multiple summaries
def pct40(column):
    return column.quantile(0.4)

print(dogs["weight"].agg([pct30, pct40]))
'''
pct30    22.3
pct40    23.0
Name: weight, dtype: float64
'''

# 5- Cumulative statistics (.cumsum(), .cummax(), .cummin(), .cumprod())
dogs_weight_sorted = dogs.sort_values("weight")[["name","weight"]]

dogs_weight_sorted["cumsum"] = dogs_weight_sorted["weight"].cumsum()
print(dogs_weight_sorted[["name", "cumsum"]])
'''
    name  cumsum
1  Trufa      16
2   Scot      39
3   Dama      62
0  Pinon      92
'''

dogs_weight_sorted["cummax"] = dogs_weight_sorted["weight"].cummax()
print(dogs_weight_sorted[["name", "cummax"]])
'''
    name  cummax
1  Trufa      16
2   Scot      23
3   Dama      23
0  Pinon      30
'''

dogs_weight_sorted["cummin"] = dogs_weight_sorted["weight"].cummin()
print(dogs_weight_sorted[["name", "cummin"]])
'''
    name  cummin
1  Trufa      16
2   Scot      16
3   Dama      16
0  Pinon      16
'''

dogs_weight_sorted["cumprod"] = dogs_weight_sorted["weight"].cumprod()
print(dogs_weight_sorted[["name", "cumprod"]])
'''
    name  cumprod
1  Trufa       16
2   Scot      368
3   Dama     8464
0  Pinon   253920
'''

# 6- Values counts and values counts sorted
print(dogs["breed"].value_counts())
'''
Labrador    2
Mastin      1
Shepard     1
'''

print(dogs["breed"].value_counts(sort=True))
'''
Labrador    2
Mastin      1
Shepard     1
'''

# 7- Proportions
print(dogs["breed"].value_counts(normalize=True))
'''
Labrador    0.50
Mastin      0.25
Shepard     0.25
'''
