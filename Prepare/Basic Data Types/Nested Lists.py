#Problem Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []                        #Create a list to contain all records
    for _ in range(int(input())):       #Iterate to get all score
        name = input()
        score = float(input())
        records.append([name,score])
        
    def myfunc(x):                      #Define function to return only score
        return x[1]
        
    records.sort(key = myfunc)          #Sort records by score
    
    scores = list(zip(*records))[1]     #Make a list that contain only scores
    uniq_score = list(set(scores))      #get a list of unique scores
    uniq_score.sort()                   #sort the unique score in increasing order
    #uniq_score[1]                       #geting the second bottom score
    
    final=[]                            #Create an answer list
    for [x,y] in records:               #Iterate thru records
        if y == uniq_score[1]:          #Check if the record's score is equal the scond bottom place or not
            final.append(x)             #Collect only the name
    final.sort()                        #Sort the names in alphabet order
    for x in final:                     #Print the answers
        print(x)
