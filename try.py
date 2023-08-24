import copy

arr = [1,2,3,4]
rev=copy.deepcopy(arr)
arr.reverse()
print(arr)
print(rev)
# mini = min(arr[0], arr[len(arr) / 2], arr[len(arr) - 1])
# maxi = max(arr[0], arr[len(arr) / 2], arr[len(arr) - 1])
# arr.remove(mini)
# arr.remove(maxi)
# print(arr[0])
