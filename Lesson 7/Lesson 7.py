# Question 1
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char is 'A':
        print('X'),
    elif char is 'a':
        print('X'),
    else:
        print(char),

# Question 2

numbers = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
    print(num)

# Add your loop below!
for num in numbers:
    print(num**2)

# Question 3

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print(key+' '+d[key])

# Question 4

choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
    print(index+1, item)

# Question 5

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a >= b:
        print(a)
    elif b > a:
        print(b)

# Question 6

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!') # (It actually is.)
        break
    print('A', f)
else:
    print('A fine selection of fruits!')

# Question 7

names = ['Jess', 'Jonny', 'Danielle']

for name in names:
    if name == 'Jess':
        print("It is Jessica not Jess")
        break;
else:
    print(name)
