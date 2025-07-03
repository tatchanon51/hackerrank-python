# Problem Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

n,m = list(map(int,input().split()))

#get A list
A = []                      
for _ in range(n):
    A.append(input())

#get B list
B = []
for _ in range(m):
    B.append(input())

#setup a dict to keep all indices of any letter in A
d = defaultdict(list)
for i in range(len(A)):
    d[A[i]].append(i+1)

#for all letter in B print all indices of the letter in A
for i in B:
    if i in d:
        print(*d[i])
    else:
        print(-1)