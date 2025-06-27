# Problem Link: https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

# Sample Input
main_string = input()           #main string
sub_string = input()            #sub_string to find

#using f' because there are a variable in the pattern and using lookahead to find the needed substring to capture nothing but index of the first match
mat = re.finditer(f'(?={sub_string})', main_string)
indices = []
for matc in mat:
    indices.append((matc.start(),matc.start()+len(sub_string)-1))    #print the indeies
if indices == []:   #check if it match or not
    print((-1,-1))
else:
    for i in indices:
        print(i)
