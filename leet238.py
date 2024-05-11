# Leetcode question 238: Product of array except self

# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

import math


def productExceptSelf(nums: list[int]) -> list[int]:
    # product list to return
    product_list = []
    # copy of nums to use for math.prod task
    nums_copy = nums[:]
    # loop through every value of nums
    for n in range(len(nums)):
        # remove n from the copy of nums
        nums_copy.pop(n)
        # append the product of nums without n
        product_list.append(math.prod(nums_copy))
        # re-insert the value of n back into the copy of nums
        nums_copy.insert(n, nums[n])
    # return the list of products
    return product_list


# Test Cases
print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
