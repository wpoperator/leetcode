# Leetcode question 1389: Create Target Array in the Given Order

def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    # result list to insert
    result = []

    # loop through each nums[n] and index[i] as a zip
    for n, i in zip(nums, index):
        # use insert to put the n into the i index
        result.insert(i, n)

    return result


# Test Cases
print(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))  # [0,4,1,3,2]
print(createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))  # [0,1,2,3,4]
