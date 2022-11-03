#theauthorsaremaggiedunnandcodybrown
def until_dot(x):
    index = 0
    while index < len(x) and x[index]!= ".":
        index += 1
    print(x[:index])

until_dot("This is a sentence. This is another.")
until_dot("192.168.200.2")
until_dots("no dots here")
