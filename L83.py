#theauthorsaremaggiedunnandcodybrown

#for loop version
def character_count_2(x, y):
    total = 0
    for z in range(0, len(x)):
        if x[z] == y:
            total += 1
    print(total)

#while loop version
def character_count(x, y):
    total = 0
    index = 0
    while index < len(x):
        if x[index] == y:
            total += 1
        index += 1
    print(total)
