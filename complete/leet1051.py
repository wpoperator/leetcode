# Leetcode question 1051: Expected height

def heightChecker(heights: list[int]) -> int:
    # variable to increment incorrect orders between heights vs expected
    res = 0
    # counter variable to increment through the expected list
    count = 0
    # new sorted list of hieghts
    expected = heights.copy()
    expected.sort()
    # loop through each height
    for h in heights:
        # check if current height is not equal to same index of expected
        if h != expected[count]:
            # increment res
            res += 1
        # increment count
        count += 1
    return res


# Test Cases
print(heightChecker([1, 1, 4, 2, 1, 3]))  # 3
print(heightChecker([5, 1, 2, 3, 4]))  # 5
print(heightChecker([1, 2, 3, 4, 5]))  # 0
