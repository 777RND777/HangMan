def create_answer(word):
    answer = ""
    for i in range(len(word)):
        answer += "_"
    return answer


def default():
    word = "suspend"
    return word, create_answer(word), -1, int(1.5 * len(word))
