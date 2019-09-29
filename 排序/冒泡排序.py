import numpy as np
"""
冒泡排序把最大的值排到了最后一位，依次类推
"""


def bubbleSort(lyst):
    n = len(lyst)
    while n >1:
        i = 0
        while i < n-1:
            j = i + 1
            if lyst[i] > lyst[j]:
                temp = lyst[i]
                lyst[i] = lyst[j]
                lyst[j] = temp
            i += 1
        n -= 1


if __name__ == "__main__":
    lyst = np.random.rand(10) * 100
    bubbleSort(lyst)
    print(lyst)
