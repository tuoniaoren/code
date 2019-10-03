def bucket_sort(li, n=100, max_num=10000):
    """
    :param li: 数列
    :param n:  桶的个数
    :param max_num: 数的范围：0-10000
    :return: 桶内排序可以使用其他的排序。
    """
    buckets = [[] for _ in range(n)]
    for var in li:
        i = min(var // (max_num // n), n-1)
        buckets[i].append(var)  # 将var加入对应的桶中
        j = len(buckets[i]) - 2
        while (j > -1):  # 采用插入排序使得桶内数据有序
            if buckets[i][j] > var:
                buckets[i][j+1] = buckets[i][j]
                j -= 1
            else:
                break
        buckets[i][j+1] = var
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc) # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
    return sorted_li

import random
li = [random.randint(0, 1000) for i in range(10000)]
li = bucket_sort(li)
print(li)