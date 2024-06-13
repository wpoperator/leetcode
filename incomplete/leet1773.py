def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    # result variable to return
    res = 0
    # loop through items and check if ruleValue is present in each item
    for i in range(len(items)):
        if ruleValue in items[i]:
            # each time it's true increment
            res += 1
    return res


# Test Cases
print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver"))  # 1
print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))  # 2
