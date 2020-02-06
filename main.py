from words import *
from outputs import *


word, answer, attempts = default()
used_attempts = 0


while True:
    show_status(answer, used_attempts, attempts)
    letter = input("Letter: ")
    if not letter:
        print("You must type letter.")
    else:
        if len(letter) == 1:
            answer = letter_in_answer(letter, answer, word)
        if is_end(letter, answer, word, used_attempts, attempts):
            word, answer, attempts = default()
            used_attempts = -1
        used_attempts += 1
