# Problem Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import OrderedDict
import re
dict = OrderedDict()
patt = r'(?P<NAME>[a-zA-Z]+ ?[a-zA-Z]*) (?P<PRICE>[0-9]+)'      #pattern for detect names and prices
for i in range(int(input())):
    a = re.match(patt,input())
    if a.group('NAME') in dict:                                 #check if the item is already in the dict
        dict[a.group('NAME')] = (dict[a.group('NAME')]+int(a.group('PRICE'))) #Sum the prices and update the dict
    else:
        dict[a.group('NAME')] = int(a.group('PRICE'))
for i  in dict.items():
    print(i[0],i[1])