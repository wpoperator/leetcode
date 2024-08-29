# Leetcode question 1672: Richest Customer Wealth

# Return the wealth that the richest customer has.


def maximumWealth(accounts: list[list[int]]) -> int:
    # create new list to store sums
    sums_list = []
    # loop through each list and append the sum value to sums_list
    for a in accounts:
        new_sum = sum(a)
        sums_list.append(new_sum)
    # return the maximum value from sums_list
    return max(sums_list)


# Test Cases
print(maximumWealth([[1, 2, 3], [3, 2, 1]]))  # 6
print(maximumWealth([[1, 5], [7, 3], [3, 5]]))  # 10
print(maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # 17
