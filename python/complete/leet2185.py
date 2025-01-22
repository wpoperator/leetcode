def prefixCount(words: list[str], pref: str) -> int:
    # count variable for each prefix found
    count = 0
    # prefix variable length
    length = len(pref)
    # loop through words
    for w in words:
        # case if the prefix of current word equals pref
        if w[:length] == pref:
            # increment count
            count += 1
    return count


# Test Cases
print(prefixCount(["pay", "attention", "practice", "attend"], "at"))  # 2
print(prefixCount(["leetcode", "win", "loops", "success"], "code"))  # 0
