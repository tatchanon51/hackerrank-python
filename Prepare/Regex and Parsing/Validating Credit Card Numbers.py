# Problem Link: https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true

import re

for _ in range(int(input())):
    s = input()
    patt = r'^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    patt2 = r'^[456][0-9]{15}$'
    if re.search(patt,s) or re.search(patt2,s):
        valido = True
        s = s.split('-')
        s = ''.join(s)
        for i in range(len(s)-3):
            if s[i]==s[i+1] and s[i+1]==s[i+2] and s[i+2]==s[i+3]:
                valido = False
    else:
        valido = False
                
    print('Valid' if valido else 'Invalid')
        