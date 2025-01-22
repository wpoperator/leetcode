# Leetcode question 1281: Subtract the Product and Sum of Digits of an Integer

import math


def subtractProductAndSum(n: int) -> int:
    # store values for product
    product_list = []
    # store values for sum
    sum_list = []
    # loop through a string variant of n
    for d in str(n):
        # append each item to each list as integer
        product_list.append(int(d))
        sum_list.append(int(d))
    # subtract sum from product
    return math.prod(product_list) - sum(sum_list)


# Test Cases
print(subtractProductAndSum(234))  # 15
print(subtractProductAndSum(4421))  # 21
