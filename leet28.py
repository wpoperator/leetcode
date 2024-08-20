# Leetcode question 28: Neelde in a Haystack

def strStr(haystack: str, needle: str) -> int:
    # get length of needle
    n_length = len(needle)

    # loop through haystack using range
    for char in range(0, len(haystack)):
        # check if current char index value + n_length slice equals needle
        if needle == haystack[char:char + n_length]:
            # return current char index value when true
            return char
        else:
            # otherwise continue the loop
            continue
    # return -1 as default after loop if needle is not found
    return -1


# Test Cases
print(strStr("sadbutsad", "sad"))  # 0
print(strStr("leetcode", "leeto"))  # -1
print(strStr("hello", "ll"))  # 2
