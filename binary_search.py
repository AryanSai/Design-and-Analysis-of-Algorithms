import random


def binarysearch(a, x, l, u):
    while l != u:
        m = (l + u) // 2
        if x < a[m]:
            return binarysearch(a, x, l, u - 1)
        elif x > a[m]:
            return binarysearch(a, x, l + 1, u)
        else:
            return a[m]
    else:
        return 0


a = random.sample(range(0, 10000), 500)
a.sort()
# a = [1, 3, 5, 12, 34, 56, 78]
print(a)
x = random.sample(a, 1)
print(x[0])
if binarysearch(a, x[0], 0, len(a)) != 0:
    print("The element exists!!")
else:
    print("The element does not exist!!")
