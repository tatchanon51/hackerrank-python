# Problem Link: https://www.hackerrank.com/challenges/itertools-permutations

import itertools

inp = input().split()
a = list(inp[0])
b = int(inp[1])
per = list(itertools.permutations(a,b))     #Get all possible mix (no repeat- unlike product())
final = []
for i in per:
    final.append(''.join(i))                #Join the mix

final.sort()
for i in final:
    print(i)