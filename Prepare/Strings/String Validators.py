# Problem Link: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()                             #Get input
    lis = list(s)                           #make it a list
    ans = [False,False,False,False,False]   #Set default answers to all False
    
    for t in lis:                           #Iterate to each input
        if t.isalnum():                     #Check if it's all numbers or alphabets
            ans[0] = True
        if t.isalpha():                     #Check if it's all alphabets
            ans[1] = True
        if t.isdigit():                     #Check if it's all digits
            ans[2] = True
        if t.islower():                     #Check if it's all lower
            ans[3] = True
        if t.isupper():                     #Check if it's all upper
            ans[4] = True
    for a in ans:
        print(a)
    
