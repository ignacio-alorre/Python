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

# Import the cars.csv data: cars
# cars = pd.read_csv("cars.csv")
# print(cars)

print("\nPrint out country column as Pandas Series:")
print(cars["country"])

print("\nPrint out country column as Pandas DataFrame:")
print(cars[["country"]])

print("\nPrint out DataFrame with country and drives_right columns:")
print(cars[["country", "drives_right"]])

print("\nPrint out first 3 observations:")
print(cars[0:3])

print("\nPrint out fourth, fifth and sixth observation:")
print(cars[3:6])

print("\nPrint out observation for Japan:")
print(cars.loc["JPN"])

print("\nPrint out observations for Australia and Egypt:")
print(cars.loc[["AUS", "EG"]])

print("\nPrint out a sub-DataFrame, containing the observations for Russia and Morocco "+
      "and the columns country and drives_right.")
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])

print("\nPrint out drives_right column as Series")
print(cars["drives_right"])

print("\nPrint out drives_right column as DataFrame")
print(cars.loc[:,["drives_right"]])

print("\nPrint out cars_per_cap and drives_right as DataFrame")
print(cars.loc[:,["cars_per_cap", "drives_right"]])
