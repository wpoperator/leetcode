# Leetcode question 881: Boats to save people

# Return the minimum number of boats to carry every given person.

def numRescueBoats(people: list[int], limit: int) -> int:
    # sort the list of people
    people.sort()
    # i starting at 0 for first nth value
    i = 0
    # j equal to the length of people - 1 to stay in bounds
    j = len(people) - 1
    # create incementing variable to return for minimum number of boats
    boat = 0
    # loop to iterate through each nth value of people
    while (i <= j):
        # check if nth value + the next value is less or equal to limit
        if people[j] + people[i] <= limit:
            # increment i to continue through the loop
            i += 1
        # otherwise decrement j to narrow down remaining list of people
        j -= 1
        # increment number of boats needed
        boat += 1
    # return the total number of boats
    return boat


# Test Cases
print(numRescueBoats([1, 2], 3))  # 1
print(numRescueBoats([3, 2, 2, 1], 3))  # 3
print(numRescueBoats([3, 5, 3, 4], 5))  # 4
