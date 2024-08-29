# Leetcode question 1432: Number of Steps to Reduce a Number to Zero

def numberOfSteps(num: int) -> int:
    # create steps variable starting from 0
    steps = 0
    # loop until num == 0
    while num != 0:
        # if num is divisible by 2 evenly, divide by two, increment steps
        if num % 2 == 0:
            num = num // 2
            steps += 1
        # else subtract 1 from num and increment steps
        else:
            num = num - 1
            steps += 1
    return steps


# Test Cases
print(numberOfSteps(14))  # 6
print(numberOfSteps(8))  # 4
print(numberOfSteps(123))  # 12
