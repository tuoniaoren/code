import random


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    itmp = []
    while i<=mid and j<=high:
        if li[i] < li[j]:
            itmp.append(li[i])
            i += 1
        else:
            itmp.append(li[j])
            j += 1
    # while执行完，肯定有一部分没数了
    while i<=mid:
        itmp.append(li[i])
        i += 1
    while j<=high:
        itmp.append(li[j])
        j += 1
    li[low:high+1] = itmp


def merge_sort(li, low, high):
    if low < high: #至少有两个元素
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


def merge_sort_test(li, low, high):
    if low < high: #至少有两个元素
        mid = (low + high) // 2
        merge_sort_test(li, low, mid)
        merge_sort_test(li, mid+1, high)
        print(li[low:high+1])


li = list(range(16))
random.shuffle(li)
merge_sort(li, 0, len(li)-1)
print(li)
