def compute_next(pattern):
    next = [0] * len(pattern)
    j = 0  # length of prefix that is also suffix for substr ending at i
    for i in range(1, len(pattern)):
        while (
            j > 0 and pattern[i] != pattern[j]
        ):  # we need to find a shorter prefix that is also a suffix
            j = next[j - 1]
        if (
            pattern[i] == pattern[j]
        ):  # we extended current proper prefix and can increment the length of lps
            j += 1
        next[i] = j  # updating the lps of substr ending at i
    return next


def KMPSearch(text, pattern):
    n = len(text)
    m = len(pattern)
    count = 0  # count the number of occurrences
    if m > n:
        print("Pattern String bigger than the Text String!!")
    else:
        next = compute_next(pattern)
        print("The next array of the pattern is: {}".format(next))
        i = 0  # Index for the text
        j = 0  # Index for the pattern
        while i < n:
            if pattern[j] == text[i]:  # if characters match, move both indices forward
                i += 1
                j += 1
                if j == m:
                    count += 1
                    print("Found pattern at index {}".format(str(i - j)))
                    j = next[
                        j - 1
                    ]  # Update j using the "next" array to continue searching
            else:
                if j != 0:  # Characters don't match
                    j = next[j - 1]
                else:  # No useful information in "next," move i forward
                    i += 1
    print("Pattern occurred {} many times.".format(count))


def main():
    text_file = open(
        "/home/dmacs/Desktop/MTech/101P/String Matching/Dictionary.txt", "r"
    )
    text = text_file.read()
    pattern = "apple"
    KMPSearch(text, pattern)
    text_file.close()


main()
