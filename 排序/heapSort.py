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
        if (j + 1 <= high) and (li[j + 1] > li[j]):  # 避免数组越界
            j = j + 1   # 若右孩子大于左孩子，则j指向右孩子
        if (li[j] > tmp):
            li[i] = li[j]
            i = j       # 向下调整
            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放置在某一级领导的位置
            break
    else:
        li[i] = tmp  # 把tmp放置在叶子节点


def heapSort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # i表示建堆时根节点的下标
        sift(li, i, n - 1)   # high等于n-1是因为当构建堆时，上面变动了，下面也要重新调整一下。
    # 建堆完成
    for i in range(n - 1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
    print(li)


li = [i for i in range(10)]
import random
random.shuffle(li)
print(li)
heapSort(li)
