import random


def median_of_medians(A, i):

    # divide A into sublists of len 5
    sublists = [A[j : j + 5] for j in range(0, len(A), 5)]
    print(sublists)

    medians = [sorted(sublist)[len(sublist) / 2] for sublist in sublists]
    print(medians)

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) / 2]
    else:
        # the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians) / 2)

    # partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        return median_of_medians(high, i - k - 1)
    else:  # pivot = k
        return pivot


a = random.sample(range(0, 100), 25)
# a=[2,5,1,8,23,34,45,12,9,7,3,4,11,49,10,16]
a=[61, 18, 51, 98, 29, 48, 22, 93, 20, 24, 87, 97, 14, 92, 73, 82, 27, 23, 91, 3, 2, 64, 0, 13, 53]

print(a)
print("\n")

b = sorted(a)
print(b)
print("\n")

median_array = median_of_medians(a, len(a) // 2)
print(median_array)
