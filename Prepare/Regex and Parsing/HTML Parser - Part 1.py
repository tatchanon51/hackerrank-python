# Problem Link: https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):                 #Create a sub class that inherit from HTMLParser
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)                   #Modify the print text as needed
        for attr in attrs:                      #Iterate thru attribues and print name and value
                print('->',attr[0],'>',attr[1])
    def handle_starttag(self, tag, attrs):
            print('Start :', tag)
            for attr in attrs:
                print('->',attr[0],'>',attr[1])
    def handle_endtag(self, tag):
        print("End   :", tag)

parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())