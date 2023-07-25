import random


def partition(arr):
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
    return arr


arr = [3, 5, 3, 5, 7, 8, 5, 2, 4, 1]
# arr = random.sample(range(0, 100), 10)
print(arr)
print(partition(arr))
