# List

```python
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
