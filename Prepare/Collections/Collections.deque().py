# Problem Link: https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

from collections import deque

d = deque()
for _ in range(int(input())):
    lis = list(input().split())
    if len(lis) == 2:
        com,n = lis
        if com == 'append':
            d.append(n)
        elif com == 'appendleft':
            d.appendleft(n)
    else:
        com = lis[0]
        if com == 'pop':
            d.pop()
        elif com == 'popleft':
            d.popleft()
            
print(*d)