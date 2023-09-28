# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia': 'sydney' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
europe['norway']

# Add key to dictionary
europe['italy'] = 'rome'

# Check if key in dictionary
print('italy' in europe)

# Update value of dictionary
europe["germany"] = "berlin city"

# Remove key from dictionary
europe.pop("australia")
del europe["norway"]

print(europe)

# Dictionary of dictionaries
europe = { "spain": { "capital":"madrid", "population":46.77 },
           "france": { "capital":"paris", "population":66.03 },
           "germany": { "capital":"berlin", "population":80.62 },
           "norway": { "capital":"oslo", "population":5.084 } }

# Print out the capital of France
print(europe["france"]["capital"])
# Create sub-dictionary data
data = {"capital":"rome", "population":59.83}
