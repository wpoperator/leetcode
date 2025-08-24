def zeroFilledSubarray(nums: list[int]) -> int:
    # Counter variable
    # count = 1
    # dictionary for values
    num_dict = {}
    # loop for all zeros (count single instances)
    for n in nums:
        # increment num_dict value for every instance of 0
        if n == 0 and n in num_dict:
            num_dict[n] += 1
        else:
            num_dict[n] = 1

    return sum(num_dict.values())


# Test Cases
print(zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))  # 6
