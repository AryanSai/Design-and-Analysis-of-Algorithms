# heapify top down approach

import random


def heapify(a):
    counter = 0
    i = 1
    n = len(a)
    for i in range(1, n):
        child = i
        parent = (i - 1) // 2
        while child > 0 and a[child] < a[parent]:
            a[child], a[parent] = a[parent], a[child]
            child = parent
            parent = (child - 1) // 2
            counter += 1
    # print("Count = {}".format(counter))
    return a


# a = [8, 6, 4, 2, 0, 3, -2]
a = random.sample(range(0, 20), 12)
print(a)
a = heapify(a)
print(a)
