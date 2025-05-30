import random


def heapify(a):
    n = len(a)
    i = 0
    while i <= n - 1:
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and a[i] > a[left]:
            a[i], a[left] = a[left], a[i]
            heapify(a)
        if right < n and a[i] > a[right]:
            a[i], a[right] = a[right], a[i]
            heapify(a)
        i = i + 1
    return a


def heapsort(a):
    i = 0
    n = len(a)
    while i <= n - 1:
        a[i:] = heapify(a[i:])
        i = i + 1
    return a


a = [8, 6, 4, 2, 0, 3, -2]
a = random.sample(range(0, 20), 12)
print(a)
a = heapsort(a)
print(a)
