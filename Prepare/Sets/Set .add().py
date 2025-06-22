# Problem Link: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())            #Read amount of stamps from 1st input

stp = []                    #setup a list to collect all country names
for i in range(n):          #Iterate to get all names
    stp.append(input())     #keep them in the list
stp = set(stp)              #remove all duplicate values
print(len(stp))
