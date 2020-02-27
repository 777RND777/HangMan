def show_status(ans, used, amount):
    print("______________________")
    print("Attempts:", used, "/", amount)
    print("Current:", end=" ")
    for i in ans:
        print(i, end=" ")
    print()


def letter_in_answer(letter, answer, word):
    correct = False
    if letter in answer:
        print("You have already guessed that letter.")
    elif letter in word:
        print("Nice.")
        correct = True
        for i in range(len(word)):
            if letter == word[i]:
                past = ""
                if i + 1 < len(word):
                    past = answer[i + 1:]
                answer = answer[:i] + letter + past
    else:
        print("SON OF A BITCH!!!")
    return answer, correct


def is_end(letter, answer, word, used, amount):
    if letter == word:
        print("You won! The hidden word : " + word + ".")
        return True
    if answer == word:
        print("You won! The hidden word : " + word + ".")
        return True
    if used == amount:
        print("You lost! The hidden word : " + word + ".")
        return True
    return False
