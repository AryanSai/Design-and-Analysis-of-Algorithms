import random


def minmax(a):
    if len(a) == 0:  # exception case
        return float("-inf"), float("inf")
    elif len(a) == 1:  # boundary case
        return a[0], a[0]
    elif len(a) == 2:  # base case
        return min(a[0], a[1]), max(a[0], a[1])
    else:  # normal case
        min1, max1 = minmax(a[: len(a) // 2])
        min2, max2 = minmax(a[len(a) // 2 :])
        return min(min1, min2), max(max1, max2)


a = random.sample(range(0, 100), 10)
# a = []
print(a)

min, max = minmax(a)
print("\nThe minimum element is {}!".format(min))
print("The maximum element is {}!".format(max))
