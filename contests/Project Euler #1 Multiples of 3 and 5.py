# Problem Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/

def sum_of_arithmetic_sequence(n, factor):
    t = n // factor # Find the maximum times
    s = t*(factor+factor*t) // 2 # Adapt from sum of arithmetic sequence formula
    return s

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())-1 
    result = sum_of_arithmetic_sequence(n, 3) + sum_of_arithmetic_sequence(n, 5) - sum_of_arithmetic_sequence(n, 15) 
    print(int(result))
