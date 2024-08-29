# Leetcode question 1812: Truncate Sentence

# You are given a sentence s​​​​​​ and an integer k​​​​​​. Truncate s
# ​such that it contains only the first k​​​​​​ words.
# Return s​​​​​​ after truncating it.

def truncateSentence(s: str, k: int) -> str:
    # split strings into list
    words_list = s.split(" ")
    # iterator
    i = 0
    # result string to concatenate
    result = ""
    # loop while i is <= 4
    while i <= k - 1:
        # concatentate current word plus space to result
        result += words_list[i] + ' '
        # keep the loop moving
        i += 1
    # return everything but the last space in result
    return result[:-1]


# Test Cases
print(truncateSentence("Hello how are you Contestant", 4))
print(truncateSentence("What is the solution to this problem", 4))
print(truncateSentence("chopper is not a tanuki", 5))
