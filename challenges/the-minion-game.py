'''
Challenge: https://www.hackerrank.com/challenges/the-minion-game/problem

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''

def score(string, inVow):
    result = 0
    lInput = len(string)
    for i  in range(lInput):
        if (string[i] in ("A", "E", "I", "O", "U")) == inVow:
            result = result + (lInput - i)
    return result



def minion_game(string):
    kevin = score(string, True)
    stuart = score(string, False)
    if kevin == stuart:
        print("Draw")
    elif kevin < stuart:
        print("Stuart "+str(stuart))
    else:
        print("Kevin "+str(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)