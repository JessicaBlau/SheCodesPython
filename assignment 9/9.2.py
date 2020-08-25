# Question 4

hundreds = [i*100 for i in range(1, 10) if i % 2 == 0]
print(hundreds)

# Question 5

hundreds = [i if i % 2 else i*100 for i in range(1, 10)]
print(hundreds)

# Question 6

boom7 = [i if i % 7 else 'BOOM' for i in range(1, 100)]
print(boom7)
