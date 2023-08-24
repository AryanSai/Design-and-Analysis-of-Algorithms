# O((n-m+1)m) time complexity

str = "aababaababbaab"
pattern = "ab"
n = len(str)
m = len(pattern)
s = 0  # shift position
for s in range(0, n - m + 1):  # For each of the n-m+1 possible values of the shift s
    if str[s : s + m] == pattern:  # [s:s+m] shift both indices equally
        print("Pattern occurs at index {}".format(s))
