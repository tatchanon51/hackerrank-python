# Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
import sys

for n in sys.stdin:
    sp = n.find(' ')    #find space index
    N = int(n[:sp])     #slice to get N
    M = int(n[sp:])     #slice to get M

for l in range((N-1)//2):
    print('-'.ljust((M - ((l*2)+1)*3)//2,'-')+'.|.'*(1+(l*2))+'-'.rjust((M - ((l*2)+1)*3)//2,'-'))
    
print('-'.ljust((M-7)//2,'-')+'WELCOME'+'-'.rjust((M-7)//2,'-'))

for l in range((N-1)//2):
    print('-'.ljust((M - (((((N-1)//2)-l-1)*2)+1)*3)//2,'-')+'.|.'*(1+((((N-1)//2)-l-1)*2))+'-'.rjust((M - (((((N-1)//2)-l-1)*2)+1)*3)//2,'-'))
