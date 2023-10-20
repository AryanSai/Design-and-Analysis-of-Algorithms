# Aryan Sai.A,   Reg.No. 23352
def binary_search(A, x):
    n = len(A)
    l, u = 0, n - 1  # l is the lower bound and u is the upper bound
    while l != u:  # l < u   normal case
        m = (l + u + 1) // 2  # l < m <= u
        if x < A[m]:
            u = m - 1
        else:
            l = m
    else:  # l == u
        if A[l] == x:
            return l
        else:  # element not present in the list
            return -1


x = 4
A = [3, 3, 4, 4, 4, 5, 6]
index = binary_search(A, x)
print("The element x is at the index(rightmost):{}".format(index))
