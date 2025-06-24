# Problem Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):                       #Define function
    final=[]                            #Create a list to keep all characters
    for c in s:                         #Iterate thru s string by each character
        if c.islower():                 #Check if the character is lower
            final.append(c.upper())
        elif c.isupper():               #Check if the character is capital
            final.append(c.lower())
        else:                           #For other character such as number, 
            final.append(c)
            
    return ''.join(final)               #Join all modified characters

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
