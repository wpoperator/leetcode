def firstPalindrome(words: list[str]) -> str:
    # loop through words
    for w in words:
        # check if current word equals the reversed word
        if w == w[:: -1]:
            # return current word
            return w
    # else return empty string
    return ""


# Test Cases
print(firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))  # ada
print(firstPalindrome(["notapalindrome", "racecar"]))  # racecar
print(firstPalindrome(["wqibjuqvs", "pp", "usewxryy", "hqwwqftgyu"]))  # pp
