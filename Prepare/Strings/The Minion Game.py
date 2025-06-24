# Problem Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'                        
    Stuart_score = 0
    Kevin_score = 0
    length = len(string)

    for i in range(length):                 #Iterate to each string
        if string[i] in vowels:
            Kevin_score += length - i       #If the index is a vowel then the remaining length are all string start with the vowel
        else:
            Stuart_score += length - i      #If the index isn't a vowel then the remaining length are all string start with the consonant

    if Stuart_score > Kevin_score:
        print(f"Stuart {Stuart_score}")
    elif Kevin_score > Stuart_score:
        print(f"Kevin {Kevin_score}")
    else:
        print("Draw")



