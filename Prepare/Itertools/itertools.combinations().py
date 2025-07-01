# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations
from itertools import chain

inp = ['HACK',3]
inp = list(input().split())
s = str(inp[0])
k = int(inp[1])

s = list(s)
s.sort()
a = []
for i in range(k):
    if i != 0 :
        a.append(list(combinations(s,i+1)))
a = list(chain(*a))
for n in range(len(a)):
    a[n] = ''.join(a[n])
s += a

for i in s:
    print(i)
