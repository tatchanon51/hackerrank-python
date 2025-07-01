# Problem Link: https://www.hackerrank.com/challenges/itertools-product/

import itertools

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*list(itertools.product(a,b)))       #print the list by unnest 1 level
