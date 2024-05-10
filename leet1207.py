# Leetcode question 1207: Number of unique occurences

# Given an array of integers arr, return true if the number of occurrences
# of each value in the array is unique or false otherwise.

def uniqueOccurrences(arr: list[int]) -> bool:
    # create hashmap (dict)
    hash = {}
    # loop through arr
    for n in arr:
        # check if n is in hash
        if n not in hash.keys():
            # add n into hash with the default value of zero
            hash[n] = 0
        # increment every value each pass
        hash[n] += 1
    # compare the len of unique values in a set of hash to the length of hash
    return len(set(hash.values())) == len(hash)


# Test Cases
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
print(uniqueOccurrences([1, 2]))  # False
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
