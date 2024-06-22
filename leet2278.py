def percentageLetter(s: str, letter: str) -> int:
    # count each time a character equals letter
    count = 0
    # loop through s
    for c in s:
        # if c == letter increment count
        if c == letter:
            count += 1
    # After the loop ends divide count by length of s
    percentage = count / len(s)
    # return integer value afer conversion to integer
    return int(percentage * 100)


# Test Cases
print(percentageLetter("foobar", "o"))  # 33
print(percentageLetter("jjjj", "z"))  # 0
