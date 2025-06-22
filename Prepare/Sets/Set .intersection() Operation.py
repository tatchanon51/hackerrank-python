# Problem Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

n1 = input()                            #read input
ro1 = set(map(int,input().split()))     #read input
n2 = input()                            #read input
ro2 = set(map(int,input().split()))     #read input

ro = ro1.intersection(ro2)              #intersect to get roll numbers of student who subscript to both newspaper
print(len(ro))
