# Problem Link: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())                            #read input
    final = 0                                   #set var final
    for x in range(n):                          #Iterate int < n
        x = x+1
        if 99 < x <= 150:                       #
            final = final * 100                 #For x from 100 to 150 since length of the number using 3 space it need to multiply 'final' by 100
            final = final + x*(10**(n-x))       #
        if 9 < x <= 99:                         #
            final = final * 10                  #For x from 10 to 99 since length of the number using 2 space it need to multiply 'final' by 10
            final = final + x*(10**(n-x))       #
        if x <= 9:                              #For x below 10 since length of numbers 1-9 using 1 space there is no need to multiply 'final'
            final = final + (x * (10**(n-x)))   #
print(final)
