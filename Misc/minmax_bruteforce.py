import random

def find_min_max(arr):
    n = len(arr)
    if n % 2 == 0:  # even-length array
        min_val = min(arr[0], arr[1])
        max_val = max(arr[1], arr[0])
        # start_idx = 2
    else:  # odd-length array
        min_val = max_val = arr[0]
        # start_idx = 1

    for i in range(1, n - 1, 2):
        if arr[i] < arr[i + 1]:
            min_val = min(min_val, arr[i])
            max_val = max(arr[i + 1], max_val)
        else:
            min_val = min(min_val, arr[i + 1])
            max_val = max(arr[i], max_val)
    return min_val, max_val


arr = random.sample(range(0, 100), 10)
print(arr)
min_val, max_val = find_min_max(arr)
print("Minimum:", min_val)
print("Maximum:", max_val)