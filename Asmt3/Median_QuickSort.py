import random


def median(l):
    l = sorted(l)
    # print(l[1])
    return l[1]


def partition(arr):
    n = len(arr)
    ind = arr.index(median([arr[0], arr[len(arr) / 2], arr[len(arr) - 1]]))
    x = arr[ind]
    i, j = 0, n - 1
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
        arr[ind], arr[i - 1] = arr[i - 1], arr[ind]
    # print(arr)
    return i - 1


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = partition(arr)
    arr[:pivot] = quicksort(arr[:pivot])
    arr[pivot + 1 :] = quicksort(arr[pivot + 1 :])
    print(arr)
    return arr


# arr = [7, 5, 12, 9, 2, 1, 4]
arr = random.sample(range(0, 100), 7)
# arr = [92, 84, 17, 10, 6, 45, 74]
print(arr)
print(quicksort(arr))
