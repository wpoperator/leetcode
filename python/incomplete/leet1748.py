# Leetcode question 1748: Sum of unique elements

def sumOfUnique(nums: list[int]) -> int:
    # create a separate list for all unique values
    unique = []
    # running sum of all unique values
    run_sum = 0
    # loop through nums
    for n in nums:
        # if n is not in unique
        if n in unique:
            continue
        else:
            # append n to unique
            unique.append(n)    
            # add n to sum
            run_sum += n
    # return run_sum
    return run_sum


# Test Cases
print(sumOfUnique([1, 2, 3, 2]))  # 4
