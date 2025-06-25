# Problem Link: https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import re
import itertools

#create pattern to capture set criteria as describe
patt = r"(?:.)#{1}([abcdefABCDEF0-9]{6}|[abcdefABCDEF0-9]{3})"

#Get all lines of input
inp = []
for _ in range(int(input())):
    inp.append(input())

#Keep all matched regex pattern in the 'final' list
final = []
for lin in inp:
    final.append(re.findall(patt,lin))
#Unnest the list
final = list(itertools.chain(*final))

for i in final:
    print('#'+str(i))
