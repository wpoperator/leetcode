# Leetcode 2529: Maximum Count of Positive Integer and Negative Integer

def maximumCount(nums: list[int]) -> int:
    # counter for positive numbers
    pos = 0
    # counter for negative numbers
    neg = 0

    # loop through nums
    for n in nums:
        # skip any zeros
        if n == 0:
            continue
        # check if current value of n is greater than zero
        elif n > 0:
            # increment pos everytime n is greater
            pos += 1
        else:
            # increment everytime n is less
            neg += 1

    # Return the maximum number between pos, neg
    return max(pos, neg)


# Test Cases
print(maximumCount([-2, -1, -1, 1, 2, 3]))  # 3
print(maximumCount([-3, -2, -1, 0, 0, 1, 2]))  # 3
print(maximumCount([5, 20, 66, 1314]))  # 4
