# Generate a list
areas = [11.25, 18.0, 20.0, 10.75]

# Appending new item to the list
areas.append(15.37)

# Looping a list
for a in areas:
    print(a)

'''
11.25
18.0
20.0
10.75
15.37
'''

# Change for loop to use enumerate() and update print()
for i,v in enumerate(areas) :
    print("room "+str(i)+": "+str(v))

'''
room 0: 11.25
room 1: 18.0
room 2: 20.0
room 3: 10.75
room 4: 15.37
'''

# Concatenate two lists
areas_ground_floor = [6.55, 14.36, 17.12]
total_area = areas + areas_ground_floor
print(total_area)
'''
[11.25, 18.0, 20.0, 10.75, 15.37, 6.55, 14.36, 17.12]
'''

# sorting a list
print(sorted(areas))
print(sorted(areas, reverse=True))
'''
Note- These two will not mutate the list
[10.75, 11.25, 15.37, 18.0, 20.0]
[20.0, 18.0, 15.37, 11.25, 10.75]
'''

print(areas.sort())
'''
None -> This is because the function "sort()" will mutate the object numbers, but will not return anything
'''

print(areas)
'''
Note that in the previous stabe areas was mutated
[10.75, 11.25, 15.37, 18.0, 20.0]
'''

# Equality in lists takes into account the order of the elements
ordered = [1,2,3,4,5,6,7]
unordered = [1,3,5,7,2,4,6]

print(ordered == unordered)
'''
False
'''

# Creating an empty lists in two different ways
list_1 = []
list_2 = list()