# Leetcode question 14: Longest common prefix

def longestCommonPrefix(strs: list[str]) -> str:
    # create prefix string with first character of first string
    prefix = strs[0][0]


# Test Cases
print(longestCommonPrefix(["flower", "flow", "flight"]))  # fl
# print(longestCommonPrefix(["dog", "racecar", "car"]))  #
# print(longestCommonPrefix(["aa", "ab"]))  # a
