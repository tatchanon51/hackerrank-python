# Problem Link: https://www.hackerrank.com/challenges/python-lists/problem
import sys

a = sys.stdin                       #Get all input
lis = []

for t in a:                         #Iterate thru a to separate them by line
    lis.append(t)

a = lis[0][:len(lis[0])-1]          #
b = lis[int(a)]
lis = [s[:len(s)-1] for s in lis]
lis[0] = a
lis[int(a)] = b
final = []
for com in lis:
    if 'insert' in com:
        com = com[7:]
        sp = com.find(' ')
        i = int(com[:sp])
        e = int(com[sp:])
        final.insert(i,e)
    if 'print' in com:
        print(final)
    if 'remove' in com:
        final.remove(int(com[7:]))
    if 'append' in com:
        final.append(int(com[7:]))
    if 'sort' in com:
        final.sort()
    if 'pop' in com:
        final.pop()
    if 'reverse' in com:
        final.reverse()
