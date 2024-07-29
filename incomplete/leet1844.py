# Leetcode question 1844: Replace all digits with characters

def replaceDigits(s: str) -> str:
    # create alphabet variable to use index from
    alphabet = "abcdefghijklmnopqrstuvqxyz"
    # new string to append values to
    result = ""
    # loop through s
    for i in s:
        if i not in alphabet:
            result += alphabet[int(i)]
        else:
            result += i


# Test Cases
print(replaceDigits("a1c1e1"))  # "abcdef"
