import random


def find_largest(a):
    if len(a) == 0:
        return float("-inf")
    elif len(a) == 1:
        return a[0]
    elif len(a) == 2:
        if a[0] > a[1]:
            return a[0]
        else:
            return a[1]
    else:
        max1 = find_largest(a[: len(a) / 2])
        max2 = find_largest(a[len(a) / 2 :])
        if max1 > max2:
            return max1
        else:
            return max2


a = random.sample(range(0, 100), 100)
print(a)
# print(a[: len(a) / 2])
# print(a[len(a) / 2 :])
print(find_largest(a))
