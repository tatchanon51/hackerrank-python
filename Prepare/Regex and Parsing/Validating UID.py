# Problem Link: https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

for _ in range(int(input())):
    s = input()
    upp = 0
    digi = 0
    leng = 10
    if len(s) == len(set(s)):
        if len(s) == leng:
            if s.isalnum():
                for c in s:
                    if c.isupper():
                        upp += 1                #count uppercase
                    if c.isnumeric():
                        digi += 1               #count digit
                if upp >= 2 and digi >= 3:
                    print('Valid')
                else:
                    print('Invalid')
    else:
        print('Invalid')
    