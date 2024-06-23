# Leetcode question 1979: Find greates common divisor in array

def findGCD(nums: list[int]) -> int:
    # sort nums
    nums.sort()
    # create variable for lowest value in nums
    low = nums[0]
    # create variable for highest value in nums
    high = nums[-1]
    # greatest common demoninator list
    gcds = []
    # loop up until low
    for n in range(1, low + 1):
        # if low and high is evenly divided by n
        if low % n == 0 and high % n == 0:
            # append n to gcds list
            gcds.append(n)
    # return the maximum value in gcds to find gcd
    return max(gcds)


# Test Cases
print(findGCD([2, 5, 6, 9, 10]))  # 2
print(findGCD([7, 5, 6, 8, 3]))  # 1
print(findGCD([3, 3]))  # 3
