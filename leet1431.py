# Leetcode question 1431: Extra Candies

# return a boolean list if k candies + extraCandies is more that extraCandies

def kidsWithCandies(candies, extraCandies):
    # create the return list of boolean values
    bool_list = []
    # loop through entire list using range
    for k in range(len(candies)):
        # added is the value of k in candies + the extraCandies argument
        added = candies[k] + extraCandies
        # append the boolean value if added is more that the max of candies
        bool_list.append(added >= max(candies))
    return bool_list


# Test Cases
print(kidsWithCandies([2, 3, 5, 1, 3], 3))  # [True, True, True, False, True]
