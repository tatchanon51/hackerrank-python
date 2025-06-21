# Problem Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):                 #define function average
    dis_arr = list(set(array))      #use set to remove duplicated value
    n = len(dis_arr)                #find total number of distinct height
    sm = sum(dis_arr)               #calculate the sum value
    sm = round(sm,3)                #round result to 3 decimal places
    return(sm/n)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
