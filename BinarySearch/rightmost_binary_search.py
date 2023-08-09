def binary_search_rightmost_index(a, x):
    n = len(a)
    l, u = 0, n - 1

    if n == 0:  # exception case
        return -2
    elif n == 1 and a[0] == x:  # boundary case
        return 0
    elif a[n - 1] == x:  # alternate case
        return n - 1
    while l != u:  # l < u   normal case
        m = (l + u + 1) // 2  # l < m <= u  ceiling
        if x < a[m]:
            u = m - 1
        else:
            l = m
    else:  # l == u
        if a[l] == x:
            return l
        else:  # element not present in the list
            return -1


a = [1, 1, 1, 1, 2, 1]  
# a = [8]
x = 1  # the element we are looking for
a.sort() # the input should be a sorted list
rightmost_index = binary_search_rightmost_index(a, x)
if rightmost_index == -2:
    print("The input list is empty!")
elif rightmost_index == -1:
    print("The element does not exist in the list!")
else:
    print("{} is at the position (rightmost_index): {}".format(x, rightmost_index))
