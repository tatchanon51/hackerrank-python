# Problem Link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import email.utils
import re

for _ in range(int(input())):               #Iterate thru input
    n = email.utils.parseaddr(input())
    if n[0] != '':                          #If the email address is valid the first element of parseaddr function should not be blank.
        patt = r"^[a-zA-Z]+[a-zA-Z0-9-_.]+@{1}[a-zA-Z]+.{1}[a-zA-Z]{1,3}$"          #given email criteria filter
        if bool(re.match(patt,n[1])):
            print(email.utils.formataddr(n))
