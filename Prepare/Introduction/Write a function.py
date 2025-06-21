# Problem Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):              #Define function is_leap
    leap = False                #Set leap var to false mean the year is not a leap year
    if year % 4 == 0:           #Set all year that divisible by 4 are leap years
        leap = True
    if year % 100 == 0:         #Detect all year that divisible by 100 are not leap years
        leap = False
    if year % 400 == 0:         #After that detect all year that divisible by 400 are leap years
        leap = True
    return leap

year = int(input())
print(is_leap(year))
