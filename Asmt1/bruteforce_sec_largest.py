import random

a = random.sample(range(0, 10000), 500)
print("The list of elements: ", a)

# true largest and sec_largest
# b = list(set(a))
# b.sort()
# print(max(a), b[-2])

largest = 0
sec_largest = float("-inf")

i = 0
while i < len(a):
    if a[i] > largest:
        sec_largest = largest
        largest = a[i]
    elif a[i] > sec_largest and a[i] < largest:
        sec_largest = a[i]
    i = i + 1
print(largest, sec_largest)
