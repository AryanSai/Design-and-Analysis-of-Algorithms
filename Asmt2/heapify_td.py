# heapify top down approach
def heapify(a):
    counter=0
    i = 1
    n = len(a)
    for i in range(1, n):
        child = i
        parent = (i - 1) // 2
        while child > 0 and a[child] < a[parent]:# import random


# def heapify(a):
#     n = len(a)
#     i = 0
#     while i <= n - 1:
#         minimum = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < n and a[i] > a[left]:
#             minimum = left
#         if right < n and a[i] > a[right]:
#             minimum = left
#         if i != minimum:
#             a[i], a[minimum] = a[minimum], a[i]
#             heapify(a)
#         i = i + 1
#     return a


# def heapsort(a):
#     i = 0
#     n = len(a)
#     while i <= n - 1:
#         a[i:] = heapify(a[i:])
#         i = i + 1
#     return a


# a = [8, 6, 4, 2, 0, 3, -2]
# a = random.sample(range(0, 20), 12)
# print(a)
# a = heapsort(a)
# print(a)
print(4/2)
            a[child], a[parent] = a[parent], a[child]
            child = parent
            parent = (child - 1) // 2
            counter+=1
    print("Count = {}".format(counter))        
    return a


# a = random.sample(range(0, 100000), 99999)
a = []
with open("random_numbers.txt", "r") as file:
    numbers_list = file.read().split()
    for number_str in numbers_list:
        number = int(number_str)
        a.append(number)
# print(a)
heapify(a)
print('done')
