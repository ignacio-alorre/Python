# Generate a list
areas = [11.25, 18.0, 20.0, 10.75]

# Looping a list
for a in areas:
    print(a)

'''
11.25
18.0
20.0
10.75
'''


# Change for loop to use enumerate() and update print()
for i,v in enumerate(areas) :
    print("room "+str(i)+": "+str(v))

'''
room 0: 11.25
room 1: 18.0
room 2: 20.0
room 3: 10.75
'''