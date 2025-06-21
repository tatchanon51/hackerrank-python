# Problem Link: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

lis = []                            #Set up a blank list var
for i in range(4):                  #Iterate to get 4 lines of input
    lis.append(input())
M = set(map(int,lis[1].split()))    #Set up 1st set var
N = set(map(int,lis[3].split()))    #set up 2nd set var
final = M.difference(N)             #get difference value in M
final.update(N.difference(M))       #get difference value in N and update to 'final' set
final = list(final)                 #change final set to a list since set can't be sorted
final.sort()                        #sort the list
for i in range(len(final)):
    print(final[i])
