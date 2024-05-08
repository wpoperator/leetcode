# Leetcode question 9: Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    # convert the input x from int to string, slice to reverse
    reversed_str = str(x)[::-1]
    # if reversed_str is equal to the string value of x, it is a palindrome
    if reversed_str == str(x):
        return True
    return False


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
