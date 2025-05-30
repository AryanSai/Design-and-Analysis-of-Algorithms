import random


def median_of_5(a):  # median function
    n = len(a)
    if n == 5:
        return a[2]
    elif n == 4:
        return a[1]
    elif n == 3:
        return a[1]
    elif n == 2:
        return a[0]
    else:
        return a[0]


def select(a, i):

    # divide 'a' into sublists of len 5
    sublists = [a[j : j + 5] for j in range(0, len(a), 5)]
    # print(sublists)

    # find medians of sublists
    # medians = [sorted(sublist)[len(sublist) / 2] for sublist in sublists]
    medians = [median_of_5(sorted(sublist)) for sublist in sublists]
    # print(medians)

    if len(medians) <= 5:  # base case
        median = sorted(medians)[len(medians) / 2]
    else:  # call itself recursively
        median = select(medians, len(medians) / 2)

    # partitioning step
    low = [j for j in a if j < median]
    high = [j for j in a if j > median]

    k = len(low)
    if i < k:
        return select(low, i)
    elif i > k:
        return select(high, i - k - 1)
    else:  # median = k
        return median


def median(a):
    if len(a) == 0:
        print("Empty List!!")
    elif len(a) <= 140:  # for list of length less than 140, bruteforce is good enough
        sorted_array = sorted(a)
        print("\nSorted input array: {}".format(sorted_array))
        middle_index = len(sorted_array) // 2
        median = sorted_array[middle_index - 1] if len(sorted_array) % 2 == 0 else sorted_array[middle_index]
        
        print("\nMedian: {}".format(median))
    else:  # for list of length more than 140, we use the select algorithm
        sorted_array = sorted(a)
        print("\nReal Median: {}".format(sorted_array[len(sorted_array) // 2]))
        median = select(a, len(a) // 2)
        print("\nCalculated Median: {}".format(median))


def main():
    a = random.sample(range(0, 1000), 200)
    print("Input Array: {}".format(a))
    median(a)


main()