# Problem Link: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

X = int(input())
shoe_stock = list(map(int,input().split()))
N = int(input())
rev = 0
for _ in range(N):
    siz, reve = list(map(int,input().split()))  #split between size and revenue of each customer
    if siz in shoe_stock:                       #check if the size available in stock
        shoe_stock.remove(siz)
        rev += reve
print(rev)