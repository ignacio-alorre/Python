# Print()

```python
# Printing Hello World!
name = World
print("Hello "+name+"!")

# String with multiples lines and without scape characters
stringWithNewLines = """This would be one line
and this would be the second line"""
print(stringWithNewLines)
```

# Valid variables

```python
greeting = "Hello"
Greeting = "Hola" # This will be a different variable
_name = "Scot"
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

print(a / b) # 4.0
print(a // b) # 4
print(a % b) # 0
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



