# Problem Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

_ = input()
rom_no = list(map(int,input().split())) #Get all room numbers
count = Counter(rom_no)                 #make dict room no.:frequency

for num, freq in count.items():         #Iterate thru count dict
    if freq == 1:
        print(num)