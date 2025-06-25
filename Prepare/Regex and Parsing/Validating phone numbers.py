# Problem Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import re

patt = r"^[789]{1}(\d){9}$"         #set first digit only be 7-9 and the remaining 9 digits must be numbers only
for _ in range(int(input())):
    c = bool(re.match(patt, str(input())))
    if  c == True:
        print("YES")
    else:
        print("NO")
