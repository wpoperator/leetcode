# Leetcode question 1832: Check if the Sentence Is Pangram

def checkIfPangram(sentence: str) -> bool:
    # quantity of the length of the alphabet
    alphabet = 26
    # dictionary to use as a hashmap
    letter_dict = {}
    # loop through sentence and add unique values to letter_dict
    for i in range(len(sentence)):
        if sentence[i] not in letter_dict.values():
            letter_dict[i] = sentence[i]
    # if letter_dict equals the length of alphabet then sentence is a pangram
    return len(letter_dict) == alphabet


# Test Cases
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # true
print(checkIfPangram("leetcode"))  # false
