import math

string = str(input("Enter String: "))

def mid(string):
    enum = list(enumerate(string))
    lastnum = enum[-1][0] + 1
    if lastnum % 2 == 0:
        return ""
    else:
        middle = math.floor(len(enum)/2)
        x = enum[middle][1]
        print(x)
        return x

mid(string)