import random

#Question 1


def SevenBoom():

    x = random.randint(1, 51)
    if x % 7 == 0:
        return "boom"
    else:
        return x

def SevenBoom1():

    y = random.randint(1, 21)
    num = input("Next Number")
    if num == "boom":
        if y % 7 == 0:
            return "Good"
        else:
            return "Wrong"
    elif int(num) > 20:
        return "The number is to big"
    elif int(num) < 0:
        return "The number is to small"
    elif int(num) == y:
        return num
    else:
        return "Wrong"


i = 0
while (1):
    if i == 0:
        if SevenBoom1() == "Wrong":
            break
        else:
            i += 1
    else:
        print(SevenBoom())
        i -= 1
