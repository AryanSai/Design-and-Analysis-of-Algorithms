import random


def select(A, i):

    # divide A into sublists of len 5
    sublists = [A[j : j + 5] for j in range(0, len(A), 5)]
    print(sublists)

    medians = [sorted(sublist)[len(sublist) / 2] for sublist in sublists]
    print(medians)

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) / 2]
    else:
        # the pivot is the median of the medians
        pivot = select(medians, len(medians) / 2)

    # partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return select(low, i)
    elif i > k:
        return select(high, i - k - 1)
    else:  # pivot = k
        return pivot


a = random.sample(range(0, 100), 55)

print(a)
print("\n")

b = sorted(a)
print(b)
print("\n")

median_array = select(a, len(a) // 2)
print(median_array)
