# Problem Link: https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

n = int(input())                        
st_set = set(map(int,input().split()))                  #Get all number in starting set
com_num = int(input())                                  #Get the number of command

for i in range(com_num):                                #Iterate thru all commands
    com = input().split()                               #Get the element
    n = int(com[1])                                     #Get the number of operating set
    com = com[0]                                        #Get only str from the command
    op_set = set(map(int,input().split()))              #Get the operating set in each command
    if 'intersection_update' == com:                    #Check if the command is intersection_update
        st_set.intersection_update(op_set)              
    if 'update' == com:                                 #Check if the command is update
        st_set.update(op_set)
    if 'symmetric_difference_update' == com:            #Check if the command is symmetric_difference_update
        st_set.symmetric_difference_update(op_set)
    if 'difference_update' == com:                      #Check if the command is difference_update
        st_set.difference_update(op_set)
print(sum(st_set))                                      #Print sum of the mutated set