# heapify bottom up approach
import random


def heapify(a):
    if a == sorted(a):  # exception case when the passed array is already sorted
        return a

    n = len(a)

    if n <= 1 or all(
        x == a[0] for x in a
    ):  # boundary case and check if all elements are the same
        return a

    # normal case
    i = n // 2
    counter = 0
    for i in range(len(a) // 2, -1, -1):
        while True:
            minimum = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and a[left] < a[minimum]:
                minimum = left
            if right < n and a[right] < a[minimum]:
                minimum = right
            if i != minimum:
                a[i], a[minimum] = a[minimum], a[i]
                i = minimum
            else:
                break
            counter += 1
    # print("Count = {}".format(counter))
    return a


a = random.sample(range(0, 200), 3)
# a = [1, 2, 3]
print("The input array is {}".format(a))
heap_a = heapify(a)
print("The array after heapify: {}".format(heap_a))
