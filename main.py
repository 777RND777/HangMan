word = "suspend"
attempts = len(word)
used_attempts = 0
ans = ""
for i in range(len(word)):
    ans += "_"


while True:
    print("______________________")
    print("Attempts:", used_attempts, "/", attempts)
    print("Current:", end=" ")
    for i in ans:
        print(i, end=" ")
    print()

    letter = input("Letter: ")
    if not letter:
        print("You must type letter.")
    else:
        if len(letter) == 1:
            if letter in ans:
                print("You have already guessed that letter.")
            elif letter in word:
                print("Nice.")
                for i in range(len(word)):
                    if letter == word[i]:
                        past = ""
                        if i + 1 < len(word):
                            past = ans[i+1:]
                        ans = ans[:i] + letter + past
            else:
                print("SON OF A BITCH!!!")
        else:
            if letter == word:
                print("You won! The hidden word : " + word)
                break

        if ans == word:
            print("You won! The hidden word : " + word)
            break
        if used_attempts == attempts:
            print("You lost! The hidden word : " + word)
            break
        used_attempts += 1
