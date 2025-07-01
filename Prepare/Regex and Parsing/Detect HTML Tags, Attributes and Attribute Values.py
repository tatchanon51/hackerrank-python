# Problem Link: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for att,val in attrs:
            print('->',att,'>',val)

inp = []                                    #setup list to keep all input
for _ in range(int(input())):               #loop to get all input
    inp.append(input())

inp = '\n'.join(inp)                        #join all input with \n

par = MyHTMLParser()                        #Create MyHTMLParser object
par.feed(inp)                               #Feed all input thru the object