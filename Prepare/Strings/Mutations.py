# Problem Link: https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]    #using slice method to change the character
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
