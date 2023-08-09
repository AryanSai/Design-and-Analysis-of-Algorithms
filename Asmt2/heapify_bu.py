# heapify bottom up approach
import random


def heapify(a):
    n = len(a)
    i = n // 2
    counter = 0
    for i in range(len(a) // 2, -1, -1):
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
            counter += 1
    print("Count = {}".format(counter))
    return a


a = []
with open("random_numbers.txt", "r") as file:
    numbers_list = file.read().split()
    for number_str in numbers_list:
        number = int(number_str)
        a.append(number)
# print(a)
heapify(a)
print('done')