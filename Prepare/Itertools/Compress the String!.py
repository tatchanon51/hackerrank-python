# Problem Link: https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby

s = input() 

g_data = groupby(s)
final = []
for key,group in g_data:
    final.append(tuple((len(list(group)),int(key))))
    
print(*final)
