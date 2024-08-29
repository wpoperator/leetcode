# Leetcode question 2535: Difference Between Element Sum and Digit Sum of an Array

def differenceOfSum(nums: list[int]) -> int:
    # first get the sum of nums
    list_sum = sum(nums)
    # split list
    split_list = []
    # loop through nums
    for n in nums:
        # second loop to iterate through string value of n
        for i in str(n):
            # append int value of i to split list
            split_list.append(int(i))
    # return value of list_sum - split_list
    return list_sum - sum(split_list)


# Test Cases
print(differenceOfSum([1, 15, 6, 3]))  # 9
print(differenceOfSum([1, 2, 3, 4]))  # 0
