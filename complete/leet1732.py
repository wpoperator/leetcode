# Leetcode question 1732: Find the Highest Altitude

#  You are given an integer array gain of length n where gain[i]
# is the net gain in altitude between points i​​​​​​ and i + 1
# Return the highest altitude of a point.

def largestAltitude(gain: list[int]) -> int:
    # starting variable set to zero
    start = 0
    # create result list
    result = []
    # loop through gain list and add each altitude incrementally
    for a in gain:
        start += a
        # append the altitude after each iteration
        result.append(start)

    # get the highest value from result
    highest = max(result)

    # condition if highest ends up being 0, return 0
    if highest < 0:
        return 0
    # return the highest altitude
    else:
        return max(result)


# Test Cases
print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # 0
print(largestAltitude([-5, 1, 5, 0, -7]))  # 1
