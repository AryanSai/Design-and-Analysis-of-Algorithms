import random

def median11(a):
    if len(a)==2:
        return a[0]

    # divide the list into sublists
    sublists = [a[j : j + 5] for j in range(0, len(a), 5)]
    print(sublists)

    # sort the sublists
    sublists = [sorted(i) for i in sublists]
    print(sublists)

    # find medians of sublists
    medians = []
    for i in sublists:
        if len(i) == 5:
            medians.append(i[2])
        elif len(i) == 4:
            medians.append(i[1])
        elif len(i) == 3:
            medians.append(i[2])
        elif len(i) == 2:
            medians.append(i[0])
        else:
            medians.append(i[0])
    print(medians)

    # swapping
    zipped_lists = list(zip(medians, sublists))
    sorted_median_lists = sorted(zipped_lists, key=lambda x: x[0])
    swapped_lists = [sublist for median, sublist in sorted_median_lists]
    print(swapped_lists)

    #reduce and conquer
    medians=sorted(medians)
    print("hello",medians)

    median11(medians)

    combined_lists = list(zip(medians, swapped_lists))
    reduced_lists = [
        [elt for elt in sublist if elt > median]
        for median, sublist in combined_lists
    ]
    print(reduced_lists)    

    #create a new list by merging all the sublists 
    new_list = [element for sublist in reduced_lists for element in sublist]
    print(new_list)   

    median11(new_list)      


# a = [
#     11,
#     35,
#     53,
#     76,
#     52,
#     6,
#     48,
#     3,
#     95,
#     39,
#     60,
#     64,
#     85,
#     41,
#     22,
#     58,
#     30,
#     29,
#     70,
#     84,
#     54,
#     2,
#     4,
#     10,
# ]
a = random.sample(range(0, 90), 12)
print(a)
print(sorted(a))

median11 = median11(a)
