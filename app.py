from random_words import RandomWords
import random
import string
import time


def analyze_word(word, letters):
    res = ''
    for x in word:
        if x in letters:
            res += " " + x
        else:
            res += "-"
    return res

def input_word(word):
    if word == "":
        raise Exception("Invalid word")
    start_time = time.time()
    letters = []
    ascii_alph = string.ascii_letters
    analyze_word(word, letters)
    while True:
        letter = random.choice(ascii_alph)

        if letter in word:
            if letter not in letters:
                letters.append(letter)

        res = analyze_word(word, letters)

        if "-" not in res:
            print("You won the game!")
            end_time = time.time()
            print("Time for guessing: ", (end_time - start_time))
            break
        return True

