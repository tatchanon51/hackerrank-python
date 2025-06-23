# Problem Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())                                                                #Get the number of student
    student_marks = {}                                                              #Create a dict to collect names and scores
    for _ in range(n):                                                              #Iterate to get all names and scores
        name, *line = input().split()
        scores = list(map(float, line))                                             #Make all scores to list and Set type to float
        student_marks[name] = scores                                                #Match the name to the score list and put it in the dict
    query_name = input()                                                            #Get the query name
    print('%.2f' % (sum(student_marks[query_name])/len(student_marks[query_name]))) #Calculate the average value and print in 2 decimal places
