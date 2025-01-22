# Leetcode question 392: Is Subsequence

# Given two strings s and t, return true/false if s is a subsequence of t

def isSubsequence(s: str, t: str) -> bool:
    # create two pointers that start at zero
    i = 0
    j = 0
    # each match found increases score by 1
    score = 0

    # case if s is empty, automatically return true
    if len(s) == 0:
        return True

    # loop needs to run at least the length of t
    while j < len(t):
        # if score equals len(s), break loop so i doesn't go out of range
        if score == len(s):
            break
        # if a match is found increment both the score and i
        if t[j] == s[i]:
            score += 1
            i += 1
        # after each iteration increment j to continue loop
        j += 1
    # if score is equal to len(s) then all matches were found
    return score == len(s)


# Test Cases
print(isSubsequence("abc", "ahbgdc"))  # True
print(isSubsequence("b", "abc"))  # True
print(isSubsequence("axc", "ahbgdc"))  # False
print(isSubsequence("", "ahbgdc"))  # True
