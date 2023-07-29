def heapify(a):
    n = len(a)
    for i in range(n):
        if 2 * i + 1 < n:
            if a[i] > a[2 * i + 1]:
                a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
                heapify(a)
        if 2 * i + 2 < n:
            if a[i] > a[2 * i + 2]:
                a[i], a[2 * i + 2] = a[2 * i + 2], a[i]
                heapify(a)
    return a


def heapsort(a):
    i = 0
    n = len(a)
    while i <= n - 1:
        a[i:] = heapify(a[i:])
        i = i + 1
    return a


a = [7, 3, 2, 4, 5, 8, 1]
print(a)
a = heapsort(a)
print(a)
