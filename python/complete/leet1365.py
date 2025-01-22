# Leetcode question 1365: How Many Numbers Are Smaller Than the Current Number

def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    # counter variable to append to return list
    count = 0
    # return list
    return_list = []
    # loop through nums
    for n in range(len(nums)):
        # pop n from nums
        pop = nums.pop(0)
        # append pop to end of nums
        nums.append(pop)
        # nums slice with last element removed
        removed = nums[:-1]
        # second loop through removed
        for i in removed:
            # check if pop is greater than i
            if pop > i:
                # increment count when true
                count += 1
        # append count after removed loop
        return_list.append(count)
        # reset count to 0
        count = 0
    # return return_list
    return return_list


# Test Cases
print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  # [4, 0, 1, 1, 3]
print(smallerNumbersThanCurrent([6, 5, 4, 8]))  # [2, 1, 0, 3]
print(smallerNumbersThanCurrent([7, 7, 7, 7]))  # [0, 0, 0, 0]
