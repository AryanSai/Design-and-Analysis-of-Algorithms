import random


def find_second_largest(a):
    if len(a) == 0:    # exception case
        return float("-inf"), float("-inf")
    elif len(a) == 1:  # boundary case
        return a[0], float("-inf")
    elif len(a) == 2:  # base case
        return max(a[0], a[1]), min(a[0], a[1])
    else:              # normal case
        max1, sec1 = find_second_largest(a[: len(a) // 2])
        max2, sec2 = find_second_largest(a[len(a) // 2 :])
        maxi = max(max1, max2)
        if max1 > max2:
            second_max = max(sec1, max2)
        else:
            second_max = max(sec2, max1)
        return maxi, second_max


# a = [5, 2, 8, 10, 1, 6, 12, 13]
a = random.sample(range(0, 100), 10)
print(a)
largest, second_largest = find_second_largest(a)
print("The largest element is {}!".format(largest))
print("The second largest element is {}!".format(second_largest))
