from words import *
from outputs import *


word, answer = default()
attempts = 10
used_attempts = 0
correct = True


while True:
    show_status(answer, used_attempts, attempts)
    letter = input("Letter: ")
    if not letter:
        print("You must type letter.")
    else:
        if len(letter) == 1:
            answer, correct = letter_in_answer(letter, answer, word)
        if is_end(letter, answer, word, used_attempts, attempts):
            word, answer = default()
            attempts = 10
            used_attempts = -1
        if not correct:
            used_attempts += 1
