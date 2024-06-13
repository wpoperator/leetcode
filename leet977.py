# Leetcode question 977: Squares of a Sorted Array

def sortedSquares(nums: list[int]) -> list[int]:
    # new list to append squared values of n to sort
    new_list = []
    # loop through nums and square each value
    for n in nums:
        n *= n
        # append new squared value of n to new_list
        new_list.append(n)
    # sort new_list
    new_list.sort()
    # return new_list
    return new_list


# Test Cases
print(sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
