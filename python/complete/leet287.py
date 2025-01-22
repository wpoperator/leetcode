# Leetcode question 287: Find Duplicates

# Find the duplicate value in the list

def findDuplicate(nums: list[int]) -> int:
    # create hashmap
    new_dict = {}
    # initiate a counting variable
    count = 0
    # loop
    for n in nums:
        # if n is not in new_dict values
        if n not in new_dict.values():
            # insert count as key, n as value
            new_dict[count] = n
            # increment count (the key)
            count += 1
        # return any value already found in new_dict which is the duplicate
        else:
            return n


# Test cases
print(findDuplicate([1, 3, 4, 2, 2]))  # 2
print(findDuplicate([3, 1, 3, 4, 2]))  # 3
print(findDuplicate([3, 3, 3, 3, 3]))  # 3
