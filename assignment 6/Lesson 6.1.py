# Question 1
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guesses_left -= 1
  guess = input("what is your guess?")
  if guess == random_number:
    print ("You Win!")
    break
else:
    print ("You lose.")

#Question 2
hobbies = []

# Add your code below!

for num in range(3):
  hobby = input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print (hobbies)