"""
贪心算法
问题介绍：
换零钱问题，使用最少数量的纸币换取等额的钱，其中纸币的面额为[100, 50, 20, 5, 1]
"""


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money     # 例如376， 376//100=3
        n = n % money
    return m,n


t = [100, 50, 20, 5, 1]
print(change(t, 376))
