# Problem Link: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
import re

for _ in range(int(input())):       #iterate thru all lines
    lin = input()                   #get each line
    patt = r'(?<= )&{2}(?= )'       #pattern to capture '$$' with space on both ends
    mat = re.sub(patt,'and',lin)    #change && to and
    patt = r'(?<= )\|{2}(?= )'      #pattern to capture '||' with space on both ends
    mat = re.sub(patt,'or',mat)     #change || to or
    print(mat)
