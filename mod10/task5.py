def find_insert_index(arr, value):
    if len(arr) == 0:
        return 0
    if value < arr[0]:
        return 0
    if value >= arr[-1]:
        return len(arr) - 1

    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if value < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    test = [1, 2, 3, 4, 6, 6, 6, 6, 7]
    print(find_insert_index(test, 5)) # 4
