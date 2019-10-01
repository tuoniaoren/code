def sift(li, low, high):
    """
     堆排序
    :param li: 列表
    :param low: 堆的根节点的位置
    :param high: 堆的最后一个元素的位置
    return:
    """
    i = low  # i最开始指向根节点
    j = 2 * i + 1  # j开始是左孩子
    tmp = li[low]  # 把堆顶保存下来
    while (j <= high):  # 只要j位置有数
        if (j + 1 <= high) and (li[j + 1] < li[j]):  # 避免数组越界
            j = j + 1
        if (li[j] < tmp):
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放置在某一级领导的位置
            break
    else:
        li[i] = tmp  # 把tmp放置在叶子节点


def topk(li, k):
    heap = li[0:k]
    # 1.建堆
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
    # 2.遍历剩余n-k个数，调整堆
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 3.此时得到前k大的数的小根堆，然后出数，堆顶为最小值
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap


import random
li = [i for i in range(100)]
random.shuffle(li)
print(topk(li, 10))
