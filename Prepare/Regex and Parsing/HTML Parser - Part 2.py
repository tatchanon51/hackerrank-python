# Problem Link: https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true

from html.parser import HTMLParser

class modhtmlparserr(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)


m = modhtmlparserr()
htmlcod = '\n'.join(input() for _ in range((int(input()))) )
m.feed(htmlcod)
