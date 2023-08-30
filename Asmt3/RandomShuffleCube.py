import random


def shuffle(n):
    number_list = [i for i in range(1, n + 1)]
    random_numbers = random.sample(range(0, n**3), n)
    zipped_list = dict(zip(number_list, random_numbers))
    sortlist = sorted(zipped_list, key=lambda i: zipped_list[i])
    return sortlist


n = 10
print("A random list of numbers in the range 0,{} : {}".format(n, shuffle(10)))
