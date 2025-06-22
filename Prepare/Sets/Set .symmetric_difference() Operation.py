# Problem Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true

n1 = input()                            #read input number of english subscription
ro1 = set(map(int,input().split()))     #read roll number of english subscription
n2 = input()                            #read input number of french subscription
ro2 = set(map(int,input().split()))     #read roll number of french subscription

ro = ro1.symmetric_difference(ro2)      #geting symmetic difference
print(len(ro))