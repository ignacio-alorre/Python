# Interview Question for Rakuten

# Given a string, return all possible permutations. For example:
# If input is abc:
# Output should be:
# abc
# acb
# bac
# bca
# cab
# cba

# This is a recursive solution with n!

import math

def getFactors(root,num):
    sol = []
    # return condition
    if len(num) == 1:
            return [root+num]
    # looping in next iteration
    for i in range(len(num)):  
        # Creating a substring with all remaining char but the taken in this iteration
        if i > 0:
            rem = num[:i]+num[i+1:]
        else:
            rem = num[i+1:]
        # Concatenating existing solutions with the solution of this iteration
        sol = sol + getFactors(root + num[i], rem)
    return sol

# I validated the solution taking into account two elements, the number of combinations is n! and the result can not contain duplicates. So:


inpt = "1234"
results = getFactors("",inpt)

if len(results) == math.factorial(len(inpt)) | len(results) != len(set(results)):
    print("Wrong approach")
else:
    print("Correct Approach")