def facturiol(n):
    if (n == 0):
        return 1
    return facturiol(n-1)*n

print (facturiol(5))

def AddOne(n):
    if (n == 0):
        return 0
    return AddOne(n+1)

#print(AddOne(5))

def TriangleNumbers(n):
    if n == 0:
        return 0
    return TriangleNumbers(n-1) + n

print (TriangleNumbers(5))

def SumDigit(num):
    if num == 0:
        return 0
    return SumDigit(int(num / 10)) + num % 10

print (SumDigit(578))

def countX(str):
    if str == '':
        return 0
    lastNum = str [-1]

    if lastNum == 'x':
        return countX(str[:-1]) + 1
    return countX(str[:-1]) + 0

print (countX("xxxyyyx"))

# Question 6
def sum (n):
    if n == 0:
        return 0
    return sum(n-1) + n

print (sum(5))
