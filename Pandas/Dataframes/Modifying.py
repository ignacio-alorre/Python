import pandas as pd

dogs = pd.DataFrame({
    'name' : ['Pinon', 'Trufa', 'Scot', 'Dama'] ,
    'breed' : ['Mastin', 'Shepard', 'Labrador', 'Labrador'] ,
    'color' : ["Grey", "Black", "Yellow", "Brown"],
    'weight' : ['30', '16', '23', '23'],
    'height' : [0.7, 0.35, 0.40, 0.32],
})

# 1- Adding a new column
dogs["height_cm"] = dogs["height"] * 100
print(dogs)

'''

'''