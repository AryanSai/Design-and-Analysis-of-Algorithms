import random

a = random.sample(range(0, 10000), 1000)
print("The list of elements: ",a)
negative_infinity = float('-inf')
curr_largest=negative_infinity
i=0

while i!=len(a):
    if a[i] > curr_largest:
        curr_largest = a[i]
        i = i + 1
    else:
        i = i + 1

print("The largest element",curr_largest)    