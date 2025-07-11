# Problem Link: https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

from collections import deque

for _ in range(int(input())):                   #loop thru test cases
    siz = int(input())    
    d = deque(list(map(int,input().split())))   #using deque because we need to operate on both size
    sr = list(d)                                #duplicate the list to sort
    sr.sort(reverse=False)
    valido = 'Yes'
    for i in range(len(sr)):                    #loop thru each operation
        x = sr.pop()
        if x == d[len(d)-1]:                    #check if the lowest value is on right side
            d.pop()
        elif x == d[0]:                         #check if the lowest value is on left side
            d.popleft()
        else:                                   #if no match then can't place on top
            valido = 'No'
            break
    print(valido)