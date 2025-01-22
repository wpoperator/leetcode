# Leetcode question 1408: String Matching in an Array

def stringMatching(words: list[str]) -> list[str]:
    # result set to append unique substring matches
    result = set()

    # loop begins at the first index value, increments x after each y loop
    for x in words:
        # loop through all strings in words
        for y in words:
            # match found when x != y value and x is found inside y
            if x != y and x in y:
                # add each substring found to result set
                result.add(x)
    # return a list of result set values
    return list(result)


# Test Cases
print(stringMatching(["mass", "as", "hero", "superhero"]))  # ["as", "hero"]
print(stringMatching(["leetcode", "et", "code"]))  # ["et", "code"]
print(stringMatching(["blue", "green", "bu"]))  # []
