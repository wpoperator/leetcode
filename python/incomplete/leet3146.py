# Leetcode question 3146: Permutation Difference Between Two Strings

def findPermutationDifference(s: str, t: str) -> int:
    # result variable
    result = 0
    # hash dictionary for s
    s_dict = {}
    # loop through s and create k,v pairs for index, value
    for c in range(len(s)):
        s_dict[c] = s[c]

    # for v in range(len(t)):

    # sub variable = key index - t index
    # add sub to result


# Test Cases
print(findPermutationDifference("abc", "bac"))
