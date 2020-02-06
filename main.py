from outputs import *

word = "suspend"
attempts = len(word)
used_attempts = 0
answer = ""
for i in range(len(word)):
    answer += "_"


while True:
    show_status(answer, used_attempts, attempts)
    letter = input("Letter: ")
    if not letter:
        print("You must type letter.")
    else:
        if len(letter) == 1:
            answer = letter_in_answer(letter, answer, word)
        if is_end(letter, answer, word, used_attempts, attempts):
            break
        used_attempts += 1
