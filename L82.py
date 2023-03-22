#Katherine O'Roark & Saerin Bong
def disappear(x):
    index = len(x)
    while index >= 0:
        print(x[:index])
        index -= 1

disappear('abracadabra')
