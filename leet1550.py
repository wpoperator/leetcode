# Leetcode question 1550: Three consecutive odds

def threeConsecutiveOdds(arr: list[int]) -> bool:
    # count the number of odds
    odds = 0
    # loop through arr
    for n in arr:
        # each time you find a even reset odds back to zero
        if n % 2 == 0:
            odds = 0
        # otherwise increment odds
        else:
            odds += 1
        # when odds = 3 return true
        if odds == 3:
            return True
    # if odds never reaches three return false
    return False


# Test Cases
print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # True
print(threeConsecutiveOdds([2, 6, 4, 1]))  # False
print(threeConsecutiveOdds([1, 2, 1, 1]))  # False
