#Problem Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

def print_rangoli(size):
    # your code goes here                
    al = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'      
    al = al.split(' ')                                          #Create a list of alphabet
    
    N = size

    #Generate middle line
    mid = ''
    mid += al[N-1]                                              
    for i in range(N-1):
        mid += '-'+al[N-2-i]
    for i in range(N-1):
        mid += '-'+al[i+1]

    #Generate side lines
    lin = []
    l = len(mid)
    x = mid
    n = 0 
    while n < (N-1):
        l = len(x)
        lin.append(x[:((l-1)//2)-1]+x[((l-1)//2)+3:])
        x = lin[n]
        n+=1
    ##Adding '--' the both side
    n = len(lin)
    for i in range(n):
        lin[i] = '--'*(i+1)+lin[i]+'--'*(i+1)

    #Print out all lines
    for i in range(len(lin)):
        print(lin[len(lin)-i-1])
    print(mid)
    
    for i in range(len(lin)):
        print(lin[i])
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
