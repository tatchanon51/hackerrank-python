# Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    k = int(k)
    string = str(string)
    n = len(string)
    lis = []
    line = n//k                         #Calculate line number
    for i in range(line):               #Iterate to create all separate lines
        lis.append(string[i*k:i*k+k])
    
    final = []
    for i in lis:                       #Iterate thru all line
        checker = []                    #Set a blank list as duplicate checker
        for c in i:                     #Iterate thru each line and keep characters that are not duplicate in the line
            if c not in checker:
                checker.append(c)
        final.append(''.join(checker))  #Keep all unique character in each line in the list
            
    for i in final:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
