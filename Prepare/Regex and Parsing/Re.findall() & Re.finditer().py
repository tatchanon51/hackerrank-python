#Problem Link: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

#Using positive lookahead and behide to detech all consonants and detech and capture all vowels in the middle
patt = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
m = input()
lst = re.findall(patt, m)

if lst == []:
    print(-1)
else:
    for i in lst:
        print(i)
