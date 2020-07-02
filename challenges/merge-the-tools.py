'''
Challenge: https://www.hackerrank.com/challenges/merge-the-tools/problem

Consider the following:

A string, s, of length n.
An integer, k , where k is a factor of n.
We can split s into n/k subsegments where each subsegment, t, consists of a contiguous block of k characters in s. Then, use each t to create string u such that:

* The characters in u are a subsequence of the characters in t.
* Any repeat occurrence of a character is removed from the string such that each character in u occurs exactly once. 
'''

def merge_the_tools(string, k):
    grps = int(len(string)/k)
    for i in range(grps):
        t = string[i*k:i*k+k]
        acc = t[0]
        for j in range(1,len(t)):
            if t[j] not in acc:
                acc = acc + t[j]
        print(acc)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)