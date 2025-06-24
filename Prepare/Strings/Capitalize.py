## Problem Link: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def solve(s):
    lis = s.split(' ')                  #Make the name to list separate by space
    n = len(lis)
    for i in range(n):
        lis[i] = lis[i].capitalize()    #Make the first character of each element capital
    return(' '.join(lis))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
