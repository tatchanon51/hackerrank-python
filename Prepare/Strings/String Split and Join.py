# Problem Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true

def split_and_join(line):           #define function
    line = line.split(' ')          #split string by ' ' result in a list of word
    line = '-'.join(line)           #join elements of the list and the delimiter is '-' 
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
