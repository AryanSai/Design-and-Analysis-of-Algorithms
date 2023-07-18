def binary_search_rightmost(a, x):
    n = len(a)
    l, u = 0, n - 1
    while l != u:  # l < u
        m = (l + u + 1) // 2  # l < m <= u
        if x < a[m]:
            u = m - 1
        else:
            l = m
    else:  # l == u
        if a[l] == x:
            return l
        else:
            return -1

a = [1, 1, 2, 2, 3, 4,4, 5]
x = 4
print("{} is at the position (rightmost): {}".format(x,binary_search_rightmost(a, x)))
