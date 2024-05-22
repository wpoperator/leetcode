def sumOfUnique(nums: list[int]) -> int:
    # create sum to add non-duplicate values
    nonduplicate_sum = 0
    # loop through nums
    for n in range(len(nums)):
        print(nums[n])
    #     removed = nums.pop(n)
    #     if removed in nums:
    #         continue
    #     else:
    #         nonduplicate_sum += removed
    # return nonduplicate_sum


# Test Cases
# print(sumOfUnique([1, 2, 3, 2]))  # 4
print(sumOfUnique([1, 1, 1, 1]))  # 0
