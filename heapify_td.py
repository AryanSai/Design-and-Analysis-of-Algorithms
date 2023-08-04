# heapify top down approach
def heapify(a):
    counter=0
    i = 1
    n = len(a)
    for i in range(1, n):
        child = i
        parent = (i - 1) // 2
        while child > 0 and a[child] < a[parent]:
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
