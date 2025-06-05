# Leetcode question 268: Missing Number

def missingNumber(nums: list[int]) -> int:
    # Edge case if the single integer is 0
    if len(nums) == 1 and nums[0] == 0:
        return 1
    # Edge case if nums is a single integer
    if len(nums) == 1:
        return 0
    # Comparison list
    compare_list = []
    # loop through 1 to length of nums + 1 to skip 0
    for i in range(1, len(nums) + 1):
        compare_list.append(i)
        if nums == compare_list:
            return 0
    # second loop to find missing number from compare_list in nums
    for n in compare_list:
        if n == 0:
            continue
        elif n not in nums:
            return n


# Test Cases
# print(missingNumber([3, 0, 1]))  # 2
# print(missingNumber([0, 1]))  # 2
# print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
# print(missingNumber([1, 2]))  # 0
print(missingNumber([0]))  # 1
