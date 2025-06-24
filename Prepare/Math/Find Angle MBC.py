# Problem Link: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

AB = int(input())
BC = int(input())
AC = ((AB ** 2) + (BC ** 2)) ** 0.5                                 #find AC
CM = AC/2

C_deg = math.asin(AB/AC)                                            #find angle C
BM = ((BC ** 2) + (CM ** 2) - (math.cos(C_deg) * 2 * BC * CM))**0.5 #Using Cosin law to get BM

x = math.asin((math.sin(C_deg) / BM) * CM)                          #Using Sin law to get the angle

print(str(round(math.degrees(x)))+chr(176))                         #Change the angle to degree and merge with the degree symbol