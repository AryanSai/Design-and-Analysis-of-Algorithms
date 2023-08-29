import random


def bruteforce_second_largest(a):
    if len(a) == 0: # exception case
        largest, sec_largest = float("-inf"), float("-inf")
    elif len(a) == 1: #boundary case
        largest, sec_largest = a[0], a[0]
    elif len(a) == 2: # base case
        largest = max(a[0], a[1])
        sec_largest = min(a[0], a[1])
    else:    # normal case
        # true largest and sec_largest
        b = list(set(a))
        b.sort()
        print(
            "\nThe real largest and second largest values are: {}, {}".format(
                max(a), b[-2]
            )
        )

        #calculating the largest and second largest
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
    return largest, sec_largest


a = random.sample(range(0, 10000), 3)
print("The list of elements: {}".format(a))

# from the function
largest, second_largest = bruteforce_second_largest(a)
print(
    "\nThe calculated largest and second largest values are: {}, {}".format(
        largest, second_largest
    )
)
