# Leetcode question 1935: Maximum Number of Words You Can Type

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    # split text
    split = text.split(" ")
    # counter for each word that can be typed
    count = 0
    # loop through each word of split
    for w in split:
        # get length of w
        length = len(w)
        # second loop through each character
        for c in w:
            # check if currect character exists in brokenletters
            if c not in brokenLetters:
                # reduce length by 1 each character not in brokenletters
                length -= 1
                # if length is zero, all characters if w not in brokenletters
                if length == 0:
                    # increment count if length is zero
                    count += 1
    # return final count
    return count


# Test Cases
print(canBeTypedWords("hello world", "ad"))  # 1
print(canBeTypedWords("leet code", "lt"))  # 1
print(canBeTypedWords("leet code", "e"))  # 0
