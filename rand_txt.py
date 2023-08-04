import random

max_number = 20000000 # Replace this with your desired maximum number
count = 10000000  # Replace this with the desired count of random numbers
with open("random_numbers.txt", "w") as file:
    for _ in range(count):
        random_number = random.randint(0, max_number)
        file.write(str(random_number) + " ")

print("done")


# random_numbers_list = []
# with open("random_numbers.txt", "r") as file:
#     # content = file.read()
#     numbers_list = file.read().split()
#     for number_str in numbers_list:
#         number = int(number_str)
#         random_numbers_list.append(number)
# # print(random_numbers_list)
