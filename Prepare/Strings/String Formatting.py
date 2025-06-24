def print_formatted(number):
    # your code goes here
    sp = len(bin(number)[2:])       #Find the space needed in each column

    for i in range(number):         #Iterate to generate each row
        i +=1
        print(str(i).rjust(sp,' '),oct(i)[2:].rjust(sp,' '),hex(i)[2:].upper().rjust(sp,' '),bin(i)[2:].rjust(sp,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
