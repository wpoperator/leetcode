# leecode question 2351: First letter to appear twice

def repeatedCharacter(s: str) -> str:
    # create a hash using a dictionary
    hash = {}
    # loop through entire length of s
    for i in range(len(s)):
        # if the index value of s[i] not present
        if s[i] not in hash.values():
            # input s[i] into hash
            hash[i] = s[i]
        # else s[i] is already in hash so return s[i]
        else:
            return s[i]


# Test Cases
print(repeatedCharacter("abccbaacz"))  # c
print(repeatedCharacter("abcdd"))  # d
