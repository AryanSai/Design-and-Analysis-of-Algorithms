a=[1,2,3,4,56,7,8,2,3]
negative_infinity = float('-inf')
curr_largest=negative_infinity
i=0

while i!=len(a):
    if a[i] > curr_largest:
        curr_largest = a[i]
        i = i + 1
    else:
        i = i + 1

print(curr_largest)    