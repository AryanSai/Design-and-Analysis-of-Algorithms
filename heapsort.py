def heapify(a):
    n = len(a)
    i = 0
    while i <= n - 1:
        if 2 * i + 1 < n and a[i] > a[2 * i + 1]:
            a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
            heapify(a)
        if 2 * i + 2 < n and a[i] > a[2 * i + 2]:
            a[i], a[2 * i + 2] = a[2 * i + 2], a[i]
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
print(a)
a = heapsort(a)
print(a)
