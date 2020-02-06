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


while ans != word:
    output(used_attempts, attempts)
    letter = input("Letter: ")
    if letter in word:
        print("Nice")
    else:
        print("SON OF A BITCH!!!")
