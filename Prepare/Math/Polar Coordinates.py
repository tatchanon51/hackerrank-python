#Problem Link: https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import phase

z = input()

if z.count('+') == 1:               #Check format of input x+yj, x-yj, -x-yj
    z = z.split('+')
    x = int(z[0])
    y = int(z[1][:len(z[1])-1])
if z.count('-') == 1:
    z = z.split('-')
    x = int(z[0])
    y = -int(z[1][:len(z[1])-1])
if z.count('-') == 2:
    z = z.split('-')
    x = -int(z[1])
    y = -int(z[2][:len(z[2])-1])

print(abs(complex(x,y)))
print(phase(complex(x,y)))