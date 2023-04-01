chars = {
    '2': "abc",
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def is_convenient_word(word, code):
    for i in range(len(min(word, code))):
        if word[i] not in chars[code[i]]:
            return False
    return True


if __name__ == '__main__':
    code = input()
    with open('words.txt', 'r') as f:
        answers = []
        for word in f.readlines():
            word = word[:-1]
            if is_convenient_word(word, code):
                answers.append(word)
    print(answers)
