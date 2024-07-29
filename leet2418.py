# Leetcode question 2418: Sort the People

def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    # create people dictionary from a zip of heights, names
    people_dict = {key: value for key, value in zip(heights, names)}
    # sort the people_dict items
    sorted_people = sorted(people_dict.items())
    # create list to return just the names
    result = []
    # loop into sorted people, append just the name to result
    for list in sorted_people:
        result.append(list[1])
    # return result list in reverse
    return result[::-1]


# Test Cases
print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
print(sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]))
