#Katherine O'Roark & Saerin Bong
def until_dot(s):
    index = 0
    while index < len(s) and s[index] != '.':
        index+=1
    print(s[:index])

until_dot("this is a sentence. this is another.")
until_dot("192.168.200.2")
until_dot("No dot here")
