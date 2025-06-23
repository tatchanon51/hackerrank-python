# Problem Link: https://www.hackerrank.com/challenges/python-lists/problem

a = int(input())                        #Get the number of command
lis = []

for t in range(a):                      #Iterate get all commands
    lis.append(input())

final = []                              #Setup a list to apply command
for com in lis:                         #Iterate thru all commands
    if 'insert' in com:                 #Check if it's insert command or not
        com = com[7:]                   #reduce com var to only input of insert command
        sp = com.find(' ')              #find index of space
        i = int(com[:sp])               #setup index var
        e = int(com[sp:])               #setup the number to insert var
        final.insert(i,e)
    if 'print' in com:                  #Check if it's print command or not
        print(final)
    if 'remove' in com:                 #Check if it's remove command or not
        final.remove(int(com[7:]))
    if 'append' in com:                 #Check if it's append command or not
        final.append(int(com[7:]))
    if 'sort' in com:                   #Check if it's sort command or not
        final.sort()
    if 'pop' in com:                    #Check if it's pop command or not
        final.pop()
    if 'reverse' in com:                #Check if it's reverse command or not
        final.reverse()
