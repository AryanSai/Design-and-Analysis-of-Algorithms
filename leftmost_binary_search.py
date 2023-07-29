def binary_search(a, x):
    n = len(a)
    print(n)
    l, u = 0, n - 1
    if n == 0:  # exception case
        return -2
    elif n == 1 and a[0] == x:  # exception case
        return 0
    elif a[n - 1] == x:  # alternate case
        return n - 1
    while l != u:  # l<u
        m = (l + u) / 2  # l<=m<u
        if x > a[m]:
            l = m + 1
        else:
            u = m
    else:  # l==u
        if a[l] == x:
            return l
        else:
            return -1


a = [1,2,34,2,4,523,2,2,4]  
# a = [8]
x = 2  # the element we are looking for
a.sort() # the input should be a sorted list
leftmost_index = binary_search(a, x)
if leftmost_index == -2:
    print("The input list is empty!")
elif leftmost_index == -1:
    print("The element does not exist in the list!")
else:
    print("{} is at the position (leftmost_index): {}".format(x, leftmost_index))
