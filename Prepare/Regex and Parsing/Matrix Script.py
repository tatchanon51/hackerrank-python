# Problem Link: https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

dec = []
#Transpose the matrix 
for M in range(m):
    for N in range(n):
        dec.append(matrix[N][M])

dec = ''.join(dec) #join to get one sentence

patt = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'  #Pattern to capture all symbol that in between of alphanumerics 
print(re.sub(patt,' ',dec))                             #Substitute the symbols with space and print