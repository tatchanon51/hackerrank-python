# Problem Link: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
from collections import namedtuple
N,stu = int(input()), namedtuple('Student',input().split())         #setup all field name
print(sum([int(stu(*input().split()).MARKS) for _ in range(N)])/N)                 #iterate thru all students and get MARK value
'''
from collections import namedtuple
N = int(input())
stu = namedtuple('Student',input().split())         #setup all field name
mark = []
for i in range(N):                                  #iterate thru all students and get MARK value
    mark.append(int(stu(*input().split()).MARKS))
print(sum(mark)/len(mark))'''