word = "python"
ans = ""
attempts = 0
used_attempts = 0


def output(used, amount):
    print("___________________")
    print("Attempts:", used, "/", amount)
    print("Current:", end=" ")
    for i in range(len(word)):
        print("_", end=" ")
    print()


while ans != word:
    output(used_attempts, attempts)
    letter = input("Letter: ")
    if letter in word:
        print("Nice")
    else:
        print("SON OF A BITCH")
