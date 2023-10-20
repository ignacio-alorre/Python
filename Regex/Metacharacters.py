import re

txt = "The rain in Asturias... 4 or 5 days a week"

# '[]' - A set of characters: [a-m]
#        [0-3] is the same as [0123]
#        [^0-3] means any character except 0, 1, 2 or 3

print(re.findall("[a-m]", txt))
'''
['h', 'e', 'a', 'i', 'i', 'i', 'a', 'd', 'a', 'a', 'e', 'e', 'k']
'''
print(re.findall("[^a-m]", txt))
'''
['T', ' ', 'r', 'n', ' ', 'n', ' ', 'A', 's', 't', 'u', 'r', 's', '.', '.', '.', ' ', '4', ' ', 'o', 'r', ' ', '5', ' ', 'y', 's', ' ', ' ', 'w']
'''

# '\' - Makes sure the character is not treated in a special way: "\d"
# It is also used to escape the metacharacters

print(re.findall("\d", txt))
'''
['4', '5']
'''
print(re.findall("\.", txt))
'''
['.', '.', '.']
'''

# '.' - Represent any (can be one or many) character: "he..o", "h.o"

txt2 = "hello hiodo"
print(re.findall("h...o", txt2))
print(re.findall("h.o", txt2))
'''
['hello', 'hiodo']
['hio']
'''

# '^' - Allows you to match the beginning of the string

def string_starts_with_he(m_str):
    x = re.findall("^he", m_str)
    if x:
        print("String stars with 'he'")
    else:
        print("no match")

string_starts_with_he("hello world")
'''
String stars with 'he'
'''

string_starts_with_he("bye universe")
'''
no match
'''

# '$' - Allows you to match the end of the string. It checks whether the string ends
#       with the given character(s) or not.
def string_end_with_he(m_str):
    x = re.findall("rld$", m_str)
    if x:
        print("String ends with 'rld'")
    else:
        print("no match")

string_end_with_he("hello world")
'''
String ends with 'rld'
'''

string_end_with_he("bye universe")
'''
no match
'''

# '*' - Search for a sequence that starts with some character/s, followed by 0 or more (any)
#       characters, and another string/substring. for example: "he.*o" will match helo, hello, helllo...

print(re.findall("w.*k", "wik and"))
print(re.findall("w.*k", "weak and"))
print(re.findall("w.*k", "wooook and"))
'''
['wik']
['weak']
['wooook']
'''

# '+' - Will match one or more occurrences of the regular expression preceding the + symbol
