import random

def find_largest(a):
    if len(a) == 0:
        return float("-inf")
    elif len(a) == 1:
        return a[0]
    else:
        print(a[: len(a) / 2])
        max1 = find_largest(a[: len(a) / 2])
        print(a[len(a) / 2 :])
        max2 = find_largest(a[len(a) / 2 :])
        if max1 > max2:
            return max1
        else:
            return max2


a = random.sample(range(0, 100), 5)
print(a)
print("\nThe largest element is {}!".format(find_largest(a)))
