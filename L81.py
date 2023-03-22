#Katherine O'Roark & Saerin Bong
def total_length(list):
    count = 0
    for x in list:
        count = count+len(x)
    print(count)

total_length(['Queen', 'Rules'])
total_length([])
total_length(['balloons'])
total_length(["", '', "", ''])
