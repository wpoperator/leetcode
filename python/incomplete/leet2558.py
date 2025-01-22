# Leetcode question 2558: Take Gifts From the Richest Pile

import math


def pickGifts(gifts: list[int], k: int) -> int:
    # Sort gifts
    # gifts.sort()

    # Square root
    squared_number = math.sqrt(gifts[4])
    print("Squared number:", squared_number)

    # Floor value of squared_number
    floor = math.floor(squared_number)
    print("Floor Number: ", floor)

    # Loop through gifts
    # for g in gifts:
    #     print(g)


# Test Cases
print(pickGifts([25, 64, 9, 4, 100], 4))  # 29
