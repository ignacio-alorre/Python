
# Dictionary

```python
# Unordered collections, garantee there are no duplicates in that collection, can take key value pairs. 
# Values are not accessed by an index, but by means of a key. Values can be of different types, but always unmutable.

fruit = {"orange": "a sweet citrus",
         "apple": "good for making cider",
         "lemon": "an acid citrus",
         "grape": "a small sweet fruit"}
         
print(fruit['orange'])  # "a sweet citrus"

# There is no method to append objects into a dictionary, you just add a new key and assign a new value
fruit["cherry"] = "red round berry"

# If you assign a value to an existing key, you replace the previous value rather than creating a new entry

# Deleting entries from a dictionary passing the key to delete
del fruit['apple']

# Deleting all entries from a dictionary
fruit.clear()

# If you try to access a non-existing key, you will get a KeyError.
fruit["onion"]   # KeyError

# One way to avoid this would be
if key in fruit:
         fruit[key]
         
# A safter way to get the value of a dictionary, passing a key is with the get method
fruit.get("onion") # None


```

# Set

```python
# Unordered collections, garantee there are no duplicates in that collection, intended to store similar items 
# but you can't acctually access individual items using an index (since sets are unordered index is meaningless in this context)
```



