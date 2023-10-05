# List

```python
# Mutable collection of objects. It is intented to have elements of the same type
# Counting number of occurrences of a symbol in a String

ipAddress = "192.168.0.1"
print("Number of dots is: "+ipAddress.count("."))

# Adding a new item to the list
parrotList = ['non pinin', 'no more', 'a stiff', "bereft of live"]
parrotList.append("flying")

for state in parrotList:
  print("The parrot is: "+state)
  
# Concatenating two lists
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
numbers.sort
print(numbers)  # 1 2 3 4 5 6 7 8 9

# Sorting in reverse order
numbers.sort(reverse=True) # 9 8 7 6 5 4 3 2 1
print(numbers)

# Another option:
numbers = even + odd
print(sorted(numbers))

# Attention: Following example will return None
# numbers = even + odd
# print(numbers.sort)
# The function sort will mutate the object numbers, but will not return anything

# Equality in lists takes into account the order of the elements

ordered = [1,2,3,4,5,6,7]
unordered = [1,3,5,7,2,4,6]

ordered == undordered # False

# Creating empty lists
list_1 = []
list_2 = list()


```

# Iterator

```python
str = "1234567890"

# Printing all digits in the string
for digit in iter(str):
  print(digit)
  
# Another approach would be
mIterator = iter(str)

for i in range(0, len(str)):
    print(next(mIterator))
```

# Range

```python
# Creating a range from 0 to 10 in steps of 2
even = list(range(0,10,2))

# Given an existing range, modifying the step value
myRange = range(0:10)
myNewRange = myRange[::2] # 0, 2, 4, 6, 8

# Retrieving the index of a given element in the list
index = myNewRange.index(4) # 2

# Ranges from max to min
myRange = range(0,11,-2) # 10 8 6 4 2 0

# The important thing in ranges is the value they return. So above ranges are the same
range(0, 100)[::-2] == range(99, 0, -2) # True

# Reversing an string, or range using this property
backStr = "ohcaN si eman yM"
print(backStr[::-1]) # My name is Nacho
```

# Tuples

```python
# Tuples are unmutable ordered set of data. Not always require to add the parentheses
tuple = "a", "b", "c"  # ("a", "b", "c")
print(("a", "b", "c")) # ("a", "b", "c") For example parentheses are required to pass the tuple to a function

# Tuples can combine different types of data
client = "Harrison G", 47, True

# Accessing elements of the tuple
print(combination[0]) # Harrison G

# It is not possible to modify a tuple (since they are unmutable)
client[1] = 50 # Will throw an error

# But this is approach is possible
client = client[0], 50, client[2]
print(client) # "Harrison G", 50, True

# Extracting elements of a tuple
name, age, married = client
print(name)    # Harrison G
print(age)     # 50
print(married) # True

# The use of tuples makes your code more robbust, since they are unmutable. Following action will be forbiden
client.append("Spain")

# A tuple can content other tuples 
client = "Harrison G", 47, True, (("Jon", 8), ("Beni", 12))
name, age, married, sons = client

# It would be possible to extract the individual tuples as well
name, age, married, son1, son2 = client

# In case we dont give enough variables, we will get an unpack error
name, age, married, son1 = client              # Will trigger: Not enough values to unpack
name, age, married, son1, son2, son3 = client  # Will trigger: Too many values to unpack

# In case the content of a tuple is a mutable object, for example a list, that mutable object can be modified
```
