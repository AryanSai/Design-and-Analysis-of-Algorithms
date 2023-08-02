def heapify(a):
    i = 1
    n = len(a)
    for i in range(1, n):
        child = i
        parent = (i - 1) // 2
        while child > 0 and a[child] < a[parent]:
            a[child], a[parent] = a[parent], a[child]
            child = parent
            parent = (child - 1) // 2
    return a


print(heapify([2, 3, 1, 4, 6, 22]))
