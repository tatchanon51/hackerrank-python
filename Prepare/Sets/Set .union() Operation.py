# Problem Link: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

n1 = input()                            #read input number of english subscription
ro1 = set(map(int,input().split()))     #read roll number of english subscription
n2 = input()                            #read input number of french subscription
ro2 = set(map(int,input().split()))     #read roll number of french subscription

ro = ro1.union(ro2)                     #union both roll number to get student roll numbers that subscript at least one
print(len(ro))