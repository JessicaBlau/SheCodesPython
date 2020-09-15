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


cows_and_bulls("abcd", "acdz")
