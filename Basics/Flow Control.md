# If 

``` python
age = 21
if age >= 18:
    print("You are old enough vote")
else:
    print("Please come back when you are old enough")
    
    
if age > 18 and age < 27:
    print("You are probably in the university")
    
if 18 < age < 27:
     print("You are probably in the university")
```

# ElIf

``` python
temp = int(input("Introduce temperature"))
if temp > 40:
    print("It is really hot")
elif temp > 18:
    print("It is rather warm")
else:
    print("It is cold")
```

# Not

``` python
txt = input("Introduce something")

if not txt:
    print("The user didn't introduce text")
else:
    print("The user introduced {}".format(txt))

```

# For loop

``` python
# The following will print from 1 to 9, 10 is not included
for i in range(1:10):
    print("idx: {}".format(i))
    
#Concatenating string into for loop
concat = ''
for i in range(1:10):
    concat += i
    
# for loop across a string

line = "here3there4aresome6number4and2letters"
cleanNumbers = ''
for char in line:
    if char in "0123456789":
        cleanNumbers += char

# The loop will iterate from 0 to 100 in steps of 5
for i in range (0. 100, 5)
    print("i is {}".format(i))
```

# Continue, Break, Else

```python
shoppingList = ['pasta', 'fruit', 'rice', 'spam', 'bread']

# Loop skipping the word spam from the list
for item in shoppingList:
    if item == spam:
        continue
    print("item: "+item)
    
# Stopping the loop when spam is reached
for item in shoppingList:
    if item == spam:
        break
    print("item: "+item)
    
meal = ['pasta', 'fruit', 'rice', 'spam', 'bread']
nasty_food = ''

# In the loop below the else is triggered in case there is no break
for item in meal:
    if item == 'spam':
        nasty_food = 'spam'
        break
else:
    print('I will order that food')
    
if nasty_food == 'spam':
    print('I want something without spam')
```

# While Loop

```python
i = 0
while i < 10:
    print("i is {}".format(i))
    i += 1
    
available_exits = ["east", "north east", "south"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("introduce exit: ")
    if chosen_exit == "quit":
        break
else: 
    print("You got out there")
```


