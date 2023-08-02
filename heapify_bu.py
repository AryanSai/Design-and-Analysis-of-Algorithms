import random


def heapify(a, n, i):
    while True:
        minimum = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and a[left] < a[minimum]:
            minimum = left
        if right < n and a[right] < a[minimum]:
            minimum = right
        if i != minimum:
            a[i], a[minimum] = a[minimum], a[i]
            i = minimum
        else:
            break    


a = random.sample(range(0, 100), 50)
# a = [8, 2, 7, 5, 4, 12, 9, 1, 0]
print(a)

for i in range(len(a) // 2, -1, -1):
    heapify(a, len(a), i)

print(a)
