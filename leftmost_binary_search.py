def binary_search(a, x):
    n = len(a)
    l, u = 0, n - 1
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


a = [1, 1, 2, 2, 3, 4, 5]
x = 2
print("{} is at the position(leftmost):{} ".format(x,binary_search(a, x)))
