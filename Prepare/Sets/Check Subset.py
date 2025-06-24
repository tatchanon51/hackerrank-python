# Problem Link: https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

T = int(input())                                    #Get the number of test case
A = []                                              #Create a list to collect all set A
B = []                                              #Create a list to collect all set A
for i in range(T*2):                                #Iterate to get all sets from input
    _ = input()                                     #No need to get the number of elements
    if ((i+1) % 2) == 1:                            #Since input swap between set A and B if 'i' is indivisible by 2, it's A set 
        A.append(set(map(int,input().split())))
    if ((i+1) % 2) == 0:                            #If 'i' is divisible by 2, it's B set 
        B.append(set(map(int,input().split())))

for i in range(T):
    print(A[i] <= B[i])                             #Check if A is a subset of B
