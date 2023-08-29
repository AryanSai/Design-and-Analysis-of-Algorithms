import random


def partition(arr):
    n = len(arr)
    x = arr[0]  # picking the first element as the pivot
    i, j = 1, n - 1 #indices for the ? section
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


arr = [random.randint(0, 100) for _ in range(20)]
print("Input Array: {}".format(arr))
print("Twoway Partitioned Array: {}".format(partition(arr)))
