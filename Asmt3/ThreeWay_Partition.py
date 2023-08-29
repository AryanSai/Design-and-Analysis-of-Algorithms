import random

def partition(arr):
    n = len(arr)
    x = arr[0]  # picking the first element as the pivot
    i, j, k = 0, 1, n - 1  # indices for the ? section
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

arr = [random.randint(0, 100) for _ in range(20)]
print("Input Array: {}".format(arr))
print("Threeway Partitioned Array: {}".format(partition(arr)))
