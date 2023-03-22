#Katherine O'Roark & Saerin Bong
def count_characters(word, x):
    index = 0
    count = 0
    while index < len(word):
        if word[index] == x:
            count = count+1
        index+=1
    print(count)

count_characters('Goodbye', 'o')
