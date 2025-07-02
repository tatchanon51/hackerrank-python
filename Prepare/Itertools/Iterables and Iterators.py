# Problem Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

import itertools

N = int(input())
lis = input().split()
K = int(input())

tot = 0                                 #total cases
wan = 0                                 #wanted cases
for i in itertools.combinations(lis,K):
    if 'a' in i:
        wan +=1
        tot +=1
    else:
        tot +=1
print(round(wan/tot,3))