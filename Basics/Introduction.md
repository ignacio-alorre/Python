
# Variables

```python
# Valid variables
greeting = "Hello"
_name = "Scot"

# This will be a different variable
Greeting = "Hola" 

# Assigning to variables
a, b = 12, 13
```

# Print()

```python
# Printing Hello World!
name = World
print("Hello "+name+"!")

# String with multiples lines and without scape characters
stringWithNewLines = """This would be one line
and this would be the second line"""
print(stringWithNewLines)

# print() add a new line by default at the end of the printing action
# In case you want to avoid this or add a different termination to a printed line you can:
print("This is the sentence to print", end = "")
```

# Capturing input

```python
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
```

# Type conversion

```python
age = 54
sentence = "I am"
# The following will generate an error, sicne each variable has a different datatype
#print(sentence + age)

# Operations + Integers

```python
a = 12
b = 3
c = 2

print(a / b)  # 4.0
print(a // b) # 4
print(a % b)  # 0
print(b ** 2) # 9
```

# Operations + Strings

```python
str = "Labrador Retriever"
print(str[0])    #    L
print(str[-1])   #    r
print(str[0:4])  #    Labr
print(str[3:2])  #    ra
print(str[:6])   #    Labrad
print(str[9:])   #    Retriever
print(str[0:6:2])#    Lba   (From index 0 to index 6, no inclusive, print all characters skipping 1)

print("Hello" * 3) # Hello Hello Hello

print("day" in "Today") # True
```

# String Formatting

```python
age = 24
print("My age is "+ str(age) + " years")

# Replacement fields
print("My age is {0} years".format(age))
print("My age is {0} years. Tomorrow I become {1}".format(age, 25))
print("My age is %d years" % age)

# In the example below the 3 in %3d determines the number of characters allocated for that digit
# in this particular case, since 24 has just two digits, it will be converted into " 24"
print("My age is %3d years %s" % (age, "old"))

# Another option
print("My age is {0:3} years" % (age))  

# In case the parameters are in order you dont need to use the index
print("My age is {:3} years {}" % (age, "old"))
```

# Augmented Assigment

```python
x = 4
x += 6
print(x) # 10
x *= 3
print(x)  # 30
x /= 6
print(x)  # 5
x **= 2
print(x)  # 25
```
