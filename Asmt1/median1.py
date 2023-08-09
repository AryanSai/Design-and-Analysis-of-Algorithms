import random

def median_of_5(a):
    n = len(a)
    if n == 5:
        return a[2]
    elif n == 4:
        return a[1]
    elif n == 3:
        return a[2]
    elif n == 2:
        return a[0]
    else:
        return a[0]

def select(a, i):
    # divide a into sublists of len 5
    sublists = [a[j : j + 5] for j in range(0, len(a), 5)]
    print(sublists)

    # find medians of sublists
    medians = [median_of_5(sorted(sublist)) for sublist in sublists]
    print(medians)

    if len(medians) <= 5:  # base case
        median = sorted(medians)[len(medians) / 2]
    else:  # call itself recursively
        median = select(medians, len(medians) / 2)

    # partitioning step
    low = [j for j in a if j < median]
    high = [j for j in a if j > median]

    k = len(low) + 1
    if i < k:
        return select(low, i)
    elif i > k:
        return select(high, i - k - 1)
    else:  # median = k
        return median


a = random.sample(range(0, 100), 25)

print(a)
print("\n")

b = sorted(a)
print(b)
print("\n")

median_array = select(a, len(a) // 2)
print(median_array)