def insertionSort(lyst):
    temp = []
    temp.append(lyst[0])
    for i in range(1, len(lyst)):
        for j in range(len(temp)):
            if temp[j] > lyst[i]:
                x = temp[j]
                temp[j] = lyst[i]
                k = len(temp) - 1
                temp.append(temp[k])
                while (k > j + 1):
                    temp[k] = temp[k - 1]
                    k = k - 1
                temp[j + 1] = x
                break
        else:
            temp.append(lyst[i])
    return temp


def insertionSort2(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i = i + 1


if __name__ == '__main__':
    a = [7, 6, 5, 4, 3, 2, 1]
    b = insertionSort(a)
    insertionSort2(a)
    print(a)
    print(b)
