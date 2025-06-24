# Problem Link: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):    #define function
    l = len(string)                         #
    arr = []                                #Create arr to keep all possible string
    for i1 in range(l):                     #Iterate i1, i2 to generate all possible string
        for i2 in range(l-i1):
            arr.append(string[i2:l-i1])
    final = 0                               #Create final answer var
    for item in arr:                        #Iterate thru arr to check if the sub_string match with the element in the arr
        if item == sub_string:
            final+=1       
    return final

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
