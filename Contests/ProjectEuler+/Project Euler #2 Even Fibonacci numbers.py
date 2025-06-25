# Problem Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true
#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumevn = 0                          #sum even number of fibo
    fibo = [1,1]                        #Create fibo list
    lst = 0                             #setup last calculated fibo number
    i = 0                               #setup index of fibo list
    while lst <= n:                     #loop if last number less than or equal n
        lst = fibo[i]+fibo[i+1]         #calculate new fibo number
        fibo.append(lst)                #append to fibo list
        i += 1
        if lst % 2 == 0 and lst <= n:   #check if the number is an even number and still less than or equal n
            sumevn += lst
    print(sumevn)
