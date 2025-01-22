# Leetcode question 1833: Maximum Ice Cream Bars

def maxIceCream(costs: list[int], coins: int) -> int:
    # sort costs
    costs.sort()
    # total cost variable
    total = 0
    # count variable
    count = 0
    # loop through each cost
    for c in costs:
        # case if all costs are greater than coins
        if c > coins:
            continue
        # if total does not equal coins yet
        elif total != coins:
            # continue to add c to total
            total += c
            # increment count
            count += 1
        # return the final count
        else:
            return count
    # return count (0) for any case where all costs > coins
    return count


# Test Cases
# print(maxIceCream([1, 3, 2, 4, 1], 7))  # 4
# print(maxIceCream([10, 6, 8, 7, 7, 8], 5))  # 0
# print(maxIceCream([1, 6, 3, 1, 2, 5], 20))  # 6
print(maxIceCream([7, 3, 3, 6, 6, 6, 10, 5, 9, 2], 56))  # 9
