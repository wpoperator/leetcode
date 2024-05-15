# Leetcode question 2427: Number of Common Factors

# Given two integers a and b, return the number of common factors of a and b.
# An integer x is a common factor of a and b if x divides both a and b.

def commonFactors(a: int, b: int) -> int:
    # find the maximum number between a and b
    largest = max(a, b)
    # create incrementing variable
    counter = 0
    # loop through numbers from range of 1 to largest + 1 to stay inbounds
    for i in range(1, largest + 1):
        # use modulo operater to check if a and b % i == 0
        if a % i == 0 and b % i == 0:
            # if true, increment the counter variable
            counter += 1
    return counter


# Test Cases
print(commonFactors(12, 6))  # 4
print(commonFactors(25, 30))  # 2
