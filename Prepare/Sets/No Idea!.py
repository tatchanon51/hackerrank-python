# Problem Link: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

inp = []                            #set up a list to get input
for i in range(4):                  #Iterate to 4 lines of input
    inp.append(input())

arr = list(map(int,inp[1].split())) #separate input to variable
A = set(map(int,inp[2].split()))
B = set(map(int,inp[3].split()))

happy = 0                           #set up happiness var
for i in arr:                       #Iterate to 'arr'
    if i in A:                      #Check if the element is in A
        happy += 1
    if i in B:                      #Check if the element is in B
        happy -= 1
print(happy)
