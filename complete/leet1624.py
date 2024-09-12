def countConsistentStrings(allowed: str, words: list[str]) -> int:
    # final count of consistent strings
    final_count = 0

    # loop through each word
    for word in words:
        # set character count to zero
        count = 0
        # loop through each letter
        for letter in word:
            # if letter is found in allowed
            if letter in allowed:
                # increment count
                count += 1
                # check if count equals length of word
                if count == len(word):
                    # increment final count as every character is in allowed
                    final_count += 1
    # return the final count
    return final_count


# Test Cases
print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))  # 2
print(countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))  # 7
