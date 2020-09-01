from itertools import product
# Question 7

sumNums = lambda x, y: x+y
print(sumNums(1, 3))

# Question 8

allCombos = [(i, j) for i in range(1, 7) for j in range(1, 7)]
# allCombos = product(range(1, j+1), repeat=2)
print(list(allCombos))

# Question 9

joules = [5000, 8000, 10000, 6000, 12000]
engergyByKilocal = [(i, j) for (i, j) in zip(joules, map(lambda j: j/4184, joules))]
# engergyByKilocal = [(i, i/4184) for i in joules]

print(engergyByKilocal)

# Question 10

languages = ["HTML", "JavaScript", "Python", "Ruby"]

print(list(filter(lambda i: i == "Python", languages)))
print([i for i in languages if i == "Python"])
