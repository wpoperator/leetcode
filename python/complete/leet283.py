# Leetcode question 283: Move Zeros

# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# Do not return anything modify nums in-place

def moveZeroes(nums: list[int]) -> None:
    # create two pointers that start at zero
    i = 0
    j = 0

    # loop until j is greater than the length of nums
    while j < len(nums):
        # check if the value of the j as index of nums is not 0
        if nums[j] != 0:
            # once nums[j] != 0, check if value of i != current value of j
            if i != j:
                # swap values of nums[i] for nums[j]
                nums[i], nums[j] = nums[j], nums[i]
            # increment i to increase pointer value
            i += 1
        # increment j to increase index pointer value if j = 0 or after swap
        j += 1


# Test Cases
print(moveZeroes([0, 1, 0, 3, 12]))  # [0, 0, 1, 3, 12]
print(moveZeroes([0, 0, 1]))  # [0, 0, 1]
