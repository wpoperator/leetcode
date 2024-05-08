# Leetcode question 3131: Find the Integer Added to Array I

# Return the difference between each value from nums1 to nums2

def addedInteger(nums1: list[int], nums2: list[int]) -> int:
    # find the minimum value of both arguments
    min1 = min(nums1)
    min2 = min(nums2)
    # subtract the minimum of nums1 from minimum value nums2
    return min2 - min1


# Test Cases
print(addedInteger([2, 6, 4], [9, 7, 5]))
print(addedInteger([10], [5]))
print(addedInteger([1, 1, 1, 1], [1, 1, 1, 1]))
