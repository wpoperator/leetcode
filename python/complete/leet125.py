# Leetcode question 125: Valid Palindrome

def isPalindrome(s: str) -> bool:
    # create new string to append each lower case value of s
    new_string = ""
    # case when s is empty
    if s == "" or s == " ":
        return True
    # loop through lower case variant of s
    for i in s.lower():
        # skip spaces and check if i is alphanumeric
        if i != " " and i.isalnum():
            # concatenate i
            new_string += i
    # return comparison of new_string to reversed form
    return new_string == new_string[::-1]


# Test Cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False
print(isPalindrome(" "))  # True
print(isPalindrome("0P"))  # False
