from random_word import RandomWords


def create_answer(word):
    answer = ""
    for i in range(len(word)):
        answer += "_"
    return answer


def default():
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true")
    return word, create_answer(word), int(1.5 * len(word))
