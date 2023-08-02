import random


def printer(lst):
    for i in range(0, len(lst), 5):
        row_elements = lst[i : i + 5]
        print(" ".join(map(str, row_elements)))


def median(arr):
    i = 0
    n = len(a)
    while i + 5 < n:
        b = a[i : i + 5]
        b.sort()
        a[i : i + 5] = b
        i = i + 5
    else:
        b = a[i:]
        b.sort()
        a[i:] = b

    print("sorted rows:")
    printer(a)

    i = 2
    median_array = []
    while i < len(a):
        median_array.append(arr[i])
        i += 5

    remainder = len(a) % 5
    print(remainder, n)
    if remainder == 4:
        print(a[len(a) - 4], n)
        median_array.append(a[len(a) - 4])
    elif remainder == 3:
        print(a[len(a) - 3], n)
        median_array.append(a[len(a) - 3])
    elif remainder == 2:
        print(a[len(a) - 2], n)
        median_array.append(a[len(a) - 2])
    else:
        median_array.append(a[len(a) - 1])
    return median_array


a = random.sample(range(0, 100), 29)
# a=[2,5,1,8,23,34,45,12,9,7,3,4,11,49,10,16]
printer(a)
print("\n")

median_array = median(a)
print(median_array)
