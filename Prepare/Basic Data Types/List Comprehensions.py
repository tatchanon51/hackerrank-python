# Problem Link: https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = []                                          #Create list of 'i' to collect all possible i below or equal x
    j = []                                          #Create list of 'j' to collect all possible j below or equal y
    k = []                                          #Create list of 'k' to collect all possible k below or equal z

    x+=1                                            # x = x+1 to get x value in for function below
    y+=1                                            # y = y+1 to get y value in for function below
    z+=1                                            # z = z+1 to get z value in for function below

    ans = []                                        #Create list of all possible answers
    
    for ite in range(x):                            #Iterate thru x value to get all possible i
        i.append(ite)
    for ite in range(y):                            #Iterate thru y value to get all possible j
        j.append(ite)
    for ite in range(z):                            #Iterate thru z value to get all possible k
        k.append(ite)
        
    for itei in i:                                  #Iterate thru i,j,k to get all possible coordinate
        for itej in j:
            for itek in k:
                if n != (itei+itej+itek):           #Check if the sum of coordinate i+j+k is not equal to n  
                    ans.append([itei,itej,itek])    #Append all answers to 'ans'
    print(ans)
