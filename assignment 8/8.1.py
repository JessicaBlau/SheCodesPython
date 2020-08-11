def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n


print(factorial(5))


def add_one(n):
    if n == 0:
        return 0
    return add_one(n+1)


# print(add_one(5))


def triangle_numbers(n):
    if n == 0:
        return 0
    return triangle_numbers(n-1) + n


print(triangle_numbers(5))


def sum_digit(num):
    if num == 0:
        return 0
    return sum_digit(int(num / 10)) + num % 10


print(sum_digit(578))


def count_x(str):
    if str == '':
        return 0
    last_num = str[-1]

    if last_num == 'x':
        return count_x(str[:-1]) + 1
    return count_x(str[:-1]) + 0


print(count_x("xxxyyyx"))


# Question 6
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n


print(sum(5))


# Question 7
def sum_every_other_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_every_other_num(n-2)


print(sum_every_other_num(3))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(0))


# Question 8
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n/2)+1
    else:
        return hailstone(n*3+1)+1


a = hailstone(10)
print(a)


# Question 12
def paths(m, n):
    if n == 1 or m == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)


print(paths(5, 7))
