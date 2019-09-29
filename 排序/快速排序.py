def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右面找到比tmp小的值
            right -= 1  # right往左走
        li[left] = li[right]  # 把右边的值写到左边空位
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 3, 4, 6, 7, 8, 9]
quick_sort(li, 0, len(li) - 1)
print(li)
