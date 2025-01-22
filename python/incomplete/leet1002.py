def commonChars(words: list[str]) -> list[str]:
    first_word = words[0]

    res = []

    for c in first_word:
        for i in range(1, len(words)):
            if c in words[i]:
                res.append(c)


# Test Cases
print(commonChars(["bella", "label", "roller"]))
