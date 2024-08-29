# Leetcode question 1967: Number of strings that appear as substrings in word

def numOfStrings(patterns: list[str], word: str) -> int:
    # count the number of substrings found
    count = 0
    # loop through patterns
    for s in patterns:
        if s in word:
            # if s is found in word increment count
            count += 1
    return count


# Test Cases
print(numOfStrings(["a", "b", "c"], "aaaaabbbbb"))  # 2
print(numOfStrings(["a", "abc", "bc", "d"], "abc"))  # 3
print(numOfStrings(["a", "a", "a"], "ab"))  # 3
