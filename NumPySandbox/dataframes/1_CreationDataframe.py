# Import pandas as pd
import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country": names, "drives_right":dr, "cars_per_cap": cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels

print(cars)
'''
# Original Dataframe:

           country  drives_right  cars_per_cap
US   United States          True           809
AUS      Australia         False           731
JPN          Japan         False           588
IN           India         False            18
RU          Russia          True           200
MOR        Morocco          True            70
EG           Egypt          True            45
'''

# Import the cars.csv data: cars
# cars = pd.read_csv("cars.csv")
# print(cars)


print(cars["country"])
'''
# Print out country column as Pandas Series:

US     United States
AUS        Australia
JPN            Japan
IN             India
RU            Russia
MOR          Morocco
EG             Egypt
Name: country, dtype: object
'''


print(cars[["country"]])
'''
# Print out country column as Pandas DataFrame:

           country
US   United States
AUS      Australia
JPN          Japan
IN           India
RU          Russia
MOR        Morocco
EG           Egypt
'''


print(cars[["country", "drives_right"]])
'''
# Print out DataFrame with country and drives_right columns:

           country  drives_right
US   United States          True
AUS      Australia         False
JPN          Japan         False
IN           India         False
RU          Russia          True
MOR        Morocco          True
EG           Egypt          True
'''

print(cars[0:3])
'''
Print out first 3 observations:

           country  drives_right  cars_per_cap
US   United States          True           809
AUS      Australia         False           731
JPN          Japan         False           588
'''

print(cars[3:6])
'''
Print out fourth, fifth and sixth observation:

     country  drives_right  cars_per_cap
IN     India         False            18
RU    Russia          True           200
MOR  Morocco          True            70
'''

print(cars.loc["JPN"])
'''
Print out observation for Japan:

country         Japan
drives_right    False
cars_per_cap      588
Name: JPN, dtype: object
'''

print(cars.loc[["AUS", "EG"]])
'''
Print out observations for Australia and Egypt:
       country  drives_right  cars_per_cap
AUS  Australia         False           731
EG       Egypt          True            45
'''

print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])
'''
Print out a sub-DataFrame, containing the observations for Russia and Morocco and the columns country and drives_right.
     country  drives_right
RU    Russia          True
MOR  Morocco          True
'''

print(cars["drives_right"])
'''
Print out drives_right column as Series
US      True
AUS    False
JPN    False
IN     False
RU      True
MOR     True
EG      True
Name: drives_right, dtype: bool
'''

print(cars.loc[:,["drives_right"]])
'''
Print out drives_right column as DataFrame
     drives_right
US           True
AUS         False
JPN         False
IN          False
RU           True
MOR          True
EG           True
'''

print(cars.loc[:,["cars_per_cap", "drives_right"]])
'''
Print out cars_per_cap and drives_right as DataFrame
     cars_per_cap  drives_right
US            809          True
AUS           731         False
JPN           588         False
IN             18         False
RU            200          True
MOR            70          True
EG             45          True
'''