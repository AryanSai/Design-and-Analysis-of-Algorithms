import random


def partition(arr):
    n = len(arr)
    if n > 0:
        x = arr[0] # picking the first element as the pivot
        i, j = 1, n - 1
        while i <= j:
            if arr[i] <= x:
                i = i + 1
            elif arr[j] > x:
                j = j - 1
            else:  # arr[i]>x or arr[j]<=x
                arr[i], arr[j] = arr[j], arr[i]
                i = i + 1
                j = j - 1
        else:  # i>j
            arr[0], arr[i - 1] = arr[i - 1], arr[0]
        return i - 1
    else:
        return -1


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = partition(arr)
    arr[:pivot] = quicksort(arr[:pivot])
    arr[pivot + 1 :] = quicksort(arr[pivot + 1 :])
    return arr


arr = [random.randint(0, 100) for _ in range(20)]
print("Input Array: {}".format(arr))
print("Sorted Array: {}".format(quicksort(arr)))
