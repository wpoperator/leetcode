# Leetcode question 2828: Check if a String Is an Acronym of Words

def isAcronym(words: list[str], s: str) -> bool:
    # create empty string to concatenate first character of each word
    check_str = ""
    # loop through words
    for w in words:
        # append first character of each word to check_str
        check_str += w[0]
    # after loop compare check_str to s
    return check_str == s


# Test Cases
print(isAcronym(["alice", "bob", "charlie"], "abc"))  # True
print(isAcronym(["an", "apple"], "a"))  # False
print(isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy"))  # True
