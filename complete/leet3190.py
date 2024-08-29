# Leetcode question 3190: Find Minimum Operations to Make All nums / by 3

def minimumOperations(nums: list[int]) -> int:
    # operations variable
    operations = 0
    # loop through nums
    for n in nums:
        # add and subtract 1 from n, check if n is now divisible by 3
        if (n + 1) % 3 == 0 or (n - 1) % 3 == 0:
            # increment operations each time n is divisible by 3
            operations += 1
    # return final operations count
    return operations


# Test Cases
print(minimumOperations([1, 2, 3, 4]))  # 3
print(minimumOperations([3, 6, 9]))  # 0
