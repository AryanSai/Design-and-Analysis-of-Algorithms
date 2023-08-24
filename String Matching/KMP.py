# find the next of the pattern
def next(pattern):
    next = [0] * len(pattern)
    for i in range(1, len(pattern)):
        x = next[i - 1]
        while pattern[i] != pattern[x]:
            if x == 0:
                x = -1
                break
            x = next[x - 1]
        next[i] = x + 1
    return next


pattern = "aabaaba"
print(next(pattern))
# kmp algorithm
