import sys


def decrypt(cypher):
    chars = [x for x in cypher]
    stack = []
    dots_count = 0
    for i in range(len(chars)):
        stack.append(chars[i])
        if chars[i] == '.':
            dots_count += 1
        elif dots_count == 1 and len(stack) > 0:
            stack.pop()
            stack.pop()
            stack.append(chars[i])
            dots_count = 0
        if dots_count == 2:
            stack.pop()
            stack.pop()
            if len(stack) > 0:
                stack.pop()
            dots_count = 0
    stack = [x for x in stack if x != '.']
    return "".join(stack)


if __name__ == '__main__':
    data = sys.stdin.readline()
    sys.stdout.write(decrypt(data))
    sys.stdout.flush()
