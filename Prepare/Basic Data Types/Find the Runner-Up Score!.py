# Problem Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())                        #Get number of attendees
    arr = map(int, input().split())         #Get all score and map into integer array
    
    uniq = list(set(arr))                   #Using set function to remove duplicate score and change set to list
    uniq.sort()                             #Sort the list by value
    n = len(uniq)                           #find the length of the unique score. it resulted in increasing order so we need to get the second bottom score
    print(uniq[n-2])                        #geting the second bottom score
