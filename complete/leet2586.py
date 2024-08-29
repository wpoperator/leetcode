# Leetcode question 2586: Count the Number of Vowel Strings in Range

def vowelStrings(words: list[str], left: int, right: int) -> int:
    # vowel list
    vowels = ["a", "e", "i", "o", "u"]
    # counter varible
    count = 0
    # loop through words in the range of left : right + 1 to stay inbounds
    for w in words[left:right + 1]:
        # check if the first and last character is a vowel
        if w[0] in vowels and w[-1] in vowels:
            # increment count when true
            count += 1
    # return final count
    return count


# Test Cases
print(vowelStrings(["are", "amy", "u"], 0, 2))  # 2
print(vowelStrings(["hey", "aeo", "mu", "ooo", "artro"], 1, 4))  # 3
