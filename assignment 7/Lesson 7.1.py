# Question 1.a
def PrintStars(n):
    for num in range(0, n+2):
            print('*'*num)


# Question 1.b


t = input("Enter a number")
for num1 in range(1, int(t)):
        PrintStars(int(num1))


# Question 2


n = input("Enter a number")
for num2 in range(2, int(n)+2):
        print('*'*num2)

# Question 3


s = input("Enter a number")
for num3 in range(0, int(s)+1):
    print('*'*num3)
for num4 in range(1, int(s)):
    print("*"*(int(s)-num4))
