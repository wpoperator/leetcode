# Leetcode question 2710: Remove Trailing Zeros From a String

def removeTrailingZeros(num: str) -> str:
    # reverse using slicing the values of num as integers
    reverse = int(num[::-1])
    # return the string of reverse in reverse using slicing
    return str(reverse)[::-1]


# Test Cases
print(removeTrailingZeros("51230100"))  # 512301
print(removeTrailingZeros("123"))  # 123
