import random


def shuffle(n):
    number_list = [i for i in range(1, n + 1)]
    for i in range(len(number_list)):
        random_number = random.randint(i, n - 1)
        number_list[i], number_list[random_number] = (
            number_list[random_number],
            number_list[i],
        )
    return number_list


print(shuffle(20))
