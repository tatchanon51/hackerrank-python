# Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())    # read input
    if n % 2 == 1:              # check if odd
        print("Weird")          # print
    elif 2<=n<=5:               # check if value between 2-5
        print("Not Weird")      # print
    elif 6<=n<=20:              # check if value between 6-20
        print("Weird")          # print
    elif n>20:                  # check if value greater than 20
        print("Not Weird")      # print
