# Leetcode question 624: Maximum Distance in Arrays

def maxDistance(arrays: list[list[int]]) -> int:
    # create new list to append each number to
    num_list = []
    # loop through each list
    for li in arrays:
        # loop through each number
        for num in li:
            # ignore zeros
            if num > 0:
                # append number to num_list
                num_list.append(num)
    # sort the num_list after loops
    num_list.sort()
    # subtract highest value (last) from the lowest (first)
    return num_list[-1] - num_list[0]


# Test Cases
# print(maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))  # 4
# print(maxDistance([[1], [1]]))  # 0
# print(maxDistance([[1, 4], [0, 5]]))  # 4
print(maxDistance([[1, 5], [3, 4]]))  # 3
