import random
import string


def cows_and_bulls(string: str, guess: str):
    bools = 0
    hits = 0
    counter = 0
    counterG = 0
    for char in string:
        for charG in guess:
            if char == charG and counter == counterG:
                bools += 1
            elif char == charG:
                hits += 1
        counterG += 1
    counter += 1
    print("bools:", bools, "hits:", hits)
    if bools == len(string):
        return True
    else:
        return False


def boolsAndHits():
    word = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 20)))
    guess = input("enter your guess:\n")
    if not guess.isalpha() or None:
        guess = input("Please enter valid input:")
    result = cows_and_bulls(word, guess)
    if result is True:
        print("You Win!")
    else:
        boolsAndHits()


boolsAndHits()

