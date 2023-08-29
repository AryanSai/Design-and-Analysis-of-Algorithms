# O((n-m+1)m) time complexity


def robin_karp(str, pattern):
    n = len(str)
    m = len(pattern)
    count = 0
    s = 0  # shift position
    for s in range(
        0, n - m + 1
    ):  # For each of the n-m+1 possible values of the shift s
        if str[s : s + m] == pattern:  # [s:s+m] shift both indices equally
            count += 1
            print("Pattern occurs at index {}".format(s))
    print("Pattern occurred {} many times.".format(count))


def main():
    # str = "aababaababbaab"
    # pattern = "ab"
    text_file = open(
        "/home/dmacs/Desktop/MTech/101P/String Matching/Dictionary.txt", "r"
    )
    str = text_file.read()
    pattern = "apple"
    robin_karp(str, pattern)
    text_file.close()


main()
