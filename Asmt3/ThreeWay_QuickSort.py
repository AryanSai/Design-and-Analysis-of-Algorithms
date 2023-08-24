import random


def partition(arr):  # three way partition
    n = len(arr)
    x = arr[0]
    i, j, k = 0, 1, n - 1
    while j <= k:
        if arr[j] < x:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j + 1
        elif arr[j] == x:
            j = j + 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k = k - 1
    return k


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = partition(arr)
    arr[:pivot] = quicksort(arr[:pivot])
    arr[pivot + 1 :] = quicksort(arr[pivot + 1 :])
    return arr


arr = [random.randint(0, 100) for _ in range(13)]
print(arr)
print(quicksort(arr))
print(arr)
