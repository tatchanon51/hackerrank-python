# Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
import re

patt = r"([a-zA-Z0-9])"                 #pattern to check if it's alnumeric
m = str(input())                        #get input message

ans = []
for i in range(len(m)-1):               #iterate thru message by each character
    if m[i] == m[i+1]:                  #check if the two characters are the same
        if bool(re.match(patt,m[i])):   #check if the character is alphanumeric
            ans.append(m[i])            #keep it in 'ans' list
if ans != []:                           #print the first one if it was found
    print(ans[0])
else:                                   #print -1 if not
    print(-1)
