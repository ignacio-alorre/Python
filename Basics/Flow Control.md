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
```

