# leetcode question 1791: Find center of star graph

def findCenter(edges: list[list[int]]) -> int:
    # Count occurrences and store in a dictionary
    occurrence_dict = {}
    # loop through each list (l)
    for l in edges:
        # loop through each item (i) in list
        for i in l:
            # assign the key to default value of 0, increment by 1 always
            occurrence_dict[i] = occurrence_dict.get(i, 0) + 1

    # Return the key of the highest value in occurance_dict
    return max(occurrence_dict, key=occurrence_dict.get)


# Test Cases
print(findCenter([[1, 2], [2, 3], [4, 2]]))  # 2
print(findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))  # 1
