# Question 4

hundreds = [i*100 for i in range(1, 10) if i % 2 == 0]
print(hundreds)

# Question 5

hundreds = [i if i % 2 else i*100 for i in range(1, 10)]
print(hundreds)

# Question 6

boom7 = [i if i % 7 else 'BOOM' for i in range(1, 100)]
print(boom7)

# Question 4.2

hundreds = map(lambda i: i*100, filter(lambda i: i % 2 == 0, range(1, 10)))
print(list(hundreds))

# Question 5.2

hundreds = map(lambda i: i*100 if i % 2 == 0 else i, range(1, 10))
print(list(hundreds))

# Question 6.2

boom7 = map(lambda i: "BOOM" if i % 7 == 0 else i, range(1, 100))
print(list(boom7))
