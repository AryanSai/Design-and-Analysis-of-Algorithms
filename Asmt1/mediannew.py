import random


def median_of_5(a):
    sorted_a = sorted(a)
    n = len(a)
    if n == 5:
        return sorted_a[2]
    elif n == 4:
        return sorted_a[1]
    elif n == 3:
        return sorted_a[2]
    elif n == 2:
        return sorted_a[0]
    else:
        return sorted_a[0]

def median11(a):
    n = len(a)

    # divide the list into sublists
    sublists = [a[j : j + 5] for j in range(0, n, 5)]
    print(sublists)

    # sort the sublists
    sublists = [sorted(i) for i in sublists]
    print(sublists)

    # find medians of sublists
    medians = []
    for i in sublists:
        medians.append(median_of_5(i))

    medians=sorted(medians)
    print(medians)

    if len(medians) <= 5:  # Base case
        x = median_of_5(medians)
    else:
        # Find the median of medians
        x = median11(medians)
    print("x = ", x)

    # Partition the input array around the median-of-medians x
    low_side = [elt for elt in a if elt < x]
    print(low_side)

    high_side = [elt for elt in a if elt > x]
    print(high_side)

    k = len(low_side) + 1
    print("k=", k)
    print("n=", n)

    if n % 2 == 1:  # odd number of elements
        i = (n + 1) // 2
    else:  # even number of elements
        i = n // 2
    print("i=", i)

    if i == k:
        return x
    elif i < k:
        return median11(low_side)
    else:
        return median11(high_side)


# Test the function
a = random.sample(range(0, 100), 25)
print("Input array:", a)
print("Sorted array:", sorted(a))
median_value = median11(a)
print("The median is:", median_value)
