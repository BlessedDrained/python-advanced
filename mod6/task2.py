def is_strong_password(password: str, words: set):
    password = password.lower()
    for word in words:
        if word in password:
            return False
    return True


if __name__ == '__main__':
    with open('words.txt', 'r') as f:
        words = set(x for x in f.read().splitlines() if len(x) > 4)
    password = 'jtfwjkfl'
    print(is_strong_password(password, words))
