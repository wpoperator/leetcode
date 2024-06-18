def maxLengthBetweenEqualCharacters(s: str) -> int:
    # create hashmap
    hash = {}
    # counter variable
    count = 0
    # loop through entire length of s
    for i in range(len(s)):
        # if a duplicate is found and s[i] is equal to the first duplicate
        if s[i] in hash.values() and s[i] == hash[0]:
            # return the count - 1 to eliminate the extra iteration
            return count - 1
        # add the key and value to hash
        hash[i] = s[i]
        # increment count to keep track of number of characters
        count += 1
    # if now match is found return -1
    return -1


# Test Cases
print(maxLengthBetweenEqualCharacters("scayofdzca"))  # 6
# print(maxLengthBetweenEqualCharacters("abca"))  # 2
# print(maxLengthBetweenEqualCharacters("aa"))  # 0
# print(maxLengthBetweenEqualCharacters("cxvya"))  # -1
# print(maxLengthBetweenEqualCharacters("cabbac"))  # 4
