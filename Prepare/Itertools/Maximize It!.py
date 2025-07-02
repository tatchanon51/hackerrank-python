# Problem Link: https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

import itertools

def square(x):
    return pow(x,2)
def modu(x,y):
    return x % y

lin, divi = map(int,input().split())

mast_lis = []
for i in range(lin):
    lis = input().split()
    lis = lis[1:]                   #remove the first element that is length of each list
    lis = list(map(int,lis))        #change all elements to int type 
    lis = list(map(square,lis))     #square all elements
    mast_lis.append(lis)            #append the list to master list

prod_mast = list(itertools.product(*mast_lis)) #Product all list and get all possible mix
sum_prod_mast = list(map(sum,prod_mast))       #Sum all elements in each list to get a single value
modval = list(map(modu,sum_prod_mast,itertools.repeat(divi,len(sum_prod_mast))))                            #Calculate modulo of all possibility
modval.sort()                                   
print(modval[len(modval)-1])                  #Print the largest value