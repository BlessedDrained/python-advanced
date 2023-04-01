import re


def get_all_words(string):
    substrings = []
    for i in range(len(string)):
        substr = ""
        for j in range(i, len(string)):
            substr += string[j]
            if len(substr) > 4:
                substrings.append(substr)
    return substrings


def is_strong_password(password: str, words: set):
    password = password.lower()
    substrings = get_all_words(password)
    for substring in substrings:
        if substring in words:
            return False
    return True


if __name__ == '__main__':
    with open('words.txt', 'r') as f:
        words = set(sorted(x for x in f.read().splitlines() if len(x) >= 4))
    print(is_strong_password('jtfwjkfl', words))
