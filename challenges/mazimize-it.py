# Challenge maximize-it
# https://www.hackerrank.com/challenges/maximize-it/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
meta = input().split()
size = int(meta[0])
mod = int(meta[1])
elements = []
for i in range(size):
    line = input()
    numList = line.split()
    del numList[0]
    numList = [int(i)*int(i) for i in numList]
    elements.append(numList) 


def maxModule(elements, mod, idx, acc):
    if idx == len(elements)-1:
        maxv = 0
        for n in elements[idx]:
            if (n+acc)%mod > maxv:
                maxv = (n+acc)%mod
        return maxv
    else:
        maxv = 0
        for n in elements[idx]:
            res = maxModule(elements, mod, idx+1, acc+n)
            if res > maxv:
                maxv = res
        return maxv

print(maxModule(elements, mod, 0, 0))