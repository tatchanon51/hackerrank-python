# Problem Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

A = set(map(int,input().split()))                   #Get Set A

N = int(input())                                    #Get number of subsets

subset = []                                         #Create a list to keep all subsets
for i in range(N):                                  #Iterate to get all subsets from input
    subset.append(set(map(int,input().split())))

c = True                                            #Set default value of the answer to true
for s in subset:                                    #Iterate to subsets
    if (not (s <= A)) or len(s) == len(A):          #Check if each subset are subset to A and check if each subset are equal to A
        c = False                                   #Then change 'c' to False
print(c)
