# heapify top down approach
import random


def heapify(a):
    if a == sorted(a):  # exception case when the passed array is already sorted
        return a

    counter = 0
    i = 1
    n = len(a)
    if n <= 1 or all(
        x == a[0] for x in a
    ):  # boundary case and check if all elements are the same
        return a

    # normal case
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
a = random.sample(range(0, 200), 12)
print("The input array is {}".format(a))
heap_a = heapify(a)
print("The array after heapify: {}".format(heap_a))
