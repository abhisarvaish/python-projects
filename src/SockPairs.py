# Code to determine pairs of numbers in list
from functools import reduce


def sockMerchant(ar):
    element_count = {key: ar.count(key) for key in ar}
    pair_list = [x[1] // 2 for x in element_count.items()]
    pair_count = reduce(lambda x, y: x + y, pair_list)
    print(pair_count)


sockMerchant([10, 20, 20, 10, 10, 3050, 10, 20, 60])
