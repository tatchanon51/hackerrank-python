# Problem Link: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter

lis = []
for _ in range(int(input())):
    lis.append(input())

ct = Counter(lis)
print(len(ct))
print(*list(ct.values()))