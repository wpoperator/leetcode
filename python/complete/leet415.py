# Leetcode question 415: Add strings
def addStrings(num1: str, num2: str) -> str:
    # required for all leetcode testcases of digits at or above 5000
    sys.set_int_max_str_digits(10000)
    # return a str conversion of each num string coverted as integers
    return str(int(num1) + int(num2))


# Test Cases
print(addStrings("11", "123"))  # 134
