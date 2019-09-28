def linear_search(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i
    else:
        return -1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    b = 7
    x = linear_search(a, b)
    if x != -1:
        print("The number's index is %d!", x)
    else:
        print("The number is not found!")
