# Leetcode question 884: Uncommon words from two sentences

def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    # create a dictionary for words in s1 and s2
    word_dict = {}

    # loop through both s1 and s2
    for word in (s1 + " " + s2).split(" "):
        # check if current word is in word_dict
        if word not in word_dict:
            # assign the value of 1 for first instance
            word_dict[word] = 1
        else:
            # increment any consecutive instance
            word_dict[word] += 1

    # filter out words that appear more than once
    uncommon_words = [word for word, count in word_dict.items() if count == 1]

    return uncommon_words


# Test Cases
print(uncommonFromSentences("this apple is sweet", "this apple is sour"))  # ["sweet, sour"]
print(uncommonFromSentences("apple apple", "banana"))  # ["banana"]
