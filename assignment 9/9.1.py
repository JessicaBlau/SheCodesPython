# Question 1

movie = ['The Notebook', 'Maleficent', 'Batman v Superman', 'Black Swan', 'Gone Girl', 'War of the Worlds',
         'Just Married']
actor = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman', 'Rosamund Pike', 'Dakota Fanning',
         'Brittany Murphy']

lists = [i+" is played by "+j for (i, j) in zip(movie, actor)]

print(lists)

# Question 2

movies = dict(zip(movie, actor))

print(movies)

# Question 3

newList = [i+" is played by "+j for (i, j) in movies.items()]

print(newList)


