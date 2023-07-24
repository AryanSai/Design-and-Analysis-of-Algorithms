import random


def partition(arr):
    n = len(arr)
    x = arr[0]
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
    return arr


# arr = [7, 5, 12, 9, 2, 1, 4]
arr = random.sample(range(0, 100), 10)
print(arr)
print(partition(arr))
