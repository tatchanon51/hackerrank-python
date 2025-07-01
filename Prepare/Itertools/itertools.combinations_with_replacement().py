# Problem Link: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement

inp = input().split()
s = str(inp[0])
k = int(inp[1])
s = list(s) 
s.sort() 

final = list(combinations_with_replacement(s,k))
for i in range(len(final)):
    final[i] = ''.join(final[i])
for i in final:
    print(i)
