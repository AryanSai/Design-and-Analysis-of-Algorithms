import random

def minmax(a):
    if len(a) == 0:
        return float('-inf'), float('inf')
    elif len(a) == 1:
        return a[0], a[0]
    else:
        min1, max1 = minmax(a[:len(a)//2])
        min2, max2 = minmax(a[len(a)//2:])
        return min(min1, min2), max(max1, max2)


a = random.sample(range(0, 100), 5)
print(a)

min, max = minmax(a)
print("\nThe minimum element is {}!".format(min))
print("The maximum element is {}!".format(max))
