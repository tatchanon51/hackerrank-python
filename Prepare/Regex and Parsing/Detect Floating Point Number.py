# Problem Link: https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import re

patt = r"^([+-]?)([0-9])*\.[0-9]+$"
for _ in range(int(input())):
    print(bool(re.match(patt,input())))
