'''
* Unordered collections
* Guarantee there are no duplicates in that collection
* Can take key-value pairs.
* Values are not accessed by an index, but by means of a key.
* Values can be of different types, but always immutable.

'''

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia': 'sydney' }

# Print out the keys in europe
print(europe.keys())
'''
dict_keys(['spain', 'france', 'germany', 'norway', 'australia'])
'''

# 1- Accessing the value. For example the value that belongs to key 'norway'
europe['norway']

# 2- Inserting a value. There is no method to append objects into a dictionary, you just add a new
# key and assign a new value
europe['italy'] = 'rome'

# 3- Checking if key is present in dictionary
print('italy' in europe)
'''
True
'''

# 4- Updating value of dictionary
# If you assign a value to an existing key, you replace the previous value rather than creating a new entry

europe["germany"] = "berlin city"

# 5- Removing a key-value pair from dictionary
europe.pop("australia")
del europe["norway"]

# 6- Deleting all entries from a dictionary
europe.clear()


# 7- Accessing missing keys in a dictionary
# 7.1- If you try to access a non-existing key, you will get a KeyError.
europe["japan"]   # KeyError

# 7.2- A safter way to get the value of a dictionary, passing a key is with the get method
europe.get("japan") # None


# Dictionary of dictionaries
europe = { "spain": { "capital":"madrid", "population":46.77 },
           "france": { "capital":"paris", "population":66.03 },
           "germany": { "capital":"berlin", "population":80.62 },
           "norway": { "capital":"oslo", "population":5.084 } }

# Print out the capital of France
print(europe["france"]["capital"])
'''
paris
'''

# Create sub-dictionary data
data = {"capital":"rome", "population":59.83}

# Dictionary country-capital
europe_cc = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe_cc.items():
    print("the capital of " + k + " is " + v)
'''
the capital of spain is madrid
the capital of france is paris
the capital of germany is berlin
the capital of norway is oslo
the capital of italy is rome
the capital of poland is warsaw
the capital of austria is vienna
'''
