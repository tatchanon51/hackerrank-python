# Problem Link: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):                                #define function
    for n in range(len(string)):                            #Iterate thru string index
        if (n+1) % max_width == 0:                          #Check if the index+1 divisible by max_width
            print(string[(n+1-max_width):(n+1)])            #Print string that its length match with max_width
    return (string[(len(string)//max_width)*max_width:])    #Return the remain ones

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
