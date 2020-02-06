word = "suspend"
attempts = len(word)
used_attempts = 0
ans = ""
for i in range(len(word)):
    ans += "_"


def output(used, amount):
    print("______________________")
    print("Attempts:", used, "/", amount)
    print("Current:", end=" ")
    for i in ans:
        print(i, end=" ")
    print()


while True:
    output(used_attempts, attempts)
    letter = input("Letter: ")
    used_attempts += 1
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
