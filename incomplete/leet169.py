# Leetcode question 169: Majority Element

def majorityElement(nums: list[int]) -> int:
    # create letter dictionary
    letter_dict = {}
    # counter variable
    count = 0
    # loop through nums
    for n in nums:
        # each time n is not in leter_dict
        if n not in letter_dict.keys():
            # set key as n and count as value
            count += 1
            letter_dict[n] = count
        # else just increment the value (count)
        else:
            count = 0
            letter_dict[n] += 1

    # find maximum value of all keys
    maximum = max(letter_dict)
    # return the maximum
    return maximum


# Test Cases
# print(majorityElement([3, 2, 3]))  # 3
# print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(majorityElement([3, 3, 4]))  # 3
