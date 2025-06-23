# Problem Link: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(raw_input())                            #Get input
    integer_list = map(int, raw_input().split())    #Map all input to int function
    t = tuple(integer_list)                         #make the list to tuple
    print(hash(t))                                  
#This problem have to use Python2 to pass. IMO: Python2/3 hash function doesn't use the same mechanic.