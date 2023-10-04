# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia': 'sydney' }

# Print out the keys in europe
print(europe.keys())
'''
dict_keys(['spain', 'france', 'germany', 'norway', 'australia'])
'''

# Print out value that belongs to key 'norway'
europe['norway']

# Add key to dictionary
europe['italy'] = 'rome'

# Check if key in dictionary
print('italy' in europe)
'''
True
'''

# Update value of dictionary
europe["germany"] = "berlin city"

# Remove key from dictionary
europe.pop("australia")
del europe["norway"]

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
