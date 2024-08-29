# Leetcode question 2215: Find the difference between to lists

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    # create new lists for each list to values after loops
    res_list1 = []
    res_list2 = []

    # loop through nums1
    for n in nums1:
        # if current number absent from nums2 and res_list1
        if n not in nums2 and n not in res_list1:
            # append that current number to res_list1
            res_list1.append(n)
    # loop through nums2
    for n2 in nums2:
        # if current number absent from nums2 and res_list2
        if n2 not in nums1 and n2 not in res_list2:
            # append that current number to res_list2
            res_list2.append(n2)

    # return inside list
    return [res_list1, res_list2]


# Test Cases
print(findDifference([1, 2, 3], [2, 4, 6]))  # [[1,3],[4,6]]
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # [[3],[]]
