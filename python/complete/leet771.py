# Leetcode question 771: Stones and Jewels

def numJewelsInStones(jewels: str, stones: str) -> int:
    # result variable
    res = 0
    # loop through all stones
    for s in stones:
        # if s is found in jewels
        if s in jewels:
            # increment res
            res += 1
    return res


# Test Cases
print(numJewelsInStones("aA", "aAAbbbb"))  # 3
print(numJewelsInStones("z", "ZZ"))  # 0
