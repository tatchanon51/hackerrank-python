# Problem Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())                        #read 1st input
s = set(map(int, input().split()))      #read 2nd input - set
N = int(input())                        #read 3rd input - num command
com = []                                #setup a list to collect commands
for i in range(N):                      #Iterate to collect commands
    com.append(input())

for i in range(N):                      #Iterate to each command
    if com[i].split()[0] == 'pop':      #Check if it's 'pop'
        s.pop()
    if com[i].split()[0] == 'remove':   #Check if it's 'remove'
        s.remove(int(com[i].split()[1]))
    if com[i].split()[0] == 'discard':  #check if it's 'discard'
        s.discard(int(com[i].split()[1]))

print(sum(s))
