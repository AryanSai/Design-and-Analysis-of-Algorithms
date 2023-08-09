import random


def insertion_sort(a):
    n = len(a)
    for j in range(1, n):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


# a = [12, 11, 13, 5, 6]
a = random.sample(range(0, 100), 50)
print("The list of elements: {}".format(a))
print("The sorted list of elements: {}".format(insertion_sort(a)))
