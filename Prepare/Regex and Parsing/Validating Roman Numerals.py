# Problem Link: https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true

'''
Explaination
Try to convert each digit
For 1-9, they will be I II III IV V VI VII VIII IX that group will be (IX|IV|V?I{0,3}) and this is the end of string so +$
For 10-90, they will be X XX XXX XL L LX LXX LXXX XC that group will be (XC|XL|L?X{0,3})
For 100-900, they will be C CC CCC CD D DC DCC DCCC CM that group will be (CM|CD|D?C{0,3})
For 1000-3000, the will be X XX XXX and this is the heading of the string so + ^ 

'''
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.


import re
print(str(bool(re.match(regex_pattern, input()))))
